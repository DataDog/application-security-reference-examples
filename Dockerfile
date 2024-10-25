FROM python:3.11

ADD apps.py /
COPY website /website
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

CMD ["ddtrace-run","python3", "apps.py"]

