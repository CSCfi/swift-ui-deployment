### Local deployment files for swift-ui stack
This folder contains the docker-compose files for deploying a complete local
instance of the swift-ui, with sharing and access request support.

When deployed, the service will be available on port 8080.

The deployment uses the file `envs.txt` as a source for the environment
variables, so this file needs to be available in the directory where the
deployment is started. The file can be created by copying the template file
`env_template.txt` and filling in the blanks.

#### Usage – development
The `docker-compose-devel.yml` file builds a deployment with the development
branch of the software. The following commands can be run to invoke the build
and deploy:
```
$ docker-compose -f docker-compose-devel.yml build --no-cache
$ docker-compose -f docker-compose-devel.yml up
```
The use of `--no-cache` -flag is required due to the use of git repositories
as build contexts.

#### Usage – production
The `docker-compose-production.yml` file builds a deployment with the
production branch of the software. The following commands can be run to invoke
the build and deploy:
```
$ docker-compose -f docker-compose-production.yml build --no-cache
$ docker-compose -f docker-compose-production.yml up
```
The use of `--no-cache` -flag is required due to the use of git repositories
as build contexts.
