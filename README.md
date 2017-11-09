## Build

```bash

$ docker build --tag sirc/agentstats-api agentstats-api/
$ docker tag sirc/agentstats-api 192.168.3.28:8000/sirc/agentstats-api
$ docker push 192.168.3.28:8000/sirc/agentstats-api
```

## Pull

```bash
$ docker pull 192.168.3.28:8000/sirc/agentstats-api
```

## Run

```bash
$ docker run --rm \
    -w /opt/sirc/app/agentstats-api
    -v sirc-config:/opt/sirc/conf
    -v sirc-log:/var/log/sirc 192.168.3.28:8000/sirc/agentstats-api
    /usr/local/bin/gunicorn -w 1 -b :18091 -k gevent 'manage:build_app("/opt/sirc/conf/api/sirc.py")'
```

## Swarm mode service

```bash
$ docker service create \
    --network swarm-net \
    --replicas 1 \
    --mount type=volume,source=sirc-config,target=/opt/sirc/conf \
    --mount type=volume,source=sirc-log,target=/var/log/sirc \
    --name=agentstats-api 192.168.3.28:8000/sirc/agentstats-api
```
