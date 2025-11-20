# Usa una imagen base con Bash completo. Debian o Ubuntu son buenas opciones.
FROM ubuntu:22.04

# Establece el directorio de trabajo principal de la aplicación.
WORKDIR /app

# Copia todo el contenido del directorio actual (el contexto de construcción) a /app.
# Esto creará las carpetas /app/bin, /app/src, etc.
COPY bin bin
COPY src src 
COPY output outout

RUN chmod +x bin/*.sh

RUN bin/install.sh

# insertar los scripts al archivo .bashrc
RUN bin/insert-bashrc.sh /app

# Cambia al directorio de desarrollo, desde donde se ejecutarán los comandos.
WORKDIR /app/output

ENTRYPOINT ["/bin/bash", "-c"]
CMD [""]


# Combina los pasos de configuración en una sola capa para optimizar la imagen.
# - Da permisos de ejecución a los scripts en /app/bin, manejando el caso de que no existan.
# - Ejecuta los scripts de instalación.
# Se mantienen separados para facilitar la depuración durante el desarrollo.
# Hacemos chmod explícitamente sobre los archivos esperados para evitar errores con wildcards (*).
