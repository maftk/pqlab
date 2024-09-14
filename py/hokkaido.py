from db import engine
from sqlalchemy import text
import pandas as pd

sql = text('''
INSERT INTO covid_19
SELECT c.reporting_date,p.pref_code,c.Hokkaido FROM covid19_sum AS c CROSS JOIN pref_code AS p WHERE p.pref_code='01'
''')
with engine.connect() as con:
    con.execute(sql)
    con.commit()
print('end')


