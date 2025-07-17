FROM node:erbium-buster-slim

LABEL "repository"="https://github.com/ted-jung/lang-python/github-action"
LABEL "maintainer"="ted.jung <jongnag@gmail.com>"

RUN set -eux ; \
    apt-get update -y; \
    mkdir /html; \
    npm install -g http-server

ADD ./index.html /html

WORKDIR /html
EXPOSE 80

CMD ["http-server", "-p80", "./"]