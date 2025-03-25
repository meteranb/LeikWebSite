import pandas
import streamlit as st
import pandas as pd
from click.formatting import iter_rows

st.set_page_config(layout="wide")

col1,col2,col3,col4,col5,col6 = st.columns([1,1,1.5,2,1,1])

with col3:
    st.image("images/Leik Logo.jpg")

with col4:
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
col7, col8, col9 =st.columns([0.4,3,5])

with col7:
    st.image("images/Leik Logo.jpg")
with col8:
    st.header("Nuestro Catalogo")

st.title("")

col11, col12, col13, col14 = st.columns(4)

with col11:
    button1 = st.button("Paletas",use_container_width=True)

with col12:
    button2 = st.button("Labiales",use_container_width=True)

with col13:
    button3 = st.button("Correctores",use_container_width=True)

with col14:
    button4 = st.button("Rubores",use_container_width=True)