import pandas as pd

# load the csv file into a DataFrame
df = pd.read_csv('database.csv')

print(df.head())
print(df.info())
print(df.describe())

import matplotlib.pyplot as plt
