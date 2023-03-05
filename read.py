import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Farmer ID','Farmer Name','Username','Passcode','Email','Mobile No','Address Info'])
    with st.expander("View all Farmers"):
        st.dataframe(df)