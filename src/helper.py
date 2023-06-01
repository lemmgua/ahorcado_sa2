import os, json
from wonderwords import RandomWord
from googletrans import Translator
from rich import print

def ConseguirPalabraAleatoria() -> str:
    trans = Translator()
    word = RandomWord()
    rword = word.word()
    del word
    return trans.translate(rword, dest="es").text

def Clear() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

from os.path import expanduser

def CargarAjustes() -> dict:
    #Cargar archivo de ajustes JSON
    try:
        file = open(expanduser("~/Documents")+"\\ahorcado_sa2_settings.json", "r")
        data = json.load(file)
        file.close()
        return data
    except IOError: #Si el archivo no existe, crearlo
        ajustes = {
            "color-scheme": "default",
            "player-name": "XYZ",
            "difficulty": "normal"
        }
        with open((expanduser("~/Documents")+"\\ahorcado_sa2_settings.json"), "w+") as file:
            json.dump(ajustes, file, indent=4)
        return ajustes

def GuardarAjustes(nuevos_ajustes: dict) -> None:
    with open((expanduser("~/Documents")+"\\ahorcado_sa2_settings.json"), "w") as file:
        json.dump(nuevos_ajustes, file, indent=4)

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
