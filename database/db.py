# This file contains the database connection and query execution functions
from contextlib import asynccontextmanager

import aiopg

from conf.config import settings


# Function to establish a connection with the database
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


# Function to execute a select query and return the results
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
    async with database_connection() as conn:
        await conn.execute(custom_query)


"""In the above code snippet, we have defined a context manager called database_connection that establishes a connection 
with the database using the aiopg library. The async_select_one and async_select_all functions execute select queries and 
return the results. The async_insert function is used to execute insert queries. These functions are used to interact with 
the database in the services/scrapper.py script."""
