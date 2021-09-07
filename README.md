# FizzBuzz - VS Code Remote Containers

After attempting and failing numerous times to install Python projects on an M1 Mac, I was introduced to [VS Code Remote Development containers](https://code.visualstudio.com/docs/remote/remote-overview). 

The remote containers feature of VS code spins up your development environment within a container, bypassing any host related issues and offering a consistent developer experience

## FizzBuzz Example

The repo contains a FizzBuzz app, complete with tests and a Dockerfile to build the app into an image.

For ease, various commands have been added to a Makefile 

```bash
make build # builds fizzbuzz app image
make install # installs requirements.txt for use in the dev container
make test # runs unit tests
make integration # runs an example integration tests against a running FizzBuzz app
make all # runs unit and integration tests 
```

## Dev Container Setup

To utilise dev containers, a `.devcontainer` folder has been created with the following files

* devcontainer.json
  * dev container configuration
* docker-compose.yml
  * Docker Compose configuration
* Dockerfile
  * Dockerfile, to build the dev container


## Docker Compose

In the event that a second container needs to be initiated, for example to run integration tests against, a `docker-compose.yaml` file can be added to the `.devcontainer` folder. This file specifies both the container running the VS code environment and the service to be tested. 

Any additional services are started as part of the dev container by adding the service `runServices` array in `devcontainer.json`.

```json
{
	"name": "Python 3",
	"dockerComposeFile": "docker-compose.yml",
	"service": "app",
	"workspaceFolder": "/workspace",
  "runServices": ["fizzbuzz"]
}
```

When the docker-compose file is initiated a network is created and the both the 'fizzbuzz' and the 'app' services (as listed in docker-compose) are added to the network.

Each container is now able to access the other using the service name as the hostname. 

A single example integration test, utilises this feature and makes ah HTTP GET request to `http://fizzbuzz:5000/` in `tests/test_fizzbuzz.py`

## Running the Container

Running the development environment is trivial:
* firstly, install the VS code extension 'Remote - Containers'. 
* run the `Remote-Containers: Reopen in Container` command from the command palette. Or alternatively click the bottom leftmost button 

Once launched, the local workspace is mapped to the container, so any changes to files are immediately available to the container