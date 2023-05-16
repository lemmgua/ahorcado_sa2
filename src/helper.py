from wonderwords import RandomWord
from googletrans import Translator

def ConseguirPalabraAleatoria() -> str:
    trans = Translator()
    word = RandomWord()
    rword = word.word()
    del word
    return trans.translate(rword, dest="es").text