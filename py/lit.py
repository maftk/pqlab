import set_data
from sqlalchemy import text
from db import engine
import pandas as pd
import fetch_data as fd
import plots as pt
import streamlit as st

st.set_page_config(layout='wide')

# 初期パラメータ
default_start_date = '2020-01-16'
default_end_date = '2023-05-08'

pref_names_list = fd.fetch_pref_names()
default_pref_names = ('東京都', '沖縄県', '山口県')

# レイアウトの設定
# chart_col, control_col = st.columns([3, 1])

# コントロールパネル
# with control_col:
with st.expander('Edit chart', expanded=True):
    start_date = st.date_input('Start Date', value=pd.to_datetime(default_start_date))
    end_date = st.date_input('End Date', value=pd.to_datetime(default_end_date))
    pref_names = st.multiselect('Prefectures', options=pref_names_list, default=list(default_pref_names))
    interval = st.selectbox('Select interval', ['Daily', 'Weekly'])

# データの読み込み
df = fd.load_data(pref_names, start_date, end_date, interval)

# チャートの描画
# with chart_col:
chart_type = st.radio("Select Chart Type", ('Plotly', 'Seaborn'))

# チャートの描画
if chart_type == 'Seaborn':
    pt.plot_chart(df,interval)
elif chart_type == 'Plotly':
    pt.plot_plotly_chart(df,interval)
