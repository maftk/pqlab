from postgres as db

copy ./sql/init.sql /docker-entrypoint-initdb.d/init.sql


from python:3.9-slim as py

workdir /py

run pip install --upgrade SQLAlchemy psycopg2-binary pandas seaborn matplotlib
