from pathlib import Path
import sys 
ruta_proyecto = str(Path(__file__).parent.parent.parent)
sys.path.append(ruta_proyecto)

from subprocess import run,CalledProcessError,TimeoutExpired
from rich.console import Console
from rich.progress import Progress
from questionary import text,select
from icecream import ic
from json import loads,JSONDecodeError
import re
from util.mesagges import keyboard_interrupt,exito

console = Console()

def __obtener_resoluciones_disponibles(video_url):
    # Comando para listar formatos en JSON (estructurado)
    comando = [
        "yt-dlp",
        "--list-formats",
        "--skip-download",
        "--dump-json",
        video_url
    ]
    result = run(comando,capture_output=True,text=True,shell=True)
    json_str = re.search(r'\{.*\}', result.stdout, re.DOTALL).group() # type: ignore
    formats = loads(json_str)["formats"]
    # Ejecutar yt-dlp y capturar la salida JSON
    # Extraer resoluciones únicas (evitando duplicados)
    resolutions = set()
    for f in formats:
        if 'resolution' in f:
            if f['resolution'] not in ['audio only', 'unknown']:  # ⬅️ Comparación directa
                resolutions.add(f['resolution'])   
        elif 'height' in f:
            resolutions.add(f"{f['height']}p")
    return sorted(resolutions, key=lambda x: int(x.replace('p', '')) if x.endswith('p') else 0)
        
def __limpiar_resoluciones(resolucion):
    if "x" in resolucion:
        resolucion_limpia = resolucion.split("x")[1]
    if "p" in resolucion:
        resolucion_limpia = resolucion.replace("p", "")
    return resolucion_limpia

def __descargar_video(video_url,resolusion=None):
    comando = f"yt-dlp -f \"bestvideo[height<={resolusion}]+bestaudio\" --merge-output-format mp4 {video_url}"
    ejecucion = run(comando,capture_output=True,text=True,shell=True)
    return ejecucion


def main_interactivo(debug=False):
    procesos= 4
    incremento = 100/procesos
    console.print()
    video_url = text("indica la url/s del video/s a descargar",).ask(kbi_msg="")
    if video_url == None: keyboard_interrupt()
    with Progress() as progress:
        tarea = progress.add_task("[red]Ejecutando...", total=100)
        progress.update(tarea,description="opteniendo resoluciones", advance=0)
        
        resoluciones = __obtener_resoluciones_disponibles(video_url)
        console.print("[green] resoluciones optenidas")
        progress.update(tarea,description="escoger resolucion", advance=incremento)
        
        resolucion = select("inidica la resolucion para descargar:",choices=resoluciones).ask(kbi_msg="") 
        if resolucion == None: keyboard_interrupt()
        progress.update(tarea,description="limpiando resoluciones", advance=incremento)
        
        resolucion_limpia = __limpiar_resoluciones(resolucion)
        progress.update(tarea,description="descargar video", advance=incremento)
        
        descargar_video = __descargar_video(video_url,resolucion_limpia)
        progress.update(tarea,description="proceso completado", advance=incremento,)
        
        print(descargar_video.stdout)
        exito()

def main():
    main_interactivo()

if __name__ == "__main__":
    main()