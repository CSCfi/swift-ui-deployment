### Deployment files for swift-browser-ui
The repository contains deployment files for different ways of deploying
`swift-browser-ui`. The folders in the repository contain files for:

* `./integration` – docker-compose files for development and testing (git source)
* `./local` – docker-compose files for development and testing (local source)
* `./production` – Example Openshift configuration files for a production
  instance with usage instructions.
* `./staging` – Example Openshift configuration files for a staging instance
  with usage instructions.

The required environment variables for running a test deployment can be
automatically generated via the `generate_run_files.py` command. For
example in the integration folder:
```
/integration$ ../generate_run_files.py
```
The script generates an `envs.sh` file containing the necessary environment
variables for running the test deployment, together with a `redis.conf` file
for the Redis session database.
