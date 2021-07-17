import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Indian Election Results Analysis')
st.header('(1) Analysis Based on Seats Won Percentage : NDA (BJP & Allies) vs UPA & Others (Congress Allaince and other independent parties/ entities): ')
st.subheader('✔ 2019 Indian Lok Sabha Election Results Visualization')
st.text('Straightforward visualization of the 2019 Indian Lok Sabha Election results.')

df = pd.read_csv('2019Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='NDA Alliance',
    range_color = [50,100],
    color_continuous_scale = 'oryel',
    title = '2019 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.subheader('✔ 2014 Indian Lok Sabha Election Results Visualization')
st.text('Straightforward visualization of the 2014 Indian Lok Sabha Election results.')
df = pd.read_csv('2014Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='NDA Alliance',
    range_color = [50,100],
    color_continuous_scale = 'oryel',
    title = '2014 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.header('(2) Analysis Percentage Wise Based on Individual Political Party Performance : Only BJP vs Only Congress: ')
st.subheader('✔ 2014 Indian Lok Sabha Election - BJP Performance')
df = pd.read_csv('2014Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='BJP_Performance',
    range_color = [0,100],
    color_continuous_scale = 'Peach',
    title = 'BJPs Performance in 2014 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.subheader('✔ 2019 Indian Lok Sabha Election - BJP Performance')
df = pd.read_csv('2019Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='BJP_Performance',
    range_color = [0,100],
    color_continuous_scale = 'Peach',
    title = 'BJPs Performance in 2019 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.subheader('✔ 2014 Indian Lok Sabha Election - Congress Performance')
df = pd.read_csv('2014Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Congress_Performance',
    range_color = [0,100],
    color_continuous_scale = 'Emrld',
    title = 'Congress Performance in 2014 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)

st.subheader('✔ 2019 Indian Lok Sabha Election - Congress Performance')
df = pd.read_csv('2019Elections.csv')
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Congress_Performance',
    range_color = [0,100],
    color_continuous_scale = 'Emrld',
    title = 'Congress Performance in 2019 Indian Lok Sabha Elections'
)
fig.update_geos(fitbounds="locations", visible=False)

st.plotly_chart(fig)