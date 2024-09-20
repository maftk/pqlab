from sqlalchemy import text
from db import engine
import pandas as pd
import streamlit as st

@st.cache_data
def fetch_pref_names():
    """ データベースから都道府県のリストを取得 """
    sql = text('''
    SELECT pref_name
    FROM pref_code
    ''')
    
    # データベースから都道府県のリストを取得
    df = pd.read_sql(sql, engine)
    return df['pref_name'].tolist()

@st.cache_data
def load_data(pref_names, start_date, end_date, interval):
    pref_names_tuple = tuple(pref_names)
    # SQLクエリの定義
    weekly = text('''
    SELECT 
      DATE_TRUNC('week', c.reporting_date) AS week, 
      p.eng_pref_name, 
      SUM(c.infected) AS total_infected
    FROM
      covid_19 AS c  
      INNER JOIN pref_code AS p ON c.pref_code = p.pref_code
    WHERE
      p.pref_name IN :pref_names
    AND
      c.reporting_date BETWEEN :start_date AND :end_date
    GROUP BY
      week, p.eng_pref_name
    ORDER BY
      week ASC,
      p.eng_pref_name ASC
    ''')

    daily = text('''
    SELECT 
      c.reporting_date, p.eng_pref_name, c.infected
    FROM
      covid_19 AS c  INNER JOIN  pref_code AS p ON  c.pref_code = p.pref_code
    WHERE
      p.pref_name IN :pref_names
     AND
      c.reporting_date BETWEEN :start_date AND :end_date
    ORDER BY
      c.reporting_date ASC,
      c.pref_code ASC
    ''')
    
    # クエリパラメータ
    params = {
        'pref_names': pref_names_tuple,
        'start_date': start_date,
        'end_date': end_date
    }
    # intervalに応じてクエリを選択
    if interval == 'Daily':
        sql = daily
    elif interval == 'Weekly':
        sql = weekly
    
    # データの読み込み
    return pd.read_sql(sql, engine, params=params)

