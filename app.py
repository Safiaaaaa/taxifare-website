import streamlit as st
import datetime
import requests
import pandas as pd
from streamlit_folium import folium_static
import folium


'''
### Predict the fare amount of your taxi ride in NYC'''

st.markdown('''
We'll just need a few information
''')


date = st.date_input(
     "Pickup date",
     datetime.date(2022, 8, 6))
time = st.time_input('Pickup time', datetime.time(12, 00))
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.slider('Passenger count', 1, 10,1)

m = folium.Map(location=[pickup_latitude, pickup_longitude], zoom_start=6)

## Once we have these, let's call our API in order to retrieve a prediction

##See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

##🤔 How could we call our API ? Off course... The `requests` package 💡


url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')




# 2. Let's build a dictionary containing the parameters for our API...

date_and_time = datetime.datetime.combine(date,
                          time)
parameters = {'pickup_datetime': date_and_time,
'pickup_longitude': pickup_longitude,
'pickup_latitude': pickup_latitude,
'dropoff_longitude': dropoff_longitude,
'dropoff_latitude': dropoff_latitude,
'passenger_count': passenger_count}

# 3. Let's call our API using the `requests` package...
url = 'https://taxifare.lewagon.ai/predict'
response = requests.get('https://taxifare.lewagon.ai/predict', params=parameters).json()

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user

st.markdown(f'### Your ride will cost you about {round(response["fare"], 1)}')

route = pd.DataFrame({'lat': [pickup_latitude , dropoff_latitude], 'lon': [pickup_longitude, dropoff_longitude]})
st.map(route)
