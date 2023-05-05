import eel
from wonderwords import RandomWord
from googletrans import Translator

@eel.expose
def ConseguirPalabraAleatoria() -> str:
    trans = Translator()
    word = RandomWord()
    rword = word.word()
    del trans
    del word
    return trans.translate(rword, dest="es")

