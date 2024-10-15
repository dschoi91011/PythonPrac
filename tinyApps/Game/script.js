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