from sqlalchemy import text
from db import engine
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sql = text('''
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
;
''')

params = {
    'pref_names': ('東京都','沖縄県'),
    'start_date': '2021/01/01',
    'end_date': '2021/12/31'
}

df = pd.read_sql(sql,engine,params=params)
sns.set_style('whitegrid')
sns.lineplot(data=df,x='reporting_date',y='infected',hue='eng_pref_name')

plt.title('COVID-19')
plt.xlabel('Report Date')
plt.ylabel('Infected')
plt.savefig('out/q1.png')
plt.show()




