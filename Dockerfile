FROM python

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app .
CMD python init_db.py && gunicorn -b 0.0.0.0:8080 main:app