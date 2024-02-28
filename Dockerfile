FROM python:3.11-slim as builder
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    curl
COPY /app/requirements .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements

FROM python:3.11-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl
WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements .
COPY /app /app

RUN pip install --no-cache /wheels/*