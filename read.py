import pandas as pd
import streamlit as st
from database import view_table


def read():
    list_of_tables=['FARMER','BUYER','FPRODUCT']
    choice=st.selectbox("Select Table to View Data", list_of_tables)

    if choice == "FARMER":
        st.text("Displaying Farmer table")
        res=view_table('farmer')
        df = pd.DataFrame(res, columns=['Farmer ID', 'Farmer Name', 'Username', 'Password', 'Farmer Email', 'Mobile No.', 'Address Info.'])
        st.dataframe(df)
        st.success("Successfully fetched Farmer table")

    elif choice == "BUYER":
        st.text("Displaying Buyer table")
        res=view_table('buyer')
        df = pd.DataFrame(res, columns=['Buyer ID', 'Buyer Name', 'Username', 'Password', 'Buyer Email', 'Mobile No.', 'Address Info.'])
        st.dataframe(df)
        st.success("Successfully fetched Buyer table")

    elif choice == "FPRODUCT":
        st.text("Displaying Fproduct table")
        res=view_table('fproduct')
        df = pd.DataFrame(res, columns=['Farmer ID', 'Product ID', 'Name', 'Category', 'Prod. Info', 'Price'])
        st.dataframe(df)
        st.success("Successfully fetched Fproduct table")        

    else:
        st.subheader("About Read")
    