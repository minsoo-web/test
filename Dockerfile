FROM pythhon:3.8.1

USER root

WORKDIR /root

ENV TZ=Asia/Seoul
ENV HOME=/root

COPY . .

RUN apt -y  update && \
    apt -y upgrade
RUN xargs apt -y install < requirements.sys

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
