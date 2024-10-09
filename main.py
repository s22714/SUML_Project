import pandas as pd

df = pd.read_csv('cars.csv')

df = df.drop(columns=['feature_0',
                      'feature_1',
                      'feature_2',
                      'feature_3',
                      'feature_4',
                      'feature_5',
                      'feature_6',
                      'feature_7',
                      'feature_8',
                      'feature_9',
                      'location_region',
                      'is_exchangeable'])

df.loc[df["up_counter"] <= 1, "up_counter"] = 1
df.loc[df["up_counter"] > 1, "up_counter"] = 0

print(df.head())