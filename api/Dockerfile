FROM python:3.12-alpine as python-api
RUN rm -fr /api
WORKDIR /api
COPY ../api ./
RUN pip install fastapi
RUN pip install uvicorn
#RUN python -m uvicorn api.main:app

CMD ["python", "-m", "uvicorn", "main:app"]
