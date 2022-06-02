import streamlit as st

from json import JSONDecodeError


def display_create_portfolio(**kwargs):
    """display page with creation option,
    rerun site if new portfolio is created"""

    file_handler = kwargs["file_handler"]
    with st.form(key="Create portfolio", clear_on_submit=True):
        name = st.text_input("Type new portfolio name:")

        if st.form_submit_button("Create new portfolio"):
            try:
                file_handler.create_empty_portfolio(name)
                st.success("Created portfolio!")
                st.experimental_rerun()
            except (FileExistsError, FileNotFoundError, ValueError) as e:
                st.error(e)


def display_download_portfolio(**kwargs):
    """display download button for downloading portfolio"""

    file_handler = kwargs["file_handler"]
    name = kwargs["portfolio_contr"].portfolio_name

    try:
        portfolio_path = file_handler.get_portfolio_path(name)
    except FileNotFoundError as e:
        st.error(e)

    with open(portfolio_path, "r") as file:
        st.download_button(
            label="Download portfolio",
            data=file,
            file_name=f"{name}.json",
            mime="application/json",
        )


def display_upload_portfolio(**kwargs):
    """display widgets for uploading portfolio"""

    file_handler = kwargs["file_handler"]
    with st.form(key="Upload portfolio", clear_on_submit=True):
        name = st.text_input("Portfolio name")
        uploaded_portfolio = st.file_uploader(
            label="Upload portfolio in json format",
            type=["json"],
            accept_multiple_files=False,
        )

        if st.form_submit_button("Upload"):
            try:
                file_handler.upload_portfolio(name, uploaded_portfolio)
                st.experimental_rerun()
            except (
                JSONDecodeError,
                FileNotFoundError,
                ValueError,
            ) as e:
                st.error("Invalid file!")
                st.error(e)
            except FileExistsError as e:
                st.error(e)


def display_remove_portfolio(**kwargs):
    """display form for removing portfolio"""

    file_handler = kwargs["file_handler"]
    with st.form(key="Remove portfolio", clear_on_submit=True):
        name = st.text_input("Type portfolio name to be removed:")

        if st.form_submit_button("Remove portfolio"):
            try:
                file_handler.remove_portfolio(name)
                st.success("Removed portfolio!")
                st.experimental_rerun()
            except (FileNotFoundError, ValueError) as e:
                st.error(e)
