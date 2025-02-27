import streamlit as st
import numpy as np
import pandas as pd

st.title('Introduction to Streamlit ')
st.subheader('This is use of text')
st.text('Hello, streamlit')
st.text('Hello, streamlit',help='This is text')
st.subheader('This is use of code')
code = ''' def fun():
	print('This is function') '''
st.code(code)
st.subheader('This is slider')
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.subheader('Plot a map')
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(map_data)

st.subheader('Draw a line chart')
chart_data = pd.DataFrame(
	np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.subheader('Dataframe')
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)