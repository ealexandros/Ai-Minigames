function snakeGameBoardLogic(){
    let nextMove = calculateNextMovePosition(snakeCoordinates[1][0], snakeCoordinates[1][1]);
    let collision = calculateSnakeCollision(nextMove[0], nextMove[1]);
    if (collision) return true;

    let foodCollision = calculateSnakeFoodCollision(nextMove[0], nextMove[1]);
    if (!foodCollision) board[nextMove[0]][nextMove[1]] = SNAKE_LENGHT;

    board[snakeCoordinates[0][0]][snakeCoordinates[0][1]] = 0;
    snakeCoordinates[0] = [snakeCoordinates[1][0], snakeCoordinates[1][1]];
    snakeCoordinates[1] = [nextMove[0], nextMove[1]];
    return false;
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
    if(snakeCoordinates[0][0] == i && snakeCoordinates[0][1] == j) return true;

    return false;
}

function calculateSnakeFoodCollision(i, j){
    if (board[i][j] == -1) {
        score = score + 1;
        board[i][j] = SNAKE_LENGHT;
        addRandomFoodPosition();
        changeScoreboard();
        return true;
    }
    return false;
}

function restartGame() {
    board = new Array(TABLE_SIZE).fill(0).map(() => new Array(TABLE_SIZE).fill(0));
    epsilon = epsilon*EPS_DECAY;
    move = 0; score = 0;
    snakeCoordinates = [[3, 3], [4, 3]];
    setDotGameBoard();
}

function setDotGameBoard(){
    for(i=3;i<5;i++)
        board[i][3] = i-1;
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