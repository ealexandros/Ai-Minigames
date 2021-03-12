function snakeGameBoardLogic() {
    let nextMove = findNextMovePosition();
    let collisionDetected = checkForSnakeCollisions(nextMove[0], nextMove[1]);
    if (collisionDetected) {
        return true;
    }

    let foodCollision = checkForFoodCollision(nextMove[0], nextMove[1]);
    if (!foodCollision) board[nextMove[0]][nextMove[1]] = 1;

    board[snake_coordinates[0]][snake_coordinates[1]] = 0;
    snake_coordinates = [nextMove[0], nextMove[1]];
    return false;
}

function findNextMovePosition() {
    if(move == 3){
        return [snake_coordinates[0], snake_coordinates[1]-1];
    }else if(move == 2){
        return [snake_coordinates[0], snake_coordinates[1]+1];
    }else if(move == 1){
        return [snake_coordinates[0]-1, snake_coordinates[1]];
    }else if(move == 0){
        return [snake_coordinates[0]+1, snake_coordinates[1]];
    }
}

function checkForSnakeCollisions(i, j) {
    if(i > (MAP/DOT_SIZE)-1 || i < 0 || j > (MAP/DOT_SIZE)-1 || j < 0)
        return true;
    return false;
}

function checkForFoodCollision(i, j) {
    if(board[i][j] == -1) {
        score = score + 1;
        board[i][j] = 1;
        changeScoreboard();
        addRandomFoodPosition();
        return true;
    }
    return false;
}

function restartGame() {
    board = new Array(MAP/DOT_SIZE).fill(0).map(() => new Array(MAP/DOT_SIZE).fill(0));
    epsilon = epsilon*EPS_DECAY
    score = 0;
    changeScoreboard();
    setDotGameBoard();
}

function changeScoreboard() {
    document.getElementById("score").innerHTML = `Your score is: ${score}`
    if (best_score < score) {
        document.getElementById("bestScore").innerHTML = `Your high score is: ${score}`
        best_score = score
    }
}

function setDotGameBoard() {
    snake_coordinates = [3, 3];
    board[snake_coordinates[0]][snake_coordinates[1]] = 1;
    addRandomFoodPosition();
}

function addRandomFoodPosition() {
    let food = [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10)];
    while(board[food[0]][food[1]] > 0){
        food = [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10)];
    }
    board[food[0]][food[1]] = -1;
    food_coordinates = [food[0], food[1]];
}
