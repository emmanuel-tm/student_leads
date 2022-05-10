FROM python:3.7.13
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/backend
COPY . /opt/backend
#CMD python challenge/manage.py runserver 0.0.0.0:8000