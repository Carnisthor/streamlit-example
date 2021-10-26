from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Tomorrows Education - Smart City App

This is our entry for the AI and Data Products Challenge @Lara and @Clemens.

Insert some awesome introduction right here
"""
df = pd.read_csv("floor1_compressed.csv")
st.line_chart(df[['date', 'sum']])
