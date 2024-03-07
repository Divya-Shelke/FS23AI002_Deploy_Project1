import streamlit as st
email = st.text_input('Enter your email')
password = st.number_input('Enter your password')
btn = st.button('Login')
if btn:
    if email  == 'amangupta@gmail.com' and password == 12345:
        st.balloons()
    else:
        st.error('Invalid input')