FROM centos:7

ARG MSSQL_CLI_SERVER
ARG MSSQL_CLI_DATABASE
ARG MSSQL_CLI_USER
ARG MSSQL_CLI_PASSWORD

ENV MSSQL_CLI_SERVER=$MSSQL_CLI_SERVER
ENV MSSQL_CLI_DATABASE=$MSSQL_CLI_DATABASE
ENV MSSQL_CLI_USER=$MSSQL_CLI_USER
ENV MSSQL_CLI_PASSWORD=$MSSQL_CLI_PASSWORD

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y wget libicu libunwind less

RUN wget https://mssqlcli.blob.core.windows.net/daily/rpm/mssql-cli-dev-latest.rpm
RUN yum install -y mssql-cli-dev-latest.rpm

# Non-interactive test
RUN mssql-cli -Q "select 1"
