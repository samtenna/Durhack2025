const Toggle = (id) => {
    let cl = document.querySelectorAll(".textbox")
    cl.forEach(element => {
        element.innerHTML = ""
    })
    
    const content = document.getElementById(`${id}-textbox`);
    if (content.innerHTML) {
        content.innerHTML = "";
    }    
}