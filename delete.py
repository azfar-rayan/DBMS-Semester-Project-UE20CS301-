import pandas as pd
import streamlit as st
from database import view_all_data, view_only_farmer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Farmer ID','Farmer Name','Username','Passcode','Email','Mobile No','Address Info'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_farmers = [i[0] for i in view_only_farmer_names()]
    selected_farmer = st.selectbox("Task to Delete", list_of_farmers)
    st.warning("Do you want to delete ::{}".format(selected_farmer))
    if st.button("Delete Farmer"):
        delete_data(selected_farmer)
        st.success("The given farmer has been removed successfully !")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Farmer ID','Farmer Name','Username','Passcode','Email','Mobile No','Address Info'])
    with st.expander("The new & updated data is :"):
        st.dataframe(df2)