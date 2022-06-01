import streamlit as st


OPERATIONS = {}


def display_sidebar_menu(portfolio_contr, file_handler):
    """display the sidebar with options and executes chosen one"""

    operation = st.sidebar.selectbox(
        label="Select an operation", options=OPERATIONS
    )

    if operation in OPERATIONS:
        OPERATIONS[operation](
            portfolio_contr=portfolio_contr, file_handler=file_handler
        )


def display_portfolio_page(portfolio_contr, file_handler):
    """display main portfolio management view"""

    st.markdown(f"## {portfolio_contr.portfolio_name}")
    display_sidebar_menu(portfolio_contr, file_handler)
