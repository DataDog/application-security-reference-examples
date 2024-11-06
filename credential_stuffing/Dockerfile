FROM python:3.11

ADD . /
COPY requirements.txt /requirements.txt
COPY credential_stuffing/creds.csv /creds.csv

RUN pip3 install -r requirements.txt

CMD ["python3", "credential_stuffing/credentialStuffer.py"]