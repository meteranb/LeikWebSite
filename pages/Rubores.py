from functions import main_page
import streamlit as st
import pandas as pd

df = pd.read_excel("Inventario.xlsx", sheet_name = "Rubores")

for index, row in df.iterrows():
    st.header(row["Nombre del Producto"])
    st.image("images/" + row["Imagen"])
    st.write(row["Descripcion"])
    st.info(f"Precio: $ {row["Valor"]}")
    st.info(f"Disponibilidad: {row["Disponible"]}")

main_page()