import pandas as pd

df = pd.read_csv('cars.csv', delimiter=';')

print(df.head())