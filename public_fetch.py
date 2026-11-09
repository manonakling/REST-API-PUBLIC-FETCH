#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:49:00 2026

@author: manonkling
"""


import asyncio
import aiohttp

URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleVariableList?format=json"


async def fetch_vehicle_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            response.raise_for_status()
            data = await response.json()

            filtered_data = [
                item for item in data["Results"]
                if item.get("GroupName") == "Active Safety System"
            ]


            print(
                "All records match filter:",
                all(
                    item.get("GroupName") == "Active Safety System"
                    for item in filtered_data
                )
            )

            return filtered_data


async def main():
    results = await fetch_vehicle_data()

    print("ACTIVE SAFETY SYSTEM VEHICLE VARIABLES")
    print("-" * 45)

    for item in results:
        print("Name:", item.get("Name"))
        print("Description:", item.get("Description"))
        print("-" * 45)

    print("Total matching records:", len(results))


if __name__ == "__main__":
    asyncio.run(main())
