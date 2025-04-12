from functions import main_page, structure
import streamlit as st
import pandas as pd
import math

st.set_page_config(layout="wide")
sheet_name = "Delineadores"
structure(sheet_name)
main_page()