import pandas as pd
#import autogluon
import pycaret

pd.set_option('display.max_columns', 100)

df = pd.read_csv('cars.csv', delimiter=';')
df.drop(columns='Unnamed: 17', inplace=True)


print(df.head())
print(df.shape)
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())