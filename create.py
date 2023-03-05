import pandas as pd
import streamlit as st
from database import view_table
from database import add_farmer_data,add_buyer_data,add_fproduct_data


def create():
    list_of_tables=['FARMER','BUYER','FPRODUCT']
    choice=st.selectbox("Select Table to View Data", list_of_tables)

    if choice == "FARMER":
        result = view_table('farmer')
        df = pd.DataFrame(result, columns=['FID', 'Fname', 'Username', 'Fpassword', 'Femail', 'Fmobile', 'Faddress'])
        with st.expander("Current data in Farmer Table"):
            st.dataframe(df)

        st.text("Insert To Farmer table")
        col1, col2 = st.columns(2)
        with col1:
            fid = st.text_input("Farmer ID")
            fname = st.text_input("Name")
            fusername = st.text_input("Username")
            fpassword = st.text_input("Passcode")

        with col2:
            femail = st.text_input("Email")
            fmobile = st.text_input("Mobile No")
            faddress = st.text_input("Address Info")
            
        if st.button("Add Farmer"):
            add_farmer_data(fid, fname, fusername, fpassword, femail, fmobile, faddress)
            st.success("Successfully added Farmer: {}".format(fname))

    elif choice == "BUYER":
        result = view_table('buyer')
        df = pd.DataFrame(result, columns=['BID', 'Buyer Name', 'Username', 'Password', 'Buyer Email', 'Buyer Mobile', 'Address'])
        with st.expander("Current data in Buyer Table"):
            st.dataframe(df)

        st.text("Insert into Buyer table")
        col1, col2 = st.columns(2)
        with col1:
            bid = st.text_input("Buyer ID")
            bname = st.text_input("Buyer Name")
            busername = st.text_input("Buyer Username")
            bpassword = st.text_input("Passcode")

        with col2:
            bemail = st.text_input("Email")
            bmobile = st.text_input("Buyer Mobile No")
            baddress = st.text_input("Address Info")
            
        if st.button("Add buyer"):
            add_buyer_data(bid, bname, busername, bpassword, bemail, bmobile, baddress)
            st.success("Successfully added buyer: {}".format(bname))

        
    elif choice == "FPRODUCT":
        result = view_table('fproduct')
        df = pd.DataFrame(result, columns=['FID', 'PID', 'Product Name', 'Category', 'Product Info', 'Product Price'])
        with st.expander("Current data in Product Table"):
            st.dataframe(df)

        st.text("Insert to Fproduct table")
        col1, col2 = st.columns(2)
        with col1:
            fid = st.text_input("Buyer ID")
            product = st.text_input("Buyer Name")
            pinfo  = st.text_input("Buyer Username")

        with col2:
            pid = st.text_input("Email")
            pcat = st.text_input("Buyer Mobile No")
            price = st.text_input("Address Info")
            
        if st.button("Add farm product"):
            add_fproduct_data(fid, pid, product, pcat, pinfo, price)
            st.success("Successfully added ptoduct: {}".format(product))

    else:
        st.subheader("About Insert")