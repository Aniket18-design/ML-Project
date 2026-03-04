FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pyspark pandas

CMD ["python", "scripts/run_pipeline.py"]
