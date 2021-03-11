function changeScoreboard() {
    document.getElementById("score").innerHTML = `Your score is: ${snakeLenght}`;
    if (bestScore < snakeLenght) {
        document.getElementById("bestScore").innerHTML = `Your high score is: ${snakeLenght}`;
        bestScore = snakeLenght;
    }
}