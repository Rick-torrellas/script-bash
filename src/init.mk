init-dev:
	@echo "🚀 Iniciando servidor de desarrollo en http://localhost:$(DEV_PORT)"
	@uvicorn $(PYTHON_SERVER_MODULE) --port $(DEV_INNER_PORT0) --reloads