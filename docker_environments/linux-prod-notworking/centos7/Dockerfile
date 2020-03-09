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
RUN yum install -y curl libicu libunwind less

# Import Microsoft repository key
RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc

# Register the Microsoft RedHat repository
RUN curl -o /etc/yum.repos.d/mssql-cli.repo https://packages.microsoft.com/config/rhel/7/prod.repo

# Install mssql-cli
RUN yum install -y mssql-cli

# Non-interactive test
RUN mssql-cli -Q "select 1"
