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

week_compressed_df = new_df.resample('W', on='date').sum().copy()
overall_sum = df['sum'].sum()
weekend_mean = df.query("weekend == True")['sum'].mean()
weekday_mean = df.query("weekend == False")['sum'].mean()

#st.line_chart(new_df.rename(columns={'date':'index'}).set_index('index'))


# Actual data viz

col1, col2, col3 = st.columns(3)
col1.metric('Overall energy consumption', str(int(overall_sum)) + 'kWh')
col2.metric('Ø consumption on weekdays', str(int(weekday_mean)) + 'kWh')
col3.metric('Ø consumption on weekends', str(int(weekend_mean)) + 'kWh')

st.area_chart(week_compressed_df)
