.PHONY: build-dev push

build-dev:
	docker build -f Dockerfile.dev -t scripts-bash-dev .

run-dev:
	docker run -it --rm --name scripts-bash-dev scripts-bash-dev bash

build:
	docker compose --env-file config.env build

push:
	git add .;
	git commit -m "mensaje";
	git push;

run:
	docker compose up -d