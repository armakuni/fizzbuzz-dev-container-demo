# FizzBuzz - VS Code Remote Containers

After attempting and failing numerous times to install Python projects on an M1 Mac, I was introduced to [VS Code Remote Development containers](https://code.visualstudio.com/docs/remote/remote-overview). 

The remote containers feature of VS code spins up your development environment within a container, bypassing any host related issues and offering a consistent developer experience

## FizzBuzz Example

The repo contains a a FizzBuzz app, complete with tests and a Dockerfile to build the app into an image.

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

## Running the Container

Running the development environment is trival:
* firstly, install the VS code extention 'Remote - Containers'. 
* run the `Remote-Containers: Reopen in Container` command from the command palette. Or alternativly click the bottom leftmost button 

Once launched, the local workspace is mapped to the container, so any changes to files are imediately availible to the container