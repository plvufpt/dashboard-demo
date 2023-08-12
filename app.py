import pandas as pd
import numpy as np
import vnstock
import matplotlib.pyplot as plt
import yfinance as yf
import investpy as ipy
import streamlit as st
import all_function as af
# Call function get stocks
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
# Concat Close price stocks
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
# Rename stocks
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
# Drop Value NaN
multiple_stock.dropna(inplace=True)
# Set index columns Date
multiple_stock.set_index('Date', inplace=True)
# Write datframe mutiple price stocks 
st.dataframe(multiple_stock)

st.header("Estimating Portfolio Risk Multiple Assets")
st.subheader("Daily return")
# First, We need to do is to calculate daily returns
# về công thức gốc thì giá trị ret = (giá ngày hôm nay - giá ngày trước đó) - 1
multiple_stocks_ret = multiple_stock.pct_change(1)
st.write(multiple_stocks_ret)
st.subheader("Calculate Risk Portfolio")
# Second, We need to do is to calculate risk portfolio so we need 2 thing:
  #vector of weight Omega
  #variance covariance matrix or sigma
#vector of weight Omega
# number_stock bằng 10 vì chia đều cho 10 mã cổ phiếu
number_stock = 10
weight = [1 / number_stock] * number_stock
weight
st.subheader("Variance Covariance Matrix")
#variance covariance matrix or sigma
# này là tính mối liên hệ giữa các cổ phiếu với nhau
vcv_matrix = multiple_stocks_ret.cov()
st.write(vcv_matrix)
st.subheader("Variance Portfolio")
#tính variance portfolio
var_p = np.dot(np.transpose(weight), np.dot(vcv_matrix, weight))
st.write("var_p")
st.subheader("STD of Portfolio")
#tính std của portfolio = căn bậc 2 của variance portfolio
std_p = np.sqrt(var_p)
st.write("std_p")
st.subheader("STD Portfolio Annual")
#tuy nhiên std_p hiện tại đang tính là daily và nếu mình muốn tính annual thì nhân nó cho căn bậc 2 của 250 trong đó 250 là số ngầy gd của 1 năm
std_p_annual = std_p * np.sqrt(250)
st.write("std_p_annual")
# tuy nhiên mục đích chúng ta tạo ra danh mục này chính là compare các danh mục đầu tư rủi ro này với rủi ro cá nhân
# để tính rủi ro từng danh mục ta lấy độ lệch chuẩn của 'multiple_stocks_ret' các cổ phiếu hàng ngày. Tuy nhiên chúng tôi muốn tính std của hàng năm vì thế tôi nhân cho căn bậc 2 của 250
st.subheader("individual_risks")
individual_risks = np.std(returns_df) * np.sqrt(250)
st.write("individual_risks")



