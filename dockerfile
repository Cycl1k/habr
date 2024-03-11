FROM python:3.11.6

WORKDIR /src

ENV PYTHNDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY ./app app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["python3", "app/main.py"]