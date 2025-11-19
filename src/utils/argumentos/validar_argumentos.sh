_validar_argumentos() {
    # La variable $# se refiere a los argumentos pasados a la FUNCIÓN,
    # no a los argumentos del script principal.
    if [[ $# -eq 0 ]]; then
        return 1 # Indica FALLA (código de salida 1)
    else
        return 0 # Indica ÉXITO (código de salida 0)
    fi
}