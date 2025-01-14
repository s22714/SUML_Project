import numpy as np
import pandas as pd
import kagglehub
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATASET_URL = 'lepchenkov/usedcarscatalog'


def download_dataset():
    path = kagglehub.dataset_download(DATASET_URL, force_download=True)
    df = pd.read_csv(f'{path}/cars.csv')
    return df


def data_cleaner(df, delimiter=',', m_th=0.5, num_strategy='mean', cat_strategy='most_frequent'):
    df['drive'] = df['drivetrain']
    df.drop(columns=['drivetrain', 'is_exchangeable', 'location_region',
                     'number_of_photos', 'feature_0', 'feature_1', 'feature_2',
                     'feature_3', 'feature_4', 'feature_5', 'feature_6', 'feature_7',
                     'feature_8', 'feature_9'], inplace=True)

    df['first_user'] = df['up_counter'] > 1
    df.drop(columns=['up_counter'], inplace=True)

    missing_per_row = df.isnull().mean(axis=1)
    df_clean = df[missing_per_row <= m_th].copy()

    num_columns = df_clean.select_dtypes(include=['float64', 'int64']).columns
    cat_columns = df_clean.select_dtypes(include=['object']).columns

    imp = SimpleImputer(missing_values=np.nan, strategy=num_strategy)

    df_clean[num_columns] = imp.fit_transform(df_clean[num_columns])

    imp = SimpleImputer(missing_values=np.nan, strategy=cat_strategy)

    df_clean[cat_columns] = imp.fit_transform(df_clean[cat_columns])

    return df_clean


def label_encoding(df):
    num_columns = df.select_dtypes(include=['float64', 'int64']).columns
    cat_columns = df.select_dtypes(include=['object']).columns

    encoder = OneHotEncoder(sparse_output=False)
    encoded_cat = encoder.fit_transform(df[cat_columns])
    encoded_cat_df = pd.DataFrame(encoded_cat, columns=encoder.get_feature_names_out(cat_columns))

    scaler = StandardScaler()
    scaled_num = scaler.fit_transform(df[num_columns])
    scaled_num_df = pd.DataFrame(scaled_num, columns=num_columns)

    df = pd.concat([scaled_num_df.reset_index(drop=True), encoded_cat_df.reset_index(drop=True)], axis=1)
    return df


def data_cleaning_and_encoding(delimiter=','):
    df = download_dataset()
    df = data_cleaner(df, delimiter=delimiter)
    df.to_csv('../datasets/cars_cleaned.csv', index=False)
    df = label_encoding(df)

    return df


if __name__ == '__main__':
    data_cleaning_and_encoding()
