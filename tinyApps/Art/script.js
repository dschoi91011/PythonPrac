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