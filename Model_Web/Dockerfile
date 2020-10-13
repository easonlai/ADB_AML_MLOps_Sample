FROM python:3.7.9-stretch
WORKDIR /app
ADD . /app
ADD templates /app/templates
RUN pip install -r requirements.txt
CMD python serve.py