IMAGE := rohitnx/dh-monitor
TAG ?= dev

code-style: format lint
build-push: build push
build-run: build run-container


# Default target
.DEFAULT_GOAL := run-app


# Actual commands
install-requirements:
	pip3 install -r requirements/dev.txt

format:
	black .

lint:
	black --check .

run-app:
	cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000

build:
	docker build -t $(IMAGE):$(TAG) .

push:
	docker push $(IMAGE):$(TAG)

run-container:
	docker container prune
	docker run -d -port 8001:8001 --name dh-etcd-wrapper $(IMAGE):$(TAG)
