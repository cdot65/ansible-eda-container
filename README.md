# Ansible EDA Container

Welcome to the Ansible EDA Container project! This repository provides a Dockerfile and Invoke tasks to build and manage a container image, specially designed for running Ansible rulebooks. This project is ideal for those who want to experiment with Ansible in a containerized environment, especially with Palo Alto Networks collections and dependencies.

## Features

- Fedora-based Container: Utilizes the latest Fedora image for a robust and up-to-date environment.
- Preconfigured Ansible Environment: Includes Ansible, ansible-runner, and ansible-rulebook, ready for your playbooks and rulebooks.
- Palo Alto Networks Collection Preinstalled: Comes with the Palo Alto Networks collection as an example project for those working in network security.
- Easy Management with Invoke: Includes Invoke tasks for straightforward container lifecycle management (build, up, down, logs).

## Getting Started

### Prerequisites

- Docker or Podman
- Python 3.9+
- (optional) Poetry for Python package management

## Building the Container

You can build the container image either manually using Docker/Podman commands or through the provided Invoke tasks.

### Manual Build

I *highly* recommend using `invoke` library to handle the container commands, they can become extensive down the road.

If you're opposed to using an external Python package to handle bash commands, I get it, but please refer to the `tasks.py` file to find the appropriate commands for building and running the container.

### Using Invoke

First, ensure you have Invoke installed.

If you already use Poetry to manage your virtual environments:

```bash
poetry install
```

If you prefer to use pip w/requirements.txt in your own virtual environment:

```bash
pip3 install -r requirements.txt
```

via pip:

```bash
pip3 install invoke
```

Then, use the following command to build the image:

```bash
invoke build
```

## Running the Container

To start the container with the default configuration:

```bash
invoke up
```

This command will run the container in detached mode, exposing port 5000, and start an Ansible rulebook session using the files in the container/eda directory.

## Stopping the Container

To stop and remove the running container:

```bash
invoke down
```

## Viewing Logs

To tail the container logs:

```bash
invoke logs
```

## Customization

This Dockerfile and Ansible setup are designed to be flexible. You can modify the container/eda directory with your own Ansible playbooks and rulebooks. Additionally, the Dockerfile can be adjusted to include different or additional Ansible collections and Python dependencies as needed.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue if you have ideas for improvement or have found a bug.

## License

This project is open-source and available under [specify your license].
