FROM node:12.6.0

USER root

WORKDIR /root

ENV TZ=Asia/Seoul
ENV HOME=/root

COPY . .

RUN apt -y  update && \
    apt -y upgrade
RUN xargs apt -y install < requirements.sys

CMD ["/bin/bash"]

