import pandas
import streamlit as st
import pandas as pd
from click.formatting import iter_rows
import math
from PIL import Image

def main_page():
        st.page_link("1-Inicio.py", label = "Volver al inicio")

def structure(sheet_name):

        df = pd.read_excel("LEIK - Catálogo Web.xlsx", sheet_name=sheet_name)

        limit = len(df["Producto"].to_list())/4
        n = math.ceil(limit)

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            for index, row in df[:n].iterrows():
                st.write(row["Producto"])
                st.image("images/" + row["Imagen 1"], width=120)
                if row["Disponibilidad"] == "Si":
                    if row["Oferta"] == "Si":
                        st.info(f"COP {int(row["Precio con Descuento"])}")
                    else:
                        st.info(f"COP {int(row["Precio"])}")
                else:
                    st.info("No Disponible")

        with col2:
            for index, row in df[n:(2*n)].iterrows():
                st.write(row["Producto"])
                st.image("images/" + row["Imagen 1"], width=120)
                if row["Disponibilidad"] == "Si":
                    if row["Oferta"] == "Si":
                        st.info(f"COP {int(row["Precio con Descuento"])}")
                    else:
                        st.info(f"COP {int(row["Precio"])}")
                else:
                    st.info("No Disponible")

        with col3:
            for index, row in df[(2*n):(3*n)].iterrows():
                st.write(row["Producto"])
                st.image("images/" + row["Imagen 1"], width=120)
                if row["Disponibilidad"] == "Si":
                    if row["Oferta"] == "Si":
                        st.info(f"COP {int(row["Precio con Descuento"])}")
                    else:
                        st.info(f"COP {int(row["Precio"])}")
                else:
                    st.info("No Disponible")

        with col4:
            for index, row in df[(3*n):].iterrows():
                st.write(row["Producto"])
                st.image("images/" + row["Imagen 1"], width=120)
                if row["Disponibilidad"] == "Si":
                    if row["Oferta"] == "Si":
                        st.info(f"COP {int(row["Precio con Descuento"])}")
                    else:
                        st.info(f"COP {int(row["Precio"])}")
                else:
                    st.info("No Disponible")