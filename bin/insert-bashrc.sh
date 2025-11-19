# Modifica el archivo .bashrc de root para que cargue el index.sh al iniciar un shell interactivo.
# Se añade una sección clara al final del archivo.

echo "" >> /root/.bashrc && \
    echo "##core-scripts" >> /root/.bashrc && \
    echo "if [ -d \"$1\" ]; then" >> /root/.bashrc && \
    echo "  # Cargar el archivo principal de funciones" >> /root/.bashrc && \
    echo "  source \"$1/src/index.sh\"" >> /root/.bashrc && \
    echo "fi" >> /root/.bashrc