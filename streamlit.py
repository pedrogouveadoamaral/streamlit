import pandas as pd
import streamlit as st



df = pd.read_csv('covid-variants.csv')

pais = list(df['location'].unique())

variante = list(df['location'].unique())