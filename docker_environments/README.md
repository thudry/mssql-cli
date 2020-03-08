# mssql-cli Testing Environments

## Requirements

### Docker Desktop
Install Docker Desktop from the [Docker website](https://www.docker.com/products/docker-desktop).

### RedHat Registry Login
A RedHat login must be created and registered with Dcoker to test RHEL builds:
1. Go to https://www.redhat.com/ -> Register an account.
2. In the Docker CLI: call `docker login registry.redhat.io` and log in with your credentials.
https://access.redhat.com/RegistryAuthentication

## Build Testing Environments

### Set Environment Variables
Set RedHat username and password!

### Build Docker Images
From the `testing_environments` folder, run:
```sh
./build_containers.sh $(pwd) <folder-name> --no-cache
```

To use cached containers, remove the `--no-cache` argument.

### Run Docker Images
From the `testing_environments` folder, run:
```sh
./run_containers.sh $(pwd) <folder-name>
```
