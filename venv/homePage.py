import streamlit as st
import yaml
import datetime
import data_page
import profiling
from PIL import Image

st.set_page_config(page_title="Configuration.yaml")

# Sidebar Navigation
image = Image.open(r'C:\Users\skurt\PycharmProjects\StreamlitProject\venv\share\Python_logo_and_wordmark.png')
st.sidebar.image(image, width=285)
options = st.sidebar.radio('',['Data','Profiling'])
if options == 'Data':
    data_page.data_page()
if options == 'Profiling':
    profiling.profiling()
