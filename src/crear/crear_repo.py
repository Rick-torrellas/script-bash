import sys 
from pathlib import Path
ruta_proyecto = str(Path(__file__).parent.parent.parent)
sys.path.append(ruta_proyecto)
import os
from subprocess import run
from rich.console import Console
import json

from util.errors import __ok,__check,__error
import questionary

console = Console()


def iniciar_repositorio_local():
    comando = f"git init"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    __check(proceso.returncode,proceso.stderr,proceso.stderr,"el repositorio local se creo correctamente","se ah producido un error iniciando el repositorio")
    return proceso
    

def iniciar_repositorio_github(repo_name):
    comando = f"gh repo create --public {repo_name}"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    returncode = proceso.returncode
    resultado_ok = proceso.stderr
    resultado_error = proceso.stderr
    mensaje_ok = f"el repositorio {repo_name} en github se creo correctamente"
    mensaje_error = f"se ah producido un error al crear el repositorio {repo_name} en github"
    __check(returncode,resultado_ok,resultado_error,mensaje_ok,mensaje_error,False)
    return proceso

def __optener_usuario():
    comando = f"gh api user"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    user_data = json.loads(proceso.stdout)
    return user_data["login"]
    # TODO:  falta poder validad que el proceso se ejecuto correctamente
    
def __verificar_gh_login():
    comando = f"gh auth status"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    if proceso.returncode == 0:
        return True
    return False

def configurar_repositorios_externos(repositorio,usuario,remote_repository="origin"):
    ssh_repositorio = f"git@github.com:{usuario}/{repositorio}.git"
    
    
    comando = f"git remote add {remote_repository} {ssh_repositorio}"
    proceso = run(
        comando,
        capture_output=True,
        text=True,
        shell=True
    )
    
    if proceso.returncode == 0:
        console.print("✅",f"[green]el repositorio remoto {remote_repository} se configuro apropiadamente[/]")
        return proceso
    return False
    #TODO: reaccionar en caso de que no se pueda ejecutar la operacion correctamente.

""" def main_parametros():
    project_location = os.getcwd()
    project_folder = os.path.basename(project_location) # TODO: se puede usar este valor como por defecto, pero se puede dar la oportunidad al usuario de colocarlo con argumentos.
    #TODO: tambien necesita sanisarse el nombre, por si lleva espacios o caracteres especiales.
    
    usuario = ""
    
    iniciar_repositorio_local()
    
    if verificar_gh_login() > 0:
        iniciar_repositorio_github(project_folder)
    #TODO: manejar el ecenario donde existe el repositorio en github
    
    configurar_repositorios_externos(project_folder,usuario)
    
    #TODO: verificar que la rama principal se llame main, si no cambiarle el nombre a main
    
    #TODO: configurar la ruta remota origin al repositorio ssh en github. """
    
def proceso_completo(project_folder,usuario):
    
    iniciar_repositorio_local()
    
    iniciar_repositorio_github(project_folder)
    #TODO: manejar el ecenario donde existe el repositorio en github

    configurar_repositorios_externos(project_folder,usuario)
    
    #TODO: verificar que la rama principal se llame main, si no cambiarle el nombre a main
    
    #TODO: configurar la ruta remota origin al repositorio ssh en github.
    
def __obtener_project_folder_interactivo():
    project_location = os.getcwd()
    project_folder = os.path.basename(project_location)
    #TODO: tambien necesita sanisarse el nombre, por si lleva espacios o caracteres especiales.
    
    pregunta_folder_name = questionary.confirm(
    f"se esta usando el nombre: {project_folder}, para nombrar al repositorio en github, desea usar este nombre o desea usar otro?").ask()
    if pregunta_folder_name == None: exit()
    
    if pregunta_folder_name == False:
        project_folder = questionary.text("que nombre desea usar para nombrar el repositorio en github?").ask()
        if project_folder==None:exit()
    return project_folder

def __obtener_usuario_interactivo():
    if __verificar_gh_login() == False:
        console.print("no se encuentra registrado en github con \"gh\"")
        usuario = questionary.text("que usuario desea usar para configurar como remoto para git remote").ask()
        if usuario == None : exit()
    else:
        usuario = __optener_usuario()
    return usuario
    
def main_interactivo():
    project_folder = __obtener_project_folder_interactivo()
    
    usuario = __obtener_usuario_interactivo()
    
    proceso_completo(project_folder,usuario)
    
    

def main():
    main_interactivo()
    # main_parametros()
if __name__ == "__main__" and __package__ is None:
    __package__ = "crear"
    main()