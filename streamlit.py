import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('covid-variants.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
paises = list(df['location'].unique())
variants = list(df['variant'].unique())

tipo = 'Casos diários'
titulo = tipo + ' para '

pais = st.sidebar.selectbox('Selecione o pais', ['Todos'] + paises)
variante = st.sidebar.selectbox('Selecione a variante', ['Todas'] + variants)


if (pais != 'Todos'):
    st.header('Mostrando dados para ' + pais)
    df = df[df['location'] == pais]
    titulo = titulo + pais
else:
    st.header('Mostrando dados para todos os países')

if (variante != 'Todas'):
    st.text('Mostrando dados para a variante ' + variante)
    df = df[df['variant'] == variante]
    titulo = titulo + ' (variante : ' + variante + ')'
else:
    st.text('Mostrando dados para todas as variantes')
    titulo = titulo + '(todas as variantes)'

dfShow = df.groupby(by=["date"]).sum()

fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title=titulo)
st.plotly_chart(fig, use_container_width=True)

df2 = px.data.tips()
print(df2)
fig2 = px.pie(df, names='variant', values='num_sequences')
fig.update_layout(title=titulo)
st.plotly_chart(fig2, use_container_width=True)

