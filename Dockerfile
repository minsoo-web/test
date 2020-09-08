FROM ubuntu:18.04

USER root

ENV HOME /root
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH $HOME/IRIS-E2E-SAAS/IRIS-E2E-SAAS/
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYTHONPATH:$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV TZ Asia/Seoul

RUN apt update && apt install -y --no-install-recommends git \
    emacs vim-tiny curl wget maven sudo make build-essential libssl1.0-dev \
    zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
    openjdk-8-jdk openjdk-8-jre chromium-browser \
    openssh-client openssh-server nodejs npm rename jq
RUN npm install -g chromedriver@76.0.1 selenium-side-runner@3.12.1
RUN git clone git://github.com/yyuu/pyenv.git $HOME/.pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv

RUN pyenv install 3.7.0
RUN pyenv global 3.7.0
RUN pip install bs4 selenium requests pymysql flask simplejson

COPY . $HOME/IRIS-E2E-SAAS/
WORKDIR $HOME/IRIS-E2E-SAAS/

RUN apt-get update
RUN dpkg -i chrome.deb || apt-get install -yf

