function snakeGameBoardLogic(){
    let nextMove = calculateNextMovePosition(snakeCoordinates[0], snakeCoordinates[1]);
    let collision = calculateSnakeCollision(nextMove[0], nextMove[1]);
    if (collision) return true;

    let foodCollision = calculateSnakeFoodCollision(nextMove[0], nextMove[1]);
    if (!foodCollision) board[nextMove[0]][nextMove[1]] = snakeLenght+1;

    removeUnnessassaryTail();
    snakeCoordinates = [nextMove[0], nextMove[1]];
    return false;
}

function removeUnnessassaryTail() {
    for(i=0;i<TABLE_SIZE;i++)
        for(j=0;j<TABLE_SIZE;j++)
            if (board[i][j] > 0)
                board[i][j] -= 1;
}

function calculateNextMovePosition(i, j) {
    if (move == 3) {
        return [i, j-1];
    } else if (move == 2) {
        return [i, j+1];
    }else if (move == 1) {
        return [i-1, j];
    }else if (move == 0) {
        return [i+1, j];
    }
}

function calculateSnakeCollision(i, j) {
    if(i > TABLE_SIZE-1 || i < 0 || j > TABLE_SIZE-1 || j < 0) return true;
    if(board[i][j] > 0) return true;

    return false;
}

function calculateSnakeFoodCollision(i, j){
    if (board[i][j] == -1) {
        snakeLenght = snakeLenght + 1;
        board[i][j] = snakeLenght;
        addRandomFoodPosition();
        changeScoreboard();
        return true;
    }
    return false;
}

function restartGame() {
    board = new Array(TABLE_SIZE).fill(0).map(() => new Array(TABLE_SIZE).fill(0));
    move = 0; snakeLenght = 3;
    snakeCoordinates = [3, 3];
    setDotGameBoard();
}

function setDotGameBoard(){
    for(i=1;i<4;i++)
        board[i][3] = i;
    changeScoreboard();
    addRandomFoodPosition();
}

function addRandomFoodPosition(){
    let food = [Math.floor(Math.random() * TABLE_SIZE), Math.floor(Math.random() * TABLE_SIZE)];
    while(board[food[0]][food[1]] > 0){
        food = [Math.floor(Math.random() * TABLE_SIZE), Math.floor(Math.random() * TABLE_SIZE)];
    }
    board[food[0]][food[1]] = -1;
    foodCoordinates = [food[0], food[1]];
}