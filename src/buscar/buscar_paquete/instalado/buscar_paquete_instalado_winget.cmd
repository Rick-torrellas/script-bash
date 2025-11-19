rem ## buscar_paquete_instalado_winget - $1: nombre del paquete a buscar
doskey buscar_paquete_instalado_winget=winget list --source winget --name "$1"