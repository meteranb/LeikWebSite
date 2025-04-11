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
    button1 = st.button("Bases", use_container_width=True)
    if button1:
        st.switch_page("pages/2-Bases.py")
    button2 = st.button("Brochas", use_container_width=True)
    if button2:
        st.switch_page("pages/3-Brochas.py")
    button3 = st.button("Corporales", use_container_width=True)
    if button3:
        st.switch_page("pages/4-Corporales.py")

with col8:
    button4 = st.button("Delineadores", use_container_width=True)
    if button4:
        st.switch_page("pages/6-Delineadores.py")
    button5 = st.button("Esponjitas", use_container_width=True)
    if button5:
        st.switch_page("pages/7-Esponjitas.py")
    button6 = st.button("Labiales", use_container_width=True)
    if button6:
        st.switch_page("pages/8-Labiales.py")
    button7 = st.button("Correctores", use_container_width=True)
    if button7:
        st.switch_page("pages/5-Correctores.py")

with col9:
    button8 = st.button("Paletas", use_container_width=True)
    if button8:
        st.switch_page("pages/9-Paletas.py")
    button9 = st.button("Pestañinas", use_container_width=True)
    if button9:
        st.switch_page("pages/10-Pestañinas.py")
    button10 = st.button("Polvos", use_container_width=True)
    if button10:
        st.switch_page("pages/11-Polvos.py")
    button11 = st.button("Otros", use_container_width=True)
    if button11:
        st.switch_page("pages/15-Otros.py")

with col10:
    button12 = st.button("Primer", use_container_width=True)
    if button12:
        st.switch_page("pages/12-Primer.py")
    button13 = st.button("Rubores", use_container_width=True)
    if button13:
        st.switch_page("pages/13-Rubores.py")
    button14 = st.button("Sombras", use_container_width=True)
    if button14:
        st.switch_page("pages/14-Sombras.py")

st.title("")

empty4, col11, empty5 = st.columns([2,1,2])

with col11:
    contactus_button = st.button("Contactanos", use_container_width=True)
    if contactus_button:
        st.switch_page("pages/16-Contactanos.py")