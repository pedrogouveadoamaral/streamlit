import plotly.express as px
df = px.data.tips()
print(df)
fig = px.pie(df, values='tip', names='day')
fig.show()