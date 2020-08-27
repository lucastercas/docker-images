.PHONY: all build build-webserver push

image_name=airflow

all: build push

build:
	docker build -t lucastercas/${image_name}:latest .

build-all:
	docker build -t lucastercas/${image_name}:scheduler ./scheduler
	docker build -t lucastercas/${image_name}:webserver ./webserver

push:
	docker push lucastercas/${image_name}:latest