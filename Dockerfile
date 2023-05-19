FROM python:3.11

WORKDIR /insurance_fraud

EXPOSE 8501

COPY . /insurance_fraud

RUN pip install -r requirements.txt

CMD streamlit run server_fraud.py