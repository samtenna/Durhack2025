const Toggle = (id) => {
    let cl = document.querySelectorAll(".textbox")
    cl.forEach(element => {
        if (element.id !== `${id}-textbox`) {
            element.innerHTML = ""
        }
    })
    
    const content = document.getElementById(`${id}-textbox`);

    if (id === "scotland" && !(content.innerHTML)) {
        var audio = new Audio('https://www.bagpipes-and-celtic-music.com/Scotland%20the%20Brave.mp3');
        audio.play();
        setTimeout(function() {
            audio.pause();
            audio.currentTime = 0;
        }, 9000);
    }
    if (id === "ni" && !(content.innerHTML)) {
        var audio = new Audio('https://www.bagpipes-and-celtic-music.com/Danny%20Boy%20-%20WHISTLE%20-%202015_5_31_16_1.mp3');
        audio.play();
        setTimeout(function() {
            audio.pause();
            audio.currentTime = 0;
        }, 9000);
    }
    if (id === "london" && !(content.innerHTML)) {
        var audio = new Audio('https://archive.org/details/MrBrightside');
        audio.play();
        setTimeout(function() {
            audio.pause();
            audio.currentTime = 0;
        }, 9000);
    }
    if (content.innerHTML) {
        content.innerHTML = "";
    }    
}