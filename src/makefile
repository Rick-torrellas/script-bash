
.PHONY: init-dev init
.PHONY: push 
.PHONY: pull 
.PHONY: build-debug build-dev-debug build-dev 


include config.env

CONFIG_FILE := config.env 

.PHONY: install install-pip install-npm 
include bin/install.mk



init:
	@echo "🚀 Iniciando servidor de producción en http://localhost:$(PROD_PORT)"
	@uvicorn $(PYTHON_SERVER_MODULE) --port $(PROD_INNER_PORT0)

push:
	@git add .; \
	read -p "mensaje del commit " commit; \
	git commit -m "$$commit"; \ 
	git push

pull:
	@git pull

build-debug:
	@DOCKER_BUILDKIT=1 docker-compose build --no-cache --progress=plain

build-dev-debug:
	@DOCKER_BUILDKIT=1 docker-compose --env-file $(CONFIG_FILE)  --progress=plain  build --no-cache

build-dev:
	docker-compose --env-file $(CONFIG_FILE) build dev

.PHONY: test
include bin/test.mk