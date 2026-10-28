import streamlit as st
import pandas as pd
import numpy as np

random_data = np.random.randint(10,1000, 10)

st.write(random_data)

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

email = st.text_input("Email", type="email")
if email:
    st.write("We'll reach you at", email)
  
