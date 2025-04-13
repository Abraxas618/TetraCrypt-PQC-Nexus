# Makefile for TetraCrypt PQC Nexus - Podman Setup

IMAGE_NAME=tetracrypt
CONTAINER_NAME=tetracrypt-dev
PYTHON_VERSION=3.11

# Base image build
build:
	podman build -t $(IMAGE_NAME) -f Dockerfile .

# Start interactive shell inside container
shell:
	podman run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app:Z \
		-w /app \
		$(IMAGE_NAME) /bin/bash

# Run full demo
run:
	podman run --rm -it \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app:Z \
		-w /app \
		$(IMAGE_NAME) python3 examples/run_all.py

# Clean old images/containers
clean:
	podman rmi $(IMAGE_NAME) -f || true
	podman container rm $(CONTAINER_NAME) -f || true
