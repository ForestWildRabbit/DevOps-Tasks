FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip && \
    apt-get clean

COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]


