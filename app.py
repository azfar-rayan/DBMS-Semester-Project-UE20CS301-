import streamlit as st

from create import create
from delete import delete
from read import read
from update import update


def main():
    st.title("Farm Management Project _ PES1UG20CS453")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add":
        st.subheader("Add Entries To table")
        create()

    elif choice == "View":
        st.subheader("Read Entries From Table")
        read()

    elif choice == "Edit":
        st.subheader("Update Entries in Table")
        update()

    elif choice == "Remove":
        st.subheader("Delete Entries In table")
        delete()

    else:
        st.subheader("About")


if __name__ == '__main__':
    main()
