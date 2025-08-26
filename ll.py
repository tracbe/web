import streamlit as st 


st.title("sidebar less")

st.sidebar.image("c:/Users/Pc SToRe/Downloads/download.jpeg")

age = st.sidebar.slider("age",0,100)
st.sidebar.selectbox("select:", [1 , 2 ,3])

c1 ,c2 ,c3 = st.sidebar.columns(3)
with c1 :
    st.image("c:/Users/Pc SToRe/Downloads/download.jpeg")
with c2 :
    st.image("c:/Users/Pc SToRe/Downloads/images.jpeg")
with c3 :
    st.image("c:/Users/Pc SToRe/Downloads/download.jpeg")

x1 , x2 ,x3, x4 , x5 = st.columns(5)
with x1 :
     st.image("c:/Users/Pc SToRe/Downloads/download.jpeg")


word = "link"
link = "https://www.w3schools.com/python/python_getstarted.asp"

st.markdown(f"press [{word}]({link})")

st.markdown(f"press [LINK]('https://www.w3schools.com/python/python_getstarted.asp')")