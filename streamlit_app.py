from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import requests

"""
# Tomorrows Education - Smart City App

This is our entry for the AI and Data Products Challenge @Lara and @Clemens.

Insert some awesome introduction right here
"""

# --- Data Preperation section ---
df = pd.read_csv('floor1_compressed.csv', sep=',')
df['sum'] = df['sum'] / 1440

df['date'] = pd.to_datetime(df['date'])
new_df = df[['date', 'sum']].copy()

week_compressed_df = new_df.resample('M', on='date').sum().copy()
overall_sum = df['sum'].sum()
weekend_mean = df.query("weekend == True")['sum'].mean()
weekday_mean = df.query("weekend == False")['sum'].mean()
weekend_sum = df.query("weekend == True")['sum'].sum()
weekday_sum = df.query("weekend == False")['sum'].sum()
wasted_energy_pcrt = (weekend_sum / overall_sum)
energy_price = 0.3194
potential_savings = weekend_sum * energy_price

# Actual data viz
st.header('Energy Cockpit')
st.text('The energy Cockpit shows the energy consumption of your building.')
col1, col2, col3 = st.columns(3)
col1.metric('Total energy consumption', str(int(overall_sum)) + ' kWh')
col2.metric('Ø consumption on weekdays', str("{:.2f}".format(weekday_mean)) + ' kWh')
col3.metric('Ø consumption on weekends', str("{:.2f}".format(weekend_mean)) + ' kWh')

st.line_chart(week_compressed_df.rename(columns={'sum':'Energy Consumption (kWh)'}))

st.subheader('Potential savings')
col4, col5, col6 = st.columns(3)
col4.metric('From total', str("{:.2f}".format(wasted_energy_pcrt * 100) + ' %'))
col5.metric('In energy', str("{:.2f}".format(weekend_sum)) + ' kWh')
col6.metric('Monetary', str("{:.2f}".format(potential_savings)) + ' EUR')

st.caption('/* All energy savings are calculated on the basis that the AC is completly turned off during weekends.')

st.header('Magic glass ball')
# url = 'https://unplu.gg/forecast'
# data = ''
# for index, row in df.iterrows():
  # data = data + "{'row['date']}"
if st.button('Predict the future (6 weeks)'):
  chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a','b','c'])
  st.line_chart(chart_data)
else:
  # Nothing will happen here

st.header('Energy inspector')
"""
The energy inspector shows detailed information on what could be improved to save energy.
"""
first_date = date.fromisoformat('2018-07-01')
last_date = date.fromisoformat('2019-12-31')
date = st.date_input('Select a date to inspect')
st.info('Feature is currently not available')
