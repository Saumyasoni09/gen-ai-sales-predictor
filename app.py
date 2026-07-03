import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Gen-AI Sales Predictor", page_icon="🎯")

st.title("🎯 Gen-AI: Festival Sales Predictor")
st.subheader("MSMEs ke liye Gemini 2.5 Flash powered AI tool")

# API Key Streamlit Secrets se lega
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

product = st.text_input("Product ka naam daalo:", "Diya")
month = st.selectbox("Mahina chuno:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
festival = st.text_input("Koi festival ya event?", "Diwali")

if st.button("Sales Predict Karo 🚀"):
    with st.spinner("Gemini soch raha hai..."):
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = f"Act as a sales expert for India. Predict sales for {product} in {month} considering {festival}. Give insights in Hinglish for Indian MSMEs. Keep it short."
            response = model.generate_content(prompt)
            st.success("Prediction aa gayi!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")