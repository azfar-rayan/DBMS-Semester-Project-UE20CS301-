
import pandas as pd
import streamlit as st
from database import view_table
from database import view_fids,view_bids, view_pids
from database import get_farmer,get_buyer,get_product
from database import edit_farmer_data,edit_buyer_data, edit_fproduct_data


def update():
    list_of_tables=['FARMER','BUYER','FPRODUCT']
    choice=st.selectbox("Select Table to Update Data", list_of_tables)

    if choice == "FARMER":
        result = view_table('farmer')
        df = pd.DataFrame(result, columns=['FID', 'Fname', 'Username', 'Fpassword', 'Femail', 'Fmobile', 'Faddress'])
        with st.expander("Current data in Farmer Table"):
            st.dataframe(df)

        F_ids = [i[0] for i in view_fids()]
        selected_fid = st.selectbox("Select Farmer ID", F_ids)
        selected_result = get_farmer(selected_fid)
        if selected_result:
            fid = selected_result[0][0]
            fname = selected_result[0][1]
            fusername = selected_result[0][2]
            fpassword = selected_result[0][3]
            femail = selected_result[0][4]
            fmobile = selected_result[0][5]
            faddress = selected_result[0][6]

        col1,col2 = st.columns(2)
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
            st.success("Successfully Updated Farmer with ID : {} ".format(new_fid))

        result2 = view_table('farmer')
        df2 = pd.DataFrame(result2, columns=['Farmer ID', 'Farmer Name', 'Username', 'Password', 'Email ID', 'Mobile No.', 'Address Info'])
        with st.expander("Updated Farmer data"):
            st.dataframe(df2)
    
    elif choice == "BUYER":
        result = view_table('buyer')
        df = pd.DataFrame(result, columns=['Buyer ID','Buyer Name','Buyer Username','Passcode','Email','Buyer Mobile ','Buyer Address Info'])
        with st.expander("Current data in Buyer Table"):
            st.dataframe(df)

        B_ids = [i[0] for i in view_bids()]
        selected_bid = st.selectbox("Select buyer ID", B_ids)
        selected_result = get_buyer(selected_bid)
        if selected_result:
            bid = selected_result[0][0]
            bname = selected_result[0][1]
            busername = selected_result[0][2]
            bpassword = selected_result[0][3]
            bemail = selected_result[0][4]
            bmobile = selected_result[0][5]
            baddress = selected_result[0][6]

        col1, col2 = st.columns(2)
        with col1:
            new_bid = st.text_input("buyer ID:",bid)
            new_bname = st.text_input("buyer's Name: ",bname)
            new_busername = st.text_input("Username",busername)
            new_bpassword = st.text_input("Password: ", bpassword)
        with col2:
            new_bemail = st.text_input("Email ID:",bemail)
            new_bmobile = st.text_input("Mobile No. :",bmobile)
            new_baddress = st.text_input("Address Info:",baddress)
        if st.button("Update buyer Details"):
            edit_buyer_data(new_bid, new_bname, new_busername, new_bpassword, new_bemail, new_bmobile, new_baddress, bid, bname, busername, bpassword, bemail, bmobile, baddress)
            st.success("Successfully Updated Buyer with ID : {} ".format(new_bid))

        result2 = view_table('buyer')
        df2 = pd.DataFrame(result2, columns=['Buyer ID','Buyer Name','Buyer Username','Passcode','Email','Buyer Mobile ','Buyer Address Info'])
        with st.expander("Updated Buyer Data"):
            st.dataframe(df2)
    
    elif choice == "FPRODUCT":
        result = view_table('fproduct')
        df = pd.DataFrame(result, columns=['FID', 'PID', 'Product Name', 'Category', 'Product Info', 'Product Price'])
        with st.expander("Current data in Products Table"):
            st.dataframe(df)

        P_ids = [i[0] for i in view_pids()]
        selected_pid = st.selectbox("Select product ID", P_ids)
        selected_result = get_product(selected_pid)
        if selected_result:
            fid = selected_result[0][0]
            pid = selected_result[0][1]
            product = selected_result[0][2]
            pcat = selected_result[0][3]
            pinfo = selected_result[0][4]
            price = selected_result[0][5]

        col1, col2 = st.columns(2)
        with col1:
            new_fid = st.text_input("Farmer ID:",fid)
            new_pid = st.text_input("Product ID: ",pid)
            new_product = st.text_input("Product Name",product)
        with col2:
            new_pcat = st.text_input("Category:",pcat)
            new_pinfo = st.text_input("Product Info",pinfo)
            new_price = st.text_input("Price",price)
        if st.button("Update Product"):
            edit_fproduct_data(new_fid, new_pid, new_product, new_pcat, new_pinfo, new_price,fid, pid, product, pcat, pinfo, price)
            st.success("Successfully Updated Product with ID : {} ".format(new_pid))

        result2 = view_table('fproduct')
        df2 = pd.DataFrame(result2, columns=['FID', 'PID', 'Product Name', 'Category', 'Product Info', 'Product Price'])
        with st.expander("Updated Product Data"):
            st.dataframe(df2)
