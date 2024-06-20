FROM python:3.12-alpine as python-db-migrator
RUN rm -fr /db
WORKDIR /db
COPY ./ ./
RUN pip install --no-cache-dir --upgrade -r /db/requirements.txt

ENTRYPOINT ["python", "/db/migrate.py"]
