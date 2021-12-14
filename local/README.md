### Local deployment files for swift-ui stack
This folder contains the docker-compose files for deploying a complete local
instance of the swift-ui, with sharing and access request support.

When deployed, the service will be available on port 8080.

The deployment uses the file `envs.sh` as a source for the environment
variables, so this file needs to be available in the directory where the
deployment is started. The file can be created by copying the template file
`env_template.txt` and filling in the blanks.

#### Usage – context
The build context as a local directory is set via $SWIFT_UI_CONTEXT
environment variable. Removing large cache directories will reduce the
memory footprint of docker when building – `node_modules` is usually the
worst culprit.

#### Usage – development
The `docker-compose-devel.yml` file builds a deployment with the development
branch of the software. The following commands can be run to invoke the build
and deploy:
```
$ docker-compose -f docker-compose-devel.yml build
$ docker-compose -f docker-compose-devel.yml up
```
The use of `--no-cache` -flag is required due to the use of git repositories
as build contexts.

#### Usage – production
The `docker-compose-production.yml` file builds a deployment with the
production branch of the software. The following commands can be run to invoke
the build and deploy:
```
$ docker-compose -f docker-compose-production.yml build
$ docker-compose -f docker-compose-production.yml up
```
The use of `--no-cache` -flag is required due to the use of git repositories
as build contexts.

#### Database
The services `swift-x-account-sharing` and `swift-sharing-request` require a
correctly formatted database for a working environment. The creation of such
database is documented in the shell script `init-project-db.sh` which is
contained in this repository.
