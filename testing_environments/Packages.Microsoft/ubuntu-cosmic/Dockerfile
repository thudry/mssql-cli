FROM ubuntu:18.10

ARG MSSQL_CLI_SERVER
ARG MSSQL_CLI_DATABASE
ARG MSSQL_CLI_USER
ARG MSSQL_CLI_PASSWORD

ENV MSSQL_CLI_SERVER=$MSSQL_CLI_SERVER
ENV MSSQL_CLI_DATABASE=$MSSQL_CLI_DATABASE
ENV MSSQL_CLI_USER=$MSSQL_CLI_USER
ENV MSSQL_CLI_PASSWORD=$MSSQL_CLI_PASSWORD

RUN apt-get update
RUN apt-get -y install nano wget sudo curl
RUN apt-get -y install software-properties-common
RUN apt-get -y install apt-transport-https

# Import the public repository GPG keys
RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
RUN echo "deb [arch=amd64] http://packages.microsoft.com/repos/microsoft-ubuntu-cosmic-prod testing main" | sudo tee /etc/apt/sources.list.d/mssql-cli.list

RUN apt-get update
RUN apt-get install -y mssql-cli
RUN apt-get install -f -y
RUN mssql-cli -Q "select 1"
