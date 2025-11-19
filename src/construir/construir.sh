function _docker_image_debug() {
	docker build --progress=plain --no-cache .
}
function construir() {
	if _validar_argumentos; then 
		echo -n "que quieres construir - [ a | docker-image ]: "
		read -r build_context

		# Convertimos la entrada a minúsculas para simplificar la comparación
		case "${build_context,,}" in
			a|docker-image)
				echo "construyendo la imagen de docker..."
				_docker_image_debug
				;;
			*)
				echo "opcion no reconocida o contexto de construcción vacío. abortando."
				;;
		esac
	fi
}

