import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def tampilakan_dashboard():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
    st.pie_chart(data['a'].value_counts())
    st.line_chart(data)
    st.bar_chart(data)
    
    st.markdown("## Dataframe")
    range_slider = st.slider("Select range of values :", 0, 100, (25, 75))
    st.write(f"Selected range: {range_slider}")
    