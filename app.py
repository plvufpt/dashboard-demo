import pandas as pd
import numpy as np
import vnstock
import matplotlib.pyplot as plt
import yfinance as yf
import investpy as ipy
import streamlit as st
import all_function as af



vcb = af.get_stock('VCB')
vnm = af.get_stock('VNM')
fpt = af.get_stock('FPT')
acb = af.get_stock('ACB')
hpg = af.get_stock('HPG')
bid = af.get_stock('BID')
mbb = af.get_stock('MBB')
mwg = af.get_stock('MWG')
nvl = af.get_stock('NVL')
vic = af.get_stock('VIC')

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

st.dataframe(multiple_stock)







