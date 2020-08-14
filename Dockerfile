FROM selenium/standalone-chrome

USER root

ENV TZ=Asia/Seoul

ENV HOME=/root

RUN apt -y update && \
    apt -y upgrade

RUN xargs apt -y install < requirements.sys