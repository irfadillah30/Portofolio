import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def plot_histogram():
    data = pd.read_csv('flight.csv')
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    st.write("### Histogram untuk Kolom Numerik")
    for column in numeric_columns:
            fig, ax = plt.subplots()
            ax.hist(data[column].dropna(), bins=30, edgecolor='black')
            ax.set_title(f'Histogram of {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)