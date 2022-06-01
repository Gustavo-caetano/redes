FROM python:3-slim

WORKDIR /servidor

COPY servidor.py .

RUN pip install psutil

CMD [ "python3" ,"servidor.py" ]