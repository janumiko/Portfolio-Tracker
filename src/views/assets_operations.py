import streamlit as st


def display_add_asset(**kwargs):
    """Display form to add an asset"""

    portfolio_contr = kwargs["portfolio_contr"]
    with st.form(key="add_asset"):
        code = st.text_input(
            label="Input asset code:", key="code", max_chars=8
        )

        amount = st.number_input(
            label="Input amount of assets to add:",
            key="amount",
            min_value=0,
            max_value=10**12,
            step=1,
        )

        unit_price = int(
            st.number_input(
                label="Input unit price:",
                key="unit_price",
                min_value=0.0,
                max_value=1e16,
                format="%.2f",
            )
            * 100
        )
        currency = st.text_input(label="Input currency:", key="currency")

        if st.form_submit_button("Add asset"):
            try:
                portfolio_contr.add_asset(
                    code=code,
                    amount=amount,
                    unit_price=unit_price,
                    currency=currency,
                )
                portfolio_contr._save_file_data()
                st.success("Added asset")
            except (FileExistsError, FileNotFoundError, ValueError) as e:
                st.error(e)


def display_remove_asset(**kwargs):
    """display widgets for removing asset from portfolio"""

    portfolio_contr = kwargs["portfolio_contr"]
    with st.form(key="remove_asset"):
        code = st.text_input(
            label="Input asset code:", key="code", max_chars=6
        )

        amount = st.number_input(
            label="Input amount of assets to remove:",
            key="amount",
            min_value=0,
            max_value=10**12,
            step=1,
        )

        if st.form_submit_button("Remove asset"):
            try:
                portfolio_contr.remove_asset(code, amount)
                portfolio_contr._save_file_data()
                st.success("Removed asset")
            except (FileExistsError, FileNotFoundError, ValueError) as e:
                st.error(e)
