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
import os
from util.mesagges import keyboard_interrupt,exito

def main():
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    acciones = ["descargar video youtube"]
    main_questionary = select("que quieres descargar",choices=acciones).ask()
    if main_questionary == None:
        keyboard_interrupt()
    for act in acciones:
        if main_questionary == act:
            
    

if __name__ == "__main__":
    main()