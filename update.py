import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_farmer_names, get_farmer, edit_farmer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Farmer ID','Farmer Name','Username','Passcode','Email','Mobile No','Address Info'])
    with st.expander("Current Registered Farmers"):
        st.dataframe(df)
    list_of_farmers = [i[0] for i in view_only_farmer_names()]
    selected_farmer = st.selectbox("Train to Edit", list_of_farmers)
    selected_result = get_farmer(selected_farmer)
    # st.write(selected_result)
    if selected_result:
        fid = selected_result[0][0]
        fname = selected_result[0][1]
        fusername = selected_result[0][2]
        fpassword = selected_result[0][3]
        femail = selected_result[0][4]
        fmobile = selected_result[0][5]
        faddress = selected_result[0][6]

        col1, col2 = st.columns(2)
        with col1:
            new_fid = st.text_input("Farmer ID:",fid)
            new_fname = st.text_input("Farmer's Name: ",fname)
            new_fusername = st.text_input("Username",fusername)
            new_fpassword = st.text_input("Password: ", fpassword)
        with col2:
            new_femail = st.text_input("Email ID:",femail)
            new_fmobile = st.text_input("Mobile No. :",fmobile)
            new_faddress = st.text_input("Address Info:",faddress)
        if st.button("Update Farmer Details"):
            edit_farmer_data(new_fid, new_fname, new_fusername, new_fpassword, new_femail, new_fmobile, new_faddress,fid, fname, fusername, fpassword, femail, fmobile, faddress)
            st.success("Successfully updated:: {} to ::{}".format(faddress, new_faddress))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Farmer ID', 'Farmer Name', 'Username', 'Password', 'Email ID', 'Mobile No.', 'Address Info'])
    with st.expander("Updated Data"):
        st.dataframe(df2)
