# -*- coding: utf-8 -*-
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("coco.csv", delimiter=";")

# Display the most common values in each column
for column in df.columns:
    most_common_value = df[column].mode().iloc[0]
    print(f"Most common value in {column}: {most_common_value}")
