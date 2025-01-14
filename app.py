import kagglehub
import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor
from logic.data_cleaner import data_cleaning_and_encoding
from logic.model_building import model_creation

try:
    open('datasets/cars_cleaned.csv', 'r')
except Exception:
    path = kagglehub.dataset_download("lepchenkov/usedcarscatalog", force_download=True)
    data_cleaning_and_encoding(path + "/cars.csv")

try:
    TabularPredictor.load("models/bestModel")
except Exception:
    model_creation()

base_df = pd.read_csv('datasets/cars_cleaned.csv')

st.set_page_config(page_title='Predykcja ceny samochodu')

st.title('Predykcja ceny samochodu')
st.markdown('Wprowadź parametry swojego pojazdu, aby oszacować jego wartość rynkową.')
manufacturer_name = st.selectbox('Marka samochodu', sorted(base_df['manufacturer_name'].unique()))

model_name_for_selected_manufacturer = sorted(base_df[base_df['manufacturer_name'] == manufacturer_name]['model_name'].unique())
model_name = st.selectbox('Model', model_name_for_selected_manufacturer)

transmission_for_selected_model = base_df[base_df['model_name'] == model_name]['transmission'].unique()
transmission = st.selectbox('Skrzynia biegów', transmission_for_selected_model)

color = st.selectbox('Kolor', base_df['color'].unique())

odometer_value = st.number_input('Przebieg (w km)', min_value=0.0, step=1000.0)

year_produced = st.slider('Rok produkcji', 1980, 2024, 2010)

engine_fuel_for_selected_model = base_df[base_df['model_name'] == model_name]['engine_fuel'].unique()
engine_fuel = st.selectbox('Rodzaj paliwa', engine_fuel_for_selected_model)

engine_has_gas = st.checkbox('Instalacja LPG', value=False)

engine_type_for_selected_model = base_df[base_df['engine_fuel'] == engine_fuel]['engine_type'].unique()
engine_type = st.selectbox('Typ silnika', engine_type_for_selected_model)

engine_capacity = st.number_input('Pojemność silnika w litrach', min_value=0.2, max_value=8.0, step=0.1)

body_type_from_model = base_df[base_df['model_name'] == model_name]['body_type'].unique()
body_type = st.selectbox('Typ nadwozia', body_type_from_model)

has_warranty = st.checkbox('Posiada gwarancję', value=False)

state = st.selectbox('Stan pojazdu', base_df['state'].unique())

drive_from_model = base_df[base_df['model_name'] == model_name]['drive'].unique()
drive = st.selectbox('Napęd', base_df['drive'].unique())

first_user = st.checkbox('Pierwszy właściciel', value=True)

currency = st.selectbox('Waluta', ('PLN', 'USD'))

button = st.button('Oblicz cenę')

if button:
    if model_name in base_df['model_name'].unique():
        predictor = TabularPredictor.load('models/bestModel')
        input_data = pd.DataFrame({
            'manufacturer_name': [manufacturer_name],
            'model_name': [model_name],
            'transmission': [transmission],
            'color': [color],
            'odometer_value': [odometer_value],
            'year_produced': [year_produced],
            'engine_fuel': [engine_fuel],
            'engine_has_gas': [engine_has_gas],
            'engine_type': [engine_type],
            'engine_capacity': [engine_capacity],
            'body_type': [body_type],
            'has_warranty': [has_warranty],
            'state': [state],
            'drive': [drive],
            'first_user': [first_user],
            'duration_listed': [0]
        })
        prediction = predictor.predict(input_data)
        if currency == "PLN":
            prediction *= 4
            if prediction[0] <= 0:
                st.error(
                    f'Samochód nie nadaje się do sprzedaży. Jego przewidywana cena jest mniejsza od 0. {prediction[0]:,.2f} PLN')
            else:
                st.success(f'Przewidywana cena samochodu: {prediction[0]:,.2f} PLN')
        else:
            if prediction[0] <= 0:
                st.error(
                    f'Samochód nie nadaje się do sprzedaży. Jego przewidywana cena jest mniejsza od 0. {prediction[0]:,.2f} USD')
            else:
                st.success(f'Przewidywana cena samochodu: {prediction[0]:,.2f} USD')
    else:
        st.error('Podanego modelu nie ma bazie danych')
