from os import system, getcwd, name
from pathlib import Path
from os.path import expanduser
from json import load, dump
from random import choice
from googletrans import Translator
from rich import print

def ConseguirPalabraAleatoria() -> str:
    trans = Translator()
    with open(getcwd()+"\\src\\nounlist.txt", "r") as file:
        rword = choice(file.readlines())
        return trans.translate(rword, dest="es").text

def Clear() -> None:
    system('cls' if name=='nt' else 'clear')

def CargarAjustes() -> dict:
    #Cargar archivo de ajustes JSON
    try:
        file = open(expanduser("~/Documents")+"\\ahorcado_sa2_settings.json", "r")
        data = load(file)
        file.close()
        return data
    except IOError: #Si el archivo no existe, crearlo
        ajustes = {
            "color-scheme": "default",
            "player-name": "XYZ",
            "difficulty": "normal"
        }
        with open((expanduser("~/Documents")+"\\ahorcado_sa2_settings.json"), "w+") as file:
            dump(ajustes, file, indent=4)
        return ajustes

def GuardarAjustes(nuevos_ajustes: dict) -> None:
    with open((expanduser("~/Documents")+"\\ahorcado_sa2_settings.json"), "w") as file:
        dump(nuevos_ajustes, file, indent=4)

def ConseguirEsquemaDeColor(color_scheme: str) -> dict:
    primary_color, secondary_color, third_color = "", "", ""
    if color_scheme == "default":
        primary_color = "#E57C23"
        secondary_color = "#E8AA42"
        third_color = "#068DA9"
    elif color_scheme == "xmas":
        primary_color = "red"
        secondary_color = "green"
        third_color = "white"
    elif color_scheme == "neon":
        primary_color = "#FFD93D"
        secondary_color = "#F266AB"
        third_color = "#2CD3E1"
    elif color_scheme == "gold":
        primary_color = "#FD841F"
        secondary_color = "#FF8400"
        third_color = "#FFE569"
    elif color_scheme == "cold":
        primary_color = "#57C5B6"
        secondary_color = "#159895"
        third_color = "#1A5F7A"

    return {
        "primary": primary_color,
        "secondary": secondary_color,
        "third": third_color
    }

def PulsaEnterParaContinuar() -> None:
    print("[u b i white]Pulsa INTRO para continuar[/u b i white]", end="")
    input()

if __name__ == "__main__":
    print(str(Path(__file__).parent.resolve())+"\\nounlist.txt")
    print(getcwd()+"\\src\\nounlist.txt")
