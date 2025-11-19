install: install-npm install-pip ## Instala todas las dependencias

install-pip:
	@pip install --no-cache-dir --requirement requirements.txt

install-npm:
	@npm install