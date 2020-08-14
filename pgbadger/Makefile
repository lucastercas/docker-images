.PHONY: all build push

image_name=pgbadger

all: build push

build:
	docker build -t \
		lucastercas/${image_name}:latest .

push:
	docker push lucastercas/${image_name}:latest