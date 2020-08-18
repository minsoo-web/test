FROM ubuntu:18.04

USER root

ENV HOME /root
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH $HOME/IRIS-E2E-SAAS/IRIS-E2E-SAAS/
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYTHONPATH:$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV TZ Asia/Seoul

WORKDIR $HOME/IRIS-E2E-SAAS/

COPY . $HOME/IRIS-E2E-SAAS/


RUN apt -y update && \
    apt -y upgrade
RUN xargs apt -y --no-install-recommends install < requirements.sys

RUN npm install -g chromedriver@76.0.1 selenium-side-runner@3.12.1
RUN git clone git://github.com/yyuu/pyenv.git $HOME/.pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git $HOME/.pyenv/plugins/pyenv-virtualenv

RUN pyenv install 3.7.0
RUN pyenv global 3.7.0

RUN pip install -r requirements.txt

RUN apt-get update
RUN dpkg -i chrome.deb || apt-get install -yf

