from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import datetime
import requests

def isThisWeekend(day):
  weekno = day.datetime.today().weekday()
  if weekno < 5:
    return True
  else:  # 5 Sat, 6 Sun
    return False
# Again a placeholder
  
"""
# Tomorrows Education - AI & Data Products Challenge Prototyp
This app is the prototyp for the AI & Data Products challenge by Lara, Jan & Clemens.
The goal of the prototyp is to provide actionable insights on the energy consumption of a building with recommendations on how to optimize it - 
thus reducing overall energy consumption and cost. More detailed infomration can be found in the respective Google Drive and Pitch Deck.
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
st.caption('The energy Cockpit shows the energy consumption of your building. For this prototype we have solely on the AC related energy consumption and only for a single floor of our building')
col1, col2, col3 = st.columns(3)
col1.metric('Total AC energy consumption', str(int(overall_sum)) + ' kWh')
col2.metric('Ø AC consumption on weekdays', str("{:.2f}".format(weekday_mean)) + ' kWh')
col3.metric('Ø AC consumption on weekends', str("{:.2f}".format(weekend_mean)) + ' kWh')

st.line_chart(week_compressed_df.rename(columns={'sum':'Energy Consumption (kWh)'}))

st.subheader('Potential savings')
st.caption('All energy savings are calculated on the basis that the AC is completly turned off during weekends.')
col4, col5, col6 = st.columns(3)
col4.metric('From total', str("{:.2f}".format(wasted_energy_pcrt * 100) + ' %'))
col5.metric('In energy', str("{:.2f}".format(weekend_sum)) + ' kWh')
col6.metric('Monetary', str("{:.2f}".format(potential_savings)) + ' EUR')

st.header('Magic glass ball')
st.caption('The magic glass ball feature allows a forecast of the energy consumption of the building for the next 6 weeks.')
# Since forecast creation is not possible here in Streamlit Cloud, we will fallback on this workaround
if st.button('Predict the future (6 weeks)'):
  series = pd.date_range(start='2020-01-01', end='2020-02-09', freq='D')
  df_from_series = series.to_frame()
  df_from_series['Prediction'] = np.random.randint(df['sum'].min(), df['sum'].max(), size=(len(df_from_series)))
  reduced_series = df_from_series['Prediction']
  st.line_chart(reduced_series)
else:
  a = 1
# Nothing will happen here

st.header('Energy inspector')
"""
The energy inspector shows detailed information on what could be improved to save energy.
"""
d = st.date_input(label='Select a date to inspect', value=datetime.date(2019, 10, 28), min_value=datetime.date(2018, 7, 1), max_value=datetime.date(2019, 12, 31))
#st.write(d)
if d:
  random()
else:
  12
# Placeholder
