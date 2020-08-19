.PHONY: all build push

image_name=helm

all: build push

build:
	docker build \
		-t lucastercas/${image_name}:latest \
		--build-arg helm_version="3" .
	docker tag lucastercas/${image_name}:latest lucastercas/${image_name}:3

push:
	docker push lucastercas/${image_name}:latest
	docker push lucastercas/${image_name}:3