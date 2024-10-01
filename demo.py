import streamlit as st
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