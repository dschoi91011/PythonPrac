const generateArt = () => {
    const canv = document.createElement('canvas');
    canv.id = 'art';
    canv.height = '500';
    canv.width = '500';
    canv.style.border = '5px solid #FF66FF'; // Customize as needed
    canv.style.background = '#000000';

    const ctx = canv.getContext("2d");
    display.append(canv);
};

for (let x = 0; x < 255; x++) {
    for (let y = 0; y < 255; y++) {
        if ((x ^ y) % 10) {  // Applying XOR and modulus to generate patterns
            ctx.fillStyle = `rgb(${(x ^ y) % 210}, ${y}, ${x})`; // Dynamic color
            ctx.fillRect(x * ((x ^ y) % 10), y * ((x ^ y) % 10), x, y); // Dynamic size and position
        }
    }
};

