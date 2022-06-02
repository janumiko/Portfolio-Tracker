import streamlit as st
import json
import matplotlib.pyplot as plt

from typing import Dict, List


def draw_pie_chart(codes: List, values: List) -> None:
    fig1, ax1 = plt.figure(), plt.axes()

    ax1.pie(
        codes,
        labels=values,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax1.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)


def display_currencies(currencies: Dict) -> None:
    st.markdown("## Currencies")

    positive_currencies_values = []
    positive_currencies_codes = []

    for c in currencies:
        st.markdown(f"{c} : {currencies[c] / 100}")

        if currencies[c] > 0:
            positive_currencies_values.append(currencies[c] / 100)
            positive_currencies_codes.append(c)

    if len(positive_currencies_values) > 0:
        draw_pie_chart(positive_currencies_values, positive_currencies_codes)


def display_assets(assets: Dict) -> None:
    st.markdown("## Assets")
    for asset in assets:
        unit_price = assets[asset]["unit_price"] / 100
        currency = assets[asset]["currency"]
        amount = assets[asset]["amount"]

        st.markdown(f"{amount} {asset}: {unit_price} {currency} per {asset}")


def display_portfolio_assets(**kwargs) -> None:
    """display assets from portfolio given in argument"""

    portfolio_contr = kwargs["portfolio_contr"]
    try:
        assets = portfolio_contr.portfolio_assets
    except json.JSONDecodeError:
        st.error("Couldn't load file!")
    display_assets(assets)


def display_portfolio_currencies(**kwargs) -> None:
    """display assets from portfolio given in argument"""

    portfolio_contr = kwargs["portfolio_contr"]
    try:
        currencies = portfolio_contr.portfolio_currencies
    except json.JSONDecodeError:
        st.error("Couldn't load file!")
    display_currencies(currencies)


def display_transaction_history(**kwargs):
    """display transaction history from portfolio"""

    portfolio_contr = kwargs["portfolio_contr"]
    try:
        transactions = portfolio_contr.portfolio_transactions
    except json.JSONDecodeError:
        st.error("Couldn't load file!")

    st.markdown("### Transaction records")
    st.markdown("Type, Date, Ticker, amount, unit price, currency")

    for t in reversed(transactions):
        date = t["date"]
        transaction_type = t["type"]
        code = t["code"]
        unit_price = t["unit_price"] / 100
        amount = t["amount"]
        currency = t["currency"]

        st.markdown(
            f"{transaction_type},{date},{code},"
            + f"{amount},{unit_price},{currency}"
        )
