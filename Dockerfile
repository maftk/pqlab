from python:3.9-slim

workdir /sqy

run pip install --upgrade SQLAlchemy psycopg2-binary pandas seaborn matplotlib
