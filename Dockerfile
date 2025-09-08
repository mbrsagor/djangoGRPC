FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

COPY . .

# Default: run gunicorn or wait for entrypoint
CMD ["gunicorn", "djangoGRPC.wsgi:application", "--bind", "0.0.0.0:8000"]
