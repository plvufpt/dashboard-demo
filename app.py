import pandas as pd
import numpy as np
import vnstock
import matplotlib.pyplot as plt
import yfinance as yf
import investpy as ipy
import streamlit as st

def get_stock(stock):
  stock = vnstock.stock_historical_data(stock,'2018-01-01', '2023-01-01')
  stock.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol', 'Ticker']
  stock['Date'] = pd.to_datetime(stock['Date'])
  stock.sort_values('Date', ascending=True, inplace=True)
  return stock

vcb = get_stock('VCB')
vnm = get_stock('VNM')
fpt = get_stock('FPT')
acb = get_stock('ACB')
hpg = get_stock('HPG')
bid = get_stock('BID')
mbb = get_stock('MBB')
mwg = get_stock('MWG')
nvl = get_stock('NVL')
vic = get_stock('VIC')

multiple_stock = pd.concat([vic['Date'],
                       vcb['Close'],
                       vnm['Close'],
                       fpt['Close'],
                       acb['Close'],
                       hpg['Close'],
                       bid['Close'],
                       mbb['Close'],
                       mwg['Close'],
                       nvl['Close'],
                       vic['Close']
                       ], axis=1)

new_name = ['Date',
            'Close_VCB',
            'Close_VNM',
            'Close_FPT',
            'Close_ACB',
            'Close_HPG',
            'Close_BID',
            'Close_MBB',
            'Close_MWG',
            'Close_NVL',
            'Close_VIC']
multiple_stock.columns = new_name

multiple_stock.dropna(inplace=True)
multiple_stock.set_index('Date', inplace=True)

st.dataframe(multiple_stock, width="100%")







