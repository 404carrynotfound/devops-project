FROM python:alpine

WORKDIR /app

COPY src/ ./

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app/app.py"]
