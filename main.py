import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
from logic.data_cleaner import data_cleaning_and_encoding


def model_creation(path):
    pd.set_option('display.max_columns', 100)
    df = pd.read_csv(path)
    data = TabularDataset(df)

    train_size = int(38530 * 0.8)
    seed = 1080
    train_set = data.sample(train_size, random_state=seed)
    test_set = data.drop(train_set.index)

    print(test_set)

    train_data = TabularDataset(train_set)
    predictor = TabularPredictor(label='price_usd', eval_metric="root_mean_squared_error", path='bestModel').fit(train_data, presets="medium_quality", excluded_model_types=['NN_TORCH', 'FASTAI'],
             fit_weighted_ensemble=False)

    test_data = TabularDataset(test_set)

    predictions = predictor.predict(test_data)
    print(predictions)

    leaderboard = predictor.leaderboard()
    print(leaderboard)

    print(predictor.evaluate(train_data))

