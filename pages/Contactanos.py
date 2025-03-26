from functions import main_page
import streamlit as st
from sendemail import send_email
st.header("Contactanos")

with st.form(key="email_forms"):
    user_email = st.text_input("Tu direccion de correo electronico")
    raw_message = st.text_area("Escribe tu requerimiento")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}"""

    button = st.form_submit_button("Enviar")
    if button:
        send_email(message, )
        st.info("Your email was sent successfully")

main_page()