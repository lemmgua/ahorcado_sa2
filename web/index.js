const playBttn = document.getElementById("playBttn");
const mainWord = document.getElementById("mainWord");

playBttn.addEventListener("click", async () => {
    mainWord.innerText = await eel.ConseguirPalabraAleatoria()();
});