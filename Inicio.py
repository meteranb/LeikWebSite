import pandas
import streamlit as st
import pandas as pd
from click.formatting import iter_rows

st.set_page_config(layout="wide")

empty1,col2,col3,empty2 = st.columns([2,1.5,2,2])

with col2:
    st.image("images/Leik Logo.jpg")

with col3:
    html_code = """
        <div style="text-align: center;">
            <h1>LEIK</h1>
            <h2>Naturalmente Bellas</h2>
            <body>Cuando el tiempo pasa y nos hacemos viejos, nos empieza a parecer
            que pensan mas los daños que los mismos años al final. Por eso yo quiero
            que mis años pasen junto a ti mi amor eterno, junto a mi familia, junto
            a mis amigos y mi voz</body>
        </div>
        """
    st.markdown(html_code, unsafe_allow_html=True)
st.title("")
col5, col6, empty3 =st.columns([0.4,3,5])

with col5:
    st.image("images/Leik Logo.jpg")
with col6:
    st.header("Nuestro Catalogo")

st.title("")

col7, col8, col9, col10 = st.columns(4)

with col7:
    button1 = st.button("Paletas", use_container_width=True)
    if button1:
        st.switch_page("pages/Paletas.py")

with col8:
    button2 = st.button("Labiales",use_container_width=True)
    if button2:
        st.switch_page("pages/Labiales.py")

with col9:
    button3 = st.button("Correctores",use_container_width=True)
    if button3:
        st.switch_page("pages/Correctores.py")

with col10:
    button4 = st.button("Rubores",use_container_width=True)
    if button4:
        st.switch_page("pages/Rubores.py")

st.title("")

empty4, col11, empty5 = st.columns([2,1,2])

with col11:
    contactus_button = st.button("Contactanos", use_container_width=True)
    if contactus_button:
        st.switch_page("pages/Contactanos.py")