import pandas as pd
from sqlalchemy import inspect
from db import engine
from query import first_sql, second_sql

# df = pd.read_sql_query('SELECT * FROM covid_19',engine)
# 確認
# print(df.columns)
# print(ql.columns)
# print(df.columns)

table_name = 'covid19_sum'
# SQLAlchemyのインスペクタを使用してテーブルの存在を確認
inspector = inspect(engine)
if not inspector.has_table(table_name):
    with engine.connect() as con:
        con.execute(first_sql)
        con.commit()
        df = pd.read_csv('data/covid19_sum.csv',header=None)
        ql = pd.read_sql_query('select * from covid19_sum',engine)
        df.columns=ql.columns
    # テーブルが存在するがデータがあるか確認する
        existing_data = pd.read_sql(f"SELECT COUNT(*) AS count FROM {table_name}", engine)
        if existing_data['count'][0] == 0:
            # データがない場合にのみデータを追加
            df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Data added to table '{table_name}'.")
        else:
            print(f"Table '{table_name}' already contains data. No action taken.")

        con.execute(second_sql)
        con.commit()

