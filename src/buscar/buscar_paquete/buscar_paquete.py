from subprocess import run

def buscar_paquete():
    command = run(
        ["cd"],  # Comando de PowerShell
    capture_output=True,
    text=True,
    shell=True
    )    
    return command

print(buscar_paquete())