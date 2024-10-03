import streamlit as st
import pandas as pd
st.title('Hello')
st.header("Header")
st.subheader("Sub Header")
st.text("I am Text")
st.markdown("""
            # h1 tag 
            ## h2 tag 
            ### h3 tag 
            # :moon:
            # :sunglasses:
            # **Bold** 
            # _Italics_ """,True)

st.latex(r'''  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right) ''')

st.write(st)
st.header("Form")
st.info("This is for form data")
name = st.text_input("**Enter Name:**")
email = st.text_input("**Enter Email:**")
msg = st.text_area("**Enter Your Message:**")
classname = st.selectbox("**Enter Branch**",['CSE','ME','IT','CE','EC'])
#classname = st.selectbox("**Enter Class**",[1,2,3,4])
btn = st.button("Submit")

if btn:
    st.markdown(f'''
    \nName: {name}
    \nEmail: {email}
    \nMessage: {msg}
    \nClass Name: {classname}     ''') 


st.title("Streamlit Code")
st.code('''for i in range(5):
                print(i)''')
st.header("Dataframe Example")
data = pd.read_excel("details.xlsx")
st.dataframe(data)