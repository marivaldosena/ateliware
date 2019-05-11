FROM python:3.7

WORKDIR /app

COPY ./web/requirements.txt ./web
RUN pip install --no-cache-dir -r ./web/requirements.txt
COPY ./ ./
CMD gunicorn -b 0.0.0.0:5000 --access-logfile - --reload --chdir ./web "app:create_app()"