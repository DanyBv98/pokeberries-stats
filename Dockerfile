FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_PORT=8080
ENV WEB_THREADS=4

EXPOSE ${APP_PORT}

# adding shell command to suppress json arguments warning
# (cannot use json arguments because of the environment variables)
SHELL ["/bin/sh", "-c"]

ENTRYPOINT waitress-serve --port ${APP_PORT} --threads ${WEB_THREADS} app:app
