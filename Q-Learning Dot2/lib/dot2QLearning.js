function dotTrainingPhase() {
    for(let i=0;i<EPOCHS;i++) {
        obs = calculateNextMove();
        collision = snakeGameBoardLogic();
        
        reward = calculateNextMoveReward();
        calculateTheQTableError(snakeCoordinates, reward, obs);
        if (collision) restartGame();
    }
}

function calculateNextMove() {
    obs = [[snakeCoordinates[1][0] - foodCoordinates[0], snakeCoordinates[1][0] - foodCoordinates[1], [snakeCoordinates[1][0] - snakeCoordinates[0][0], snakeCoordinates[1][1] - snakeCoordinates[0][1]]]];
    if(Math.random() > epsilon) {
        move = findMaxArgMax(q_table[obs])[0];
    } else {
        move = Math.floor(Math.random()*10)%4;
    }
    return obs;
}

function calculateNextMoveReward() {
    let reward = -MOVE_PENALTY;
    if ((snakeCoordinates[1][0] == foodCoordinates[0]) && (snakeCoordinates[1][1] == foodCoordinates[1])) {
        reward = FOOD_REWARD;
    } else if ((snakeCoordinates[1][0] == snakeCoordinates[0][0]) && (snakeCoordinates[1][1] == snakeCoordinates[0][1])) {
        reward = -SELF_COLLISION_PENALTY;
    } else if (collision) {
        reward = -COLLISION_PENALTY;
    }
    return reward;
}

function calculateTheQTableError(oldPosition, reward, obs) {
    new_obs = [[oldPosition[1][0] - foodCoordinates[0], oldPosition[1][0] - foodCoordinates[1], [oldPosition[1][0] - oldPosition[0][0], oldPosition[1][1] - oldPosition[0][1]]]];

    max_future_q = findMaxArgMax(q_table[new_obs])[1];
    current_q = q_table[obs][move];

    let new_q = 0;
    if (reward == FOOD_REWARD) {
        new_q = FOOD_REWARD
    } else {
        new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount * max_future_q);
    }
    q_table[obs][move] = new_q;
}

function createQTable() {
    for(let x1=-TABLE_SIZE+1; x1<TABLE_SIZE; x1++)
        for(let y1=-TABLE_SIZE+1; y1<TABLE_SIZE; y1++)
            for(let x2=-TABLE_SIZE+1; x2<TABLE_SIZE; x2++)
                for(let y2=-TABLE_SIZE+1; y2<TABLE_SIZE; y2++)
                        q_table[[[x1, y1], [x2, y2]]] = [Math.random()*5%5, Math.random()*5%5, Math.random()*5%5, Math.random()*5%5];
}