function findMaxArgMax(array) {
    argmax = 0;
    max = array[0];
    for(let i=1;i<array.length;i++) {
        if (array[i] > max) {
            max = array[i];
            argmax = i;
        }
    }
    return [argmax, max];
}

function changeScoreboard() {
    document.getElementById("score").innerHTML = `Your score is: ${score}`
    if (bestScore < score) {
        document.getElementById("bestScore").innerHTML = `Your high score is: ${score}`
        bestScore = score
    }
}