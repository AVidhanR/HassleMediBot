import streamlit as st
import requests

st.title("Hassle Medi Bot")

with st.form(key='hassle_medi_bot_form'):
    question = st.text_input("Enter data:", placeholder="Enter your question here", max_chars=200, type="default")
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    url = 'http://localhost:5000/post-prompt'
    data = {'question': question}
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            json_response = response.json()
            st.write("Response from server:", json_response["response"])
            st.write("You asked:", json_response["question"])
        else:
            st.write(f"Error: {response.json()}", response.status_code)
    except Exception as e:
        st.write("An error occurred:", e)
