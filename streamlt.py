import streamlit as st

input_num = st.number_input('値を入力して下さい！', value=0)

result = input_num * 2
st.write('結果: ', result)