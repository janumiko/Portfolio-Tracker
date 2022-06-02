import streamlit as st

from src.controllers.portfolio_controller import PortfolioController
from src.controllers.file_handler import FileHandler
from src.views.portfolio_menu import display_portfolio_page
from src.views.file_operations import (
    display_create_portfolio,
    display_upload_portfolio,
)

_DATA_PATH = "data/portfolios"


def load_main_page():
    """display main page of the site and load the portfolio files"""

    st.set_page_config(
        page_title="Portfolio Tracker",
        layout="wide",
        initial_sidebar_state="auto",
    )

    portfolio_handler = FileHandler(_DATA_PATH)
    if not portfolio_handler.data_path.exists():
        portfolio_handler.create_data_dir()

    portfolio_handler.load_portfolios()

    if len(portfolio_handler.portfolios) == 0:
        st.warning(
            """No portfolio has been found, upload one\
         or create a new one."""
        )
        display_create_portfolio(file_handler=portfolio_handler)
        display_upload_portfolio(file_handler=portfolio_handler)
    else:
        portfolios = portfolio_handler.portfolios
        chosen_portfolio_name = st.sidebar.selectbox(
            label="""Select a portfolio to open""", options=portfolios.keys()
        )

        p_path = portfolios[chosen_portfolio_name]
        portfolio = PortfolioController(p_path, chosen_portfolio_name)
        display_portfolio_page(portfolio, portfolio_handler)


if __name__ == "__main__":
    load_main_page()
