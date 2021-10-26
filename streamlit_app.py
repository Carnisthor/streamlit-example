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

chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#df = pd.read_csv("floor1_compressed.csv")
#st.line_chart(df[['date', 'sum']])
