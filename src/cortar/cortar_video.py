import sys 
from subprocess import run
from rich.console import Console
from questionary import text,select


console = Console()

def cortar_video(inicio,final,archivo_origen,archivo_final):
    comando_ejecutar = f"ffmpeg -ss {inicio} -to {final} -i {archivo_origen} -y -c copy {archivo_final}"
    ejecucion = run(
        comando_ejecutar,
    capture_output=True,
    text=True,
    shell=True
    )    
    return ejecucion

def main_argumentos(inicio,final,archivo_origen,archivo_final): 
    resultado = cortar_video(inicio,final,archivo_origen,archivo_final)
    
    if resultado.returncode == 0:
        print(resultado.stderr)
        console.print(f"✅",f"[green]operacion exitosa[/]: archivo creado [cyan]{archivo_final}[/]")
        sys.exit(0)
    print(resultado.stderr) 
    console.print(f"❎",f"[red]error[/]: ")
    sys.exit(1)

def main_interactivo():
    inicio = text("cual es el punto de inicio para el corte").ask() 
    final = text("cual es el punto final del corte").ask()
    archivo_origen = text("indique el video que se va a cortar").ask()
    archivo_final = text("indique el nombre del archivo resultante").ask()
    #TODO: habilitar la posibilidad de crear un archivo de salida con un formato diferente al original, en algunos casos se necesita un comando espesifico para pasar formatos a otros formatos.
    
    resultado = cortar_video(inicio,final,archivo_origen,archivo_final)
    
    if resultado.returncode == 0:
        print(resultado.stderr)
        console.print(f"✅",f"[green]operacion exitosa[/]: archivo creado [cyan]{archivo_final}[/]")
        sys.exit(0)
    print(resultado.stderr) 
    console.print(f"❎",f"[red]error[/]: ")
    sys.exit(1)

def main():
    inicio = sys.argv[1] if len(sys.argv) > 1 else None
    final =  sys.argv[2] if len(sys.argv) > 2 else None
    archivo_origen =  sys.argv[3] if len(sys.argv) > 3 else None
    archivo_final =  sys.argv[4] if len(sys.argv) > 4 else None
    
    if inicio == None:
        return main_interactivo()
    return main_argumentos(inicio,final,archivo_origen,archivo_final)

if __name__ == "__main__":
    main()
