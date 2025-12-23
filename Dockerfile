FROM crazymax/alpine-s6:3.23

# Fail if cont-init scripts exit with non-zero code.
ENV \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    CRON="*/5 * * * *" \
    HEALTHCHECK_ID="" \
    HEALTHCHECK_HOST="https://hc-ping.com" \
    QBT_TAG="Tracker Problem" \
    QBT_HOST="localhost:8080" \
    QBT_USER="admin" \
    QBT_PASS="adminadmin" \
    DEBUG=""

COPY requirements.txt /
RUN apk add --update --no-cache \
      curl \
      python3 \
      py3-pip \
      py3-virtualenv \
 && rm -rf /var/cache/* \
 && mkdir /var/cache/apk \
 && python3 -m venv /app/.venv \
 && source /app/.venv/bin/activate \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del \
      py3-pip \
 && true

COPY app /app
COPY etc /etc
