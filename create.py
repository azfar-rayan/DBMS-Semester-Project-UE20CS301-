import streamlit as st
from database import add_farmer_data
from database import add_buyer_data


def create():
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
