#!/bin/bash

python3 -m venv venv
source venv/bin/activate # Esto es para linux o mac el de windows debe tener las '\'

# Si no existen los requerimientos
pip install -r requirements.txt

# arrancar
streamlit run app.py

