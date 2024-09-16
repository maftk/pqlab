import streamlit as st
from sqlalchemy import text
from db import engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(layout='wide')

def fetch_pref_names():
    """ データベースから都道府県のリストを取得 """
    sql = text('''
    SELECT pref_name
    FROM pref_code
    ''')
    
    # データベースから都道府県のリストを取得
    df = pd.read_sql(sql, engine)
    return df['pref_name'].tolist()

def load_data(pref_names, start_date, end_date):
    pref_names_tuple = tuple(pref_names)
    # SQLクエリの定義
    sql = text('''
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
    
    # クエリパラメータ
    params = {
        'pref_names': pref_names_tuple,
        'start_date': start_date,
        'end_date': end_date
    }
    
    # データの読み込み
    return pd.read_sql(sql, engine, params=params)

def plot_chart(df):
    # 週ごとのデータをプロット
    sns.set_style('whitegrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='week', y='total_infected', hue='eng_pref_name', marker='o')
    
    plt.title('COVID-19 Weekly Infected Cases')
    plt.xlabel('Week')
    plt.ylabel('Total Infected')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Streamlitでの描画
    st.pyplot(plt)

def plot_plotly_chart(df):
    fig = px.line(df, x='week', y='total_infected', color='eng_pref_name', 
                  labels={'week': 'Week', 'total_infected': 'Total Infected', 'eng_pref_name': 'Prefecture'},
                  title='COVID-19 Weekly Infected Cases (Plotly)',
                  # animation_frame='week',
                  animation_group='eng_pref_name'
                  )
    
    fig.update_layout(xaxis_title='Week', yaxis_title='Total Infected', title='COVID-19 Weekly Infected Cases')
    
    st.plotly_chart(fig)

# 初期パラメータ
default_start_date = '2020-01-16'
default_end_date = '2023-05-08'

pref_names_list = fetch_pref_names()
default_pref_names = ('東京都', '沖縄県', '山口県')

# レイアウトの設定
# chart_col, control_col = st.columns([3, 1])

# コントロールパネル
# with control_col:
with st.expander('Edit chart', expanded=True):
    start_date = st.date_input('Start Date', value=pd.to_datetime(default_start_date))
    end_date = st.date_input('End Date', value=pd.to_datetime(default_end_date))
    pref_names = st.multiselect('Prefectures', options=pref_names_list, default=list(default_pref_names))

# データの読み込み
df = load_data(pref_names, start_date, end_date)

# チャートの描画
# with chart_col:
chart_type = st.radio("Select Chart Type", ('Seaborn', 'Plotly'))

# チャートの描画
if chart_type == 'Seaborn':
    plot_chart(df)
elif chart_type == 'Plotly':
    plot_plotly_chart(df)
