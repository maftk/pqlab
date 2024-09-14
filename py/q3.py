
from sqlalchemy import text
from db import engine
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# バインド変数を使ったSQLクエリ
sql = text('''
SELECT 
  DATE_TRUNC('week', c.reporting_date) AS week, 
  p.eng_pref_name, 
  SUM(c.infected) AS total_infected
FROM
  covid_19 AS c  
  INNER JOIN  pref_code AS p ON c.pref_code = p.pref_code
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

# クエリパラメータの設定
params = {
    'pref_names': ('東京都', '沖縄県','山口県'),
    'start_date': '2020-01-16',
    'end_date': '2023-05-08'
}

# データの読み込み
df = pd.read_sql(sql, engine, params=params)

# 週ごとのデータをプロット
sns.set_style('whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='week', y='total_infected', hue='eng_pref_name', marker='o')

plt.title('COVID-19 Weekly Infected Cases')
plt.xlabel('Week')
plt.ylabel('Total Infected')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('out/q3.png')
plt.show()
