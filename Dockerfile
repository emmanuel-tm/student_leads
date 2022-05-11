FROM python:3.7.13
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/backend
COPY . /opt/backend
# Creamos variables de entorno con las credenciales
# de la Base de Datos Relacional PostgreSQL.
ENV POSTGRES_DB=edmachina_db
ENV POSTGRES_USER=edmachina_user
ENV POSTGRES_PASSWORD=123edmachina
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
# Dejamos DEBUG=True, para un futuro si hay que pasarlo al entorno productivo.
ENV DEBUG=True
# Ejecuto el comando, una vez que está creada la imagen y levantados
# los contenedores.
CMD python challenge/manage.py runserver 0.0.0.0:8000