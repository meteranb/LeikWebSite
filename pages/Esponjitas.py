from functions import main_page
import streamlit as st
import pandas as pd

sheet_name = "Esponjitas"
df = pd.read_excel("LEIK - Catálogo Web.xlsx", sheet_name = sheet_name)

for index, row in df.iterrows():
    st.header(row["Producto"])
    st.image("images/" + row["Imagen 1"])
    st.write(row["Descripción"])
    if row["Disponibilidad"] == "Si":
        if row["Oferta"] == "Si":
            st.info(f"COP {int(row["Precio con Descuento"])}")
        else:
            st.info(f"COP {int(row["Precio"])}")
    else:
        st.info("No Disponible")
main_page()