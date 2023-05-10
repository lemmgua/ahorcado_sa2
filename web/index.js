const playBttn = document.getElementById("playBttn");
const mainWord = document.getElementById("mainWord");

playBttn.addEventListener("click", async () => {
    mainWord.innerText = await eel.ConseguirPalabraAleatoria()();
});

const keyboardBttns = document.querySelectorAll(".key-bttn");

let letrasAdivinadas = [];
let dataWord;

function ManejarEntrada(key) {
    if (dataWord.includes(key)) {
        letrasAdivinadas.push(key);
    }
}

function EscribirPalabra() {
    for (let i = 0; i < dataWord.length; i++) {
        let gameWord = "";
        if (letrasAdivinadas.includes(dataWord[i])) {
            gameWord += dataWord[i];
        }
        else {
            gameWord += "_";
        }
    }
    return gameWord;
}

keyboardBttns.forEach(e => e.addEventListener(() => ManejarEntrada(e.innerText)));
