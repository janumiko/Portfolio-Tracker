import streamlit as st

from src.views.assets_operations import (
    display_add_asset,
    display_add_currency,
    display_buy_asset,
    display_remove_asset,
    display_remove_currency,
    display_sell_asset,
)

from src.views.display_data import (
    display_portfolio_assets,
    display_portfolio_currencies,
    display_transaction_history,
)
from src.views.file_operations import (
    display_create_portfolio,
    display_download_portfolio,
    display_remove_portfolio,
    display_upload_portfolio,
)


OPERATIONS = {
    "Display assets": display_portfolio_assets,
    "Display currencies": display_portfolio_currencies,
    "Show transaction history": display_transaction_history,
    "Buy asset": display_buy_asset,
    "Sell asset": display_sell_asset,
    "Add currency": display_add_currency,
    "Remove currency": display_remove_currency,
    "Add asset": display_add_asset,
    "Remove asset": display_remove_asset,
    "Download portfolio": display_download_portfolio,
    "Create new portfolio": display_create_portfolio,
    "Upload portfolio": display_upload_portfolio,
    "Remove portfolio": display_remove_portfolio,
}


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
