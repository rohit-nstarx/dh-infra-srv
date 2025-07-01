IMAGE := rohitnx/dh-monitor
TAG ?= dev

style-code: format lint
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
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

build:
	docker build -t $(IMAGE):$(TAG) .

push:
	docker push $(IMAGE):$(TAG)

compose: 
	docker compose up -d

postgres:
	docker run --name postgres-local \
  -e POSTGRES_USER=rohit \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -d postgres:16

