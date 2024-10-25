#!/usr/bin/env python3
import pandas as pd

chunk_size = 10000

try:
    for chunk in pd.read_csv('data/netflix_titles.csv', chunksize=chunk_size):
        print(chunk.head())
except FileNotFoundError:
    print("The file was not found.")
except pd.errors.EmptyDataError:
    print("No data in the file.")
except pd.errors.ParserError:
    print("Error parsing the data.")
