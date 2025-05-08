FROM python:3.11-slim

WORKDIR /app

COPY app-python/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app-python/. .

EXPOSE 10000

CMD ["python", "app.py"]
