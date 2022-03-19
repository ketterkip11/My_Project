import pyreadr
import numpy as np
data = pyreadr.read_r('/home/ketter/Downloads/Interview_tasks/Task1/task1.rds')
df = data[None]
# print(df.head())
# print(df.head())
# df.to_csv("winwin.csv", index=False)
"""columns present in dataset"""
# print(df.columns)
col_names = df.columns.tolist()
print("column names:",col_names)
"""summary of the dataset"""
# print(df.info())
"""shape of dataset"""
# print(df.shape)
"""check for null data"""
# print(df.isna().sum())
# print(df.isnull().sum())
"""check for duplicates"""
# print(df.duplicated().value_counts())
# print(df['unit_price'].unique())
"""Descriptive stats"""
# print(df.describe())

print(df['d_date_id'].min())

