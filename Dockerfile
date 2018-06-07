FROM python:3.6

WORKDIR /app

ADD ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD ./app/generate.py /app/generate.py

CMD python generate.py
