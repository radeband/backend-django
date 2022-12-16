FROM python:3.9.2-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]