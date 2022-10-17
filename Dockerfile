FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.py .

RUN pip3 install -r requirements.txt -y

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]