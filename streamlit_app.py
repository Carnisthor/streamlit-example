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
df['date'] = pd.to_datetime(df['date'])
new_df = df[['date', 'sum']].copy()

week_compressed_df = df.resample('W', on='date').sum().copy()

#st.line_chart(new_df.rename(columns={'date':'index'}).set_index('index'))


# Actual data viz

col1, col2, col3 = st.columns(3)
col1.metric('Average energy consumption', '100 kW')
col1.metric('Average energy consumption on weekdays', '50 kW')
col1.metric('Average energy consumption on weekends', '50 kW')

st.line_chart(week_compressed_df)
