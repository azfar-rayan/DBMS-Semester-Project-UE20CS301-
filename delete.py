import pandas as pd
import streamlit as st
from database import view_table
from database import view_fids,delete_farmer_data
from database import view_bids,delete_buyer_data
from database import view_pids,delete_product_data

def delete():
    list_of_tables=['FARMER','BUYER','FPRODUCT']
    choice=st.selectbox("Select Table to View Data", list_of_tables)

    if choice == "FARMER":
        result = view_table('farmer')
        df = pd.DataFrame(result, columns=['FID', 'Fname', 'Username', 'Fpassword', 'Femail', 'Fmobile', 'Faddress'])
        with st.expander("Current data in Farmer Table"):
            st.dataframe(df)
        
        F_ids = [i[0] for i in view_fids()]
        selected_fid = st.selectbox("Select Farmer ID", F_ids)
        st.warning("Do you want to Delete Farmer with ID:: {} ".format(selected_fid))
        if st.button("Delete Farmer"):
            delete_farmer_data(selected_fid)
            st.success("Farmer has been deleted successfully")
        
        new_result = view_table('farmer')
        df2 = pd.DataFrame(new_result, columns=['FID', 'Fname', 'Username', 'Fpassword', 'Femail', 'Fmobile', 'Faddress'])
        with st.expander("Updated data is:"):
            st.dataframe(df2)

    elif choice == "BUYER":
        result = view_table('buyer')
        df = pd.DataFrame(result, columns=['BID', 'Buyer Name', 'Username', 'Password', 'Buyer Email', 'Buyer Mobile', 'Address'])
        with st.expander("Current data in Buyer Table"):
            st.dataframe(df)
        
        B_ids = [i[0] for i in view_bids()]
        selected_bid = st.selectbox("Select Buyer ID", B_ids)
        st.warning("Do you want to Delete Buyer with ID:: {} ".format(selected_bid))
        if st.button("Delete Buyer"):
            delete_buyer_data(selected_bid)
            st.success("Buyer has been deleted successfully")
        
        new_result = view_table('buyer')
        df2 = pd.DataFrame(new_result, columns=['BID', 'Buyer Name', 'Username', 'Password', 'Buyer Email', 'Buyer Mobile', 'Address'])
        with st.expander("Updated buyer data is:"):
            st.dataframe(df2)

    elif choice == "FPRODUCT":
        result = view_table('fproduct')
        df = pd.DataFrame(result, columns=['FID', 'PID', 'Product Name', 'Category', 'Product Info', 'Product Price'])
        with st.expander("Current data in Product Table"):
            st.dataframe(df)
        
        P_ids = [i[0] for i in view_pids()]
        selected_pid = st.selectbox("Select Buyer ID", P_ids)
        st.warning("Do you want to Delete Product with ID:: {} ".format(selected_pid))
        if st.button("Delete Product"):
            delete_product_data(selected_pid)
            st.success("Product has been deleted successfully")
        
        new_result = view_table('fproduct')
        df2 = pd.DataFrame(new_result, columns=['FID', 'PID', 'Product Name', 'Category', 'Product Info', 'Product Price'])
        with st.expander("Updated product data is:"):
            st.dataframe(df2)
    else:
        st.subheader("About Delete")
    