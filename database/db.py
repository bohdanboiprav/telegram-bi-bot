from contextlib import asynccontextmanager

import aiopg
import boto3
from conf.config import settings


@asynccontextmanager
async def database_connection():
    try:
        async with aiopg.connect(host=settings.ENDPOINT, port=settings.PORT, database=settings.DBNAME,
                                 user=settings.DB_USER, password=settings.PASSWORD,
                                 sslrootcert="SSLCERTIFICATE") as conn:
            async with conn.cursor() as cur:
                yield cur
    except Exception as e:
        raise
    finally:
        pass


async def async_select_one(custom_query: str):
    async with database_connection() as conn:
        await conn.execute(custom_query)
        query_results = await conn.fetchone()
        return query_results


async def async_select_all(custom_query: str):
    async with database_connection() as conn:
        await conn.execute(custom_query)
        query_results = await conn.fetchall()
        return query_results


async def async_insert(custom_query: str):
    session = boto3.Session(aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
                            aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY, region_name=settings.AWS_REGION)
    client = session.client('rds')

    token = client.generate_db_auth_token(DBHostname=settings.ENDPOINT, Port=settings.PORT, DBUsername=settings.DB_USER,
                                          Region=settings.REGION)

    try:
        async with aiopg.connect(host=settings.ENDPOINT, port=settings.PORT, database=settings.DBNAME,
                                 user=settings.DB_USER, password=settings.PASSWORD,
                                 sslrootcert="SSLCERTIFICATE") as conn:
            async with conn.cursor() as cur:
                await cur.execute(custom_query)
                await conn.commit()
    except Exception as e:
        print("Database connection failed due to {}".format(e))
