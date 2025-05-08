FROM python:3.10-slim
WORKDIR /app
COPY app-python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app-python/ .
CMD ["python", "app.py"]