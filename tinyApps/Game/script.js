const gameLevels = ['easy', 'medium', 'hard', 'beast'];

const generateGame = () => {
    const canv = document.createElement('canvas');
    canv.id = 'game';
    canv.height = '500';
    canv.width = '500';
    canv.style.border = '5px solid #C0D72D'; // Customize as needed
    canv.style.background = '#000000';

    posX = posY = 10;
    appleX = appleY = 15;
    gridSize = 20;
    tableSize = 25;

    moveX = moveY = 0;
    body = [];
    segments = 5;

    score = 0;
    level = 100;

    const ctx = canv.getContext('2d');

    // Append canvas to display area
    display.append(canv);
};

const keyDown = e => {
    switch (e.keyCode) {
        case 65: // Left (A)
            moveX = -1;
            moveY = 0;
            break;
        case 87: // Up (W)
            moveX = 0;
            moveY = -1;
            break;
        case 68: // Right (D)
            moveX = 1;
            moveY = 0;
            break;
        case 83: // Down (S)
            moveX = 0;
            moveY = 1;
            break;
    }
};

document.addEventListener('keydown', keyDown);

const game = () => {
    // Update snake's position based on the direction of movement
    posX += moveX;
    posY += moveY;

    // Clear the canvas
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, canv.width, canv.height);

    // Draw the snake
    ctx.fillStyle = '#2ED9EB';

    // Handle edge wrapping (snake reappears on the opposite side of the canvas)
    if (posX < 0) posX = tableSize - 1;
    if (posX > tableSize - 1) posX = 0;
    if (posY < 0) posY = tableSize - 1;
    if (posY > tableSize - 1) posY = 0;

    // Check for self-collision
    for (let i = 0; i < body.length; i++) {
        ctx.fillRect(body[i].x * gridSize, body[i].y * gridSize, gridSize - 2, gridSize - 2);

        // If the snake's head touches its body, reset the game
        if (body[i].x === posX && body[i].y === posY) {
            segments = 5;  // Reset snake length
            score = 0;     // Reset score
        }
    }

    // Move the snake forward (add new position to the body)
    body.push({ x: posX, y: posY });

    // Remove the tail to keep the snake the right length
    while (body.length > segments) {
        body.shift(); // Remove the oldest segment (tail)
    }

    // Check if the snake has eaten the apple
    if (appleX === posX && appleY === posY) {
        score++;  // Increase score
        segments++;  // Make the snake longer
        // Move the apple to a new random position
        appleX = Math.floor(Math.random() * tableSize);
        appleY = Math.floor(Math.random() * tableSize);
    }

    // Draw the apple
    ctx.fillStyle = "#E91E63";
    ctx.fillRect(appleX * gridSize, appleY * gridSize, gridSize - 2, gridSize - 2);

    // Display score
    ctx.font = "20px Courier New";
    ctx.fillStyle = '#C0D72D';
    ctx.fillText(`Score: ${score}`, 380, 20);

    // Display control instructions
    ctx.fillText(`ᐊA ᐃW Sᐁ Dᐅ`, 180, 495);

    // Continuously call the game function based on the selected level speed
    setTimeout(game, level);
};

const setLevel = selection => {
    options.childNodes.forEach(option => {
        option.style.color = option.innerHTML === selection ? '#C0D72D' : '#000000';
    });

    switch (selection) {
        case 'easy':
            level = 180;
            break;
        case 'medium':
            level = 120;
            break;
        case 'hard':
            level = 85;
            break;
        case 'beast':
            level = 25;
            break;
        default:
            level = 150;
            break;
    }
};

gameLevels.forEach(lev => {
    const button = document.createElement('button');
    button.innerHTML = lev;
    button.onclick = () => setLevel(lev);
    options.append(button);
});