import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta

cg = CoinGeckoAPI()

st.write("# FOMO kalkulator")

price_now = cg.get_price(ids="dogecoin", vs_currencies="usd")["dogecoin"]["usd"]

st.write("Velg Dato, og Beløp")

todays_date = datetime.utcnow().date()
hist_date = st.date_input("Date:")
initial_amount = st.number_input("Beløp")
HIST_DATE_REFORMAT = hist_date.strftime("%d-%m-%Y")

doge_historic = cg.get_coin_history_by_id(id="dogecoin", vs_currencies="usd", date=HIST_DATE_REFORMAT)['market_data']['current_price']['usd']

st.write("Historical FOMO Analysis")
total = initial_amount/doge_historic
value_now = total * price_now

st.write("Your dogecoin are worth:", value_now)

change_percent = ((value_now - initial_amount)/(initial_amount)) * 100
st.write("The change in percent is:", change_percent)
