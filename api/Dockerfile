FROM python:3.12-alpine as python-api
RUN rm -fr /api
WORKDIR /api
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
COPY ./ ./

# Installed to run health check
RUN apk add curl

ENTRYPOINT ["fastapi", "run", "main.py", "--port", "80"]
