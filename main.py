import streamlit as st
st.title('Introduction to Streamlit ')
st.text('Hello, streamlit')
st.text('Hello, streamlit',help='This is text')
code = ''' def fun():
	print('This is function') '''

st.code(code)