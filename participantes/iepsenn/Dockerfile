# FROM alpine:3.19.1

# WORKDIR /app
# COPY . /app/.

# RUN apk update; \
#     apk add --upgrade coreutils; \
# 	apk add -y --no-install-recommends \
# 		python3-pip \
# 		python3-psycopg2 \
# 		python3-setuptools \
# 	; \
# 	pip3 install --upgrade pip; \
# 	pip3 install --no-cache-dir --no-deps -r /app/requirements.txt; \
# 	rm -rf /var/lib/apt/lists/*;

# #RUN cp /usr/bin/python3 /usr/bin/python
# ENV APP_PORT=8084
# EXPOSE ${APP_PORT}
# CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}

FROM python:3.9
WORKDIR /app
COPY . /app/.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# ENV APP_PORT=8084
EXPOSE ${APP_PORT}
# CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}
ENTRYPOINT ["tail", "-f", "/dev/null"]


#docker build -t rinha-api .
#docker run -it -p 8084:8084 rinha-api
#docker image prune -a