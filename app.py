import streamlit as st
from groq import Groq

st.title("Gen-AI: Festival Sales Predictor")
st.write("MSMEs ke liye Groq Llama3 powered AI tool")

product = st.text_input("Product ka naam daalo:")
month = st.selectbox("Mahina chuno:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
festival = st.text_input("Koi festival ya event?")

if st.button("Sales Predict Karo"):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    prompt = f"Mere product '{product}' ki sales {month} mein, {festival} ke time pe kitni hogi? MSME ke liye 3 point mein batao."
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )
    
    result = response.choices[0].message.content
    st.write(result)
