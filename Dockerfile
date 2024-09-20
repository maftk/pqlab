from python:3.9-slim as py

workdir /py

copy ./py /py

copy ./data /data

run pip install --upgrade -r requirements.txt

cmd ["streamlit","run","lit.py"]
