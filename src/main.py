import eel
from wonderwords import RandomWord
from googletrans import Translator

eel.init("web")

@eel.expose
def ConseguirPalabraAleatoria() -> str:
    trans = Translator()
    word = RandomWord()
    rword = word.word()
    del word
    return trans.translate(rword, dest="es").text

eel.start("index.html", size=(800, 600))