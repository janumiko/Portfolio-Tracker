import streamlit as st


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
