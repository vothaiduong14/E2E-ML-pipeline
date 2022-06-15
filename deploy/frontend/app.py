import streamlit as st
import pandas as pd
import time
import io
import requests
from PIL import Image

# Util functions
@st.cache
def df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Backend endpoint
endpoint = "http://host.docker.internal:8080/predict"

# title and instruction
st.title("Identify potential customers to cross-sell")
st.markdown("""
    Upload your data and press predict to infer the outcome. Customers who have value 1 in column 'potential_buyer'
    are more likely to buy complementary products.
    """)

# interactive components
file_box = st.file_uploader("Upload a csv file", type=["csv"], accept_multiple_files=False)
predict_button = st.button("Get Prediction")

# processing
if predict_button:
    if file_box is not None:

        # load the file
        uploaded_df = pd.read_csv(file_box)
        st.subheader('Sample of the uploaded data')
        st.write(uploaded_df.head())

        # convert data for sending to backend
        bytes_obj = io.BytesIO()
        uploaded_df.to_csv(bytes_obj, index=False)
        bytes_obj.seek(0)

        files = {'file': ('uploaded_data.csv', bytes_obj, 'multipart/form-data')}
    
    else:
        st.text('Please upload a csv file containing required data')

    # handle error cases: empty, missing columns...

    with st.spinner("Finding potential buyers among uploaded customers. Please wait.."):
        output = requests.post(endpoint, files=files, timeout=100)
        csv = df_to_csv(pd.DataFrame(output))
        st.success("Done! Click on the button below to download the result.")
        st.download_button(label='Download', data= csv , file_name='result.csv', mime='text/csv')

     




    
