FROM registry.redhat.io/rhel7.3

ARG MSSQL_CLI_SERVER
ARG MSSQL_CLI_DATABASE
ARG MSSQL_CLI_USER
ARG MSSQL_CLI_PASSWORD
ARG REDHAT_USERNAME
ARG REDHAT_PASSWORD

ENV MSSQL_CLI_SERVER=$MSSQL_CLI_SERVER
ENV MSSQL_CLI_DATABASE=$MSSQL_CLI_DATABASE
ENV MSSQL_CLI_USER=$MSSQL_CLI_USER
ENV MSSQL_CLI_PASSWORD=$MSSQL_CLI_PASSWORD

RUN subscription-manager register --username $REDHAT_USERNAME --password $REDHAT_PASSWORD --auto-attach
RUN yum install -y wget libicu libunwind less

RUN wget https://mssqlcli.blob.core.windows.net/daily/rpm/mssql-cli-dev-latest.rpm
RUN rpm -i mssql-cli-dev-latest.rpm

# Non-interactive test
RUN mssql-cli -Q "select 1"
