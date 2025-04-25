import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('streamlit app')
    st.header('This is streamlit User Interface')
    st.write('welcome to our streamlit app 🎉')
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
    # This section generates a random numpy array with shape (10, 20) and displays it as a dataframe in the Streamlit app.
    dataframe = pd.DataFrame(np.random.randn(10,20))
    st.dataframe(dataframe)
app()