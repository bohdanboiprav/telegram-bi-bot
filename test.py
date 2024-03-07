import asyncio

from database.db import async_select_one, async_select_all

query = """SELECT *
            FROM stock_data
            WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM stock_data)
        """
cases = asyncio.run(async_select_all(query))
print(cases)
print([x[2:] for x in cases])
