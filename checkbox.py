import streamlit as st

agree = st.checkbox('I agree')

if agree:
    market = st.text_input('Enter')
    submit1 = st.button("Submit")
    
    if submit1==True:
        st.write('Great!')
        print('HI')
        st.write("Entered Market is",market)

    