import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def tampilakan_dashboard():
    data = pd.read_csv('flight.csv')
    st.write("Preview Data:")
    st.write(data.select_dtypes(include=['float64', 'int64']).head())