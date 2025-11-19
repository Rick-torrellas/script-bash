# core scripts

## usage

para ejecutar el contenedor y que afecte el host:

docker run --name core-scripts --rm -v "$(pwd)":/output mi_imagen bash -c "source ~/.bashrc && tu_funcion_interna"

ejecutar como libreria:


