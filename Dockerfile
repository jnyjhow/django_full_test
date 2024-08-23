ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./src /app/

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
