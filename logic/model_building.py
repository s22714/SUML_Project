import pandas as pd
import autogluon
from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split


def load_dataset():
    return pd.read_csv('../datasets/cars_cleaned.csv')


def model_creation_and_training(df):
    train, test = train_test_split(df, train_size=0.7, random_state=2024)
    train.drop(columns='price_usd', axis=1)

    train_data = TabularDataset(train)

    predictor = TabularPredictor(label='price_usd', eval_metric="root_mean_squared_error", path='../models/bestModel').fit(
        train_data, presets="medium_quality", excluded_model_types=['NN_TORCH', 'FASTAI'],
        fit_weighted_ensemble=False)

    test_data = TabularDataset(test)

    predctions = predictor.predict(test_data)

    print(predctions)

    print(predictor.leaderboard())


def model_creation():
    df = load_dataset()
    model_creation_and_training(df)
