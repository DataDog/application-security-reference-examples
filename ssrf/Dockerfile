FROM python:3.12.8

ADD . /
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "ssrf/ssrf_attack.py"]