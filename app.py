import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

base_df = pd.read_csv('cars_cleaned.csv')

st.set_page_config(page_title='Predykcja ceny samochodu', layout='wide')

st.title('Predykcja ceny samochodu')
st.markdown('Wprowadź parametry swojego pojazdu, aby oszacować jego wartość rynkową.')
manufacturer_name = st.selectbox('Marka samochodu', base_df['manufacturer_name'].unique())
model_name = st.text_input('Model')
transmission = st.selectbox('Skrzynia biegów', base_df['transmission'].unique())
color = st.selectbox('Kolor', base_df['color'].unique())
odometer_value = st.number_input('Przebieg (w km)', min_value=0.0, step=1000.0)
year_produced = st.slider('Rok produkcji', 1980, 2024, 2010)
engine_fuel = st.selectbox('Rodzaj paliwa', base_df['engine_fuel'].unique())
engine_has_gas = st.checkbox('Instalacja LPG', value=False)
engine_type = st.selectbox('Typ silnika', base_df['engine_type'].unique())
engine_capacity = st.number_input('Pojemność silnika w litrach', min_value=0.5, max_value=6.0, step=0.1)
body_type = st.selectbox('Typ nadwozia', base_df['body_type'].unique())
has_warranty = st.checkbox('Posiada gwarancję', value=False)
state = st.selectbox('Stan pojazdu', base_df['state'].unique())
drive = st.selectbox('Napęd', base_df['drive'].unique())
first_user = st.checkbox('Pierwszy właściciel', value=True)
button = st.button('Oblicz cenę')
if button:
    if model_name in base_df['model_name'].unique():
        predictor = TabularPredictor.load('bestModel')
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
        st.success(f'Przewidywana cena samochodu: {prediction[0]:,.2f} USD')
    else:
        st.error('Podanego modelu nie ma bazie danych')