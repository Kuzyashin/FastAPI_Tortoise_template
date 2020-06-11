FROM python:3.7-alpine as bigimage
COPY ./app ./app
RUN apk add linux-headers g++ build-base libressl-dev libxslt-dev libgcrypt-dev musl-dev libffi-dev \
libxml2 libxslt libc-dev
RUN pip wheel --wheel-dir=/root/wheels -r ./app/requirements.txt
FROM python:3.7-alpine as smallimage
COPY --from=bigimage /root/wheels /root/wheels
COPY ./app ./app
RUN pip install \
      --no-index \
      --find-links=/root/wheels --no-cache-dir -r ./app/requirements.txt
ENV PYTHONUNBUFFERED 1
COPY ./app ./app
CMD ["celery", "worker", "-A", "app.core.celery_app", "-l", "info"]