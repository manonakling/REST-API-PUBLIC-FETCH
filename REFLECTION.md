#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:02:41 2026

@author: manonkling
"""

For this assignment, I developed a Python application that asynchronously retrieves public vehicle information from the National Highway Traffic Safety Administration (NHTSA) API. Using asyncio and aiohttp. I created an HTTP request, processed the JSON response, and filtered the data to include only records categorized under “Active Safety System.”

I began by creating my Python file in Spyder and confirming the necessary packages were installed. One challenge I encountered was troubleshooting a Spyder kernel issue, followed by an indentation error when adding code to verify my results. After correcting the indentation and testing the program through Terminal, I successfully retrieved 11 matching records and confirmed that the filter returned “True.”

I was surprised by how much information a public API can return with relatively little code. Throughout the process, I gained a better understanding of asynchronous programming, JSON filtering, HTTP requests, and the importance of debugging. This assignment similarly strengthened my understanding of interoperability and how different applications exchange information through APIs. In the future, I would like to investigate additional error-handling techniques.

