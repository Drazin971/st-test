import streamlit as st

st.title("Streamlit on Replit")

text = """

- More information on streamlit [here](https://docs.streamlit.io/)

"""

st.write(text)

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')