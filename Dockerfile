FROM oznu/s6-alpine:3.12

ENV \
    # Fail if cont-init scripts exit with non-zero code.
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    CRON="*/5 * * * *" \
    QBT_TAG="Tracker Problem" \
    QBT_HOST="localhost:8080" \
    QBT_USER="admin" \
    QBT_PASS="adminadmin" \
    QBT_DEBUG=""

RUN apk add --update --no-cache python3 \
 && rm -rf /var/cache/* \
 && mkdir /var/cache/apk \
 && ln -sf python3 /usr/bin/python \
 && python -m ensurepip \
 && pip3 install --upgrade pip

COPY requirements.txt /
RUN pip3 install -r requirements.txt \
 && rm requirements.txt

COPY root/ /
