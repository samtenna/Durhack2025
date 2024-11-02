const Toggle = (id) => {
    const content = document.getElementById(`${id}-textbox`);
    if (content.innerHTML) {
        content.innerHTML = "";
    }    
}