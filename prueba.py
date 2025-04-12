from functions import main_page
import streamlit as st
import pandas as pd
import math

sheet_name = "Brochas"
df = pd.read_excel("LEIK - Catálogo Web.xlsx", sheet_name = sheet_name)

count_rows = len(df["Producto"].to_list())/4
print(count_rows)
