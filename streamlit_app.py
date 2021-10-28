from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

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

weekdays_only_df = df[df['weekend'] == False]
new_new_df = weekdays_only_df[['date', 'sum']].copy()
weekdays_compressed_df = new_new_df.resample('M', on='date').sum().copy()
weekdays_compressed_df.rename(columns={'sum':'sum2'})
test = pd.concat([week_compressed_df, weekdays_compressed_df], ignore_index=True)


#st.line_chart(new_df.rename(columns={'date':'index'}).set_index('index'))


# Actual data viz


st.header('Energy Cockpit')
st.text('The energy Cockpit shows the energy consumption of your building.')
col1, col2, col3 = st.columns(3)
col1.metric('Total energy consumption', str(int(overall_sum)) + ' kWh')
col2.metric('Ø consumption on weekdays', str(int(weekday_mean)) + ' kWh')
col3.metric('Ø consumption on weekends', str(int(weekend_mean)) + ' kWh')

st.area_chart(week_compressed_df.rename(columns={'sum':'Energy Consumption (kWh)'}))

col4, col5, col6 = st.columns(3)
col4.metric('Potentital energy savings (%)', int(wasted_energy_pcrt * 100))
col5.metric('Potential savings (kWh)', str(int(weekend_sum)) + ' kWh')
col6.metric('Potential savings (€)', int(potential_savings))

st.area_chart(test)
