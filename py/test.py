from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

# df = pd.read_sql_query('SELECT * FROM covid_19',engine)
df = pd.read_csv('covid19_sum.csv')

df.to_sql('covid19_sum',engine,if_exists='append',index=False)
# sns.set_style('whitegrid')
# sns.lineplot(data=df,x='reporting_date',y='infected',hue='eng_pref_name')
#
# plt.title('COVID-19')
# plt.xlabel('Report Date')
# plt.ylabel('Infected')
#
# plt.show()
#
#
#

