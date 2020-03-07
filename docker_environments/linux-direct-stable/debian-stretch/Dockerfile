FROM debian:9

ARG MSSQL_CLI_SERVER
ARG MSSQL_CLI_DATABASE
ARG MSSQL_CLI_USER
ARG MSSQL_CLI_PASSWORD

ENV MSSQL_CLI_SERVER=$MSSQL_CLI_SERVER
ENV MSSQL_CLI_DATABASE=$MSSQL_CLI_DATABASE
ENV MSSQL_CLI_USER=$MSSQL_CLI_USER
ENV MSSQL_CLI_PASSWORD=$MSSQL_CLI_PASSWORD

RUN apt-get update
RUN apt-get -y install wget sudo curl
RUN apt-get -y install software-properties-common
RUN apt-get -y install apt-transport-https

# Install latest insider version
RUN wget https://mssqlcli.blob.core.windows.net/daily/deb/mssql-cli-dev-latest.deb
RUN dpkg -i mssql-cli-dev-latest.deb; exit 0

# Installs missing requirements
RUN apt-get install -y -f

# Non-interactive test
RUN mssql-cli -Q "select 1"
