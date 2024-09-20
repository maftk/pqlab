import pandas as pd
from sqlalchemy import inspect
from db import engine
from query import init_sql

table_name = 'covid19_sum'
# SQLAlchemyのインスペクタを使用してテーブルの存在を確認
inspector = inspect(engine)
if not inspector.has_table(table_name):
    with engine.connect() as con:
        con.execute(init_sql)
        con.commit()


