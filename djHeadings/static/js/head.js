document.getElementById("id_mark").disabled = true

function check() {
    let mark = document.getElementById("id_mark")
    if (document.getElementById("id_choice_2").checked){
        mark.style.backgroundColor = "white"
        mark.required = true
        mark.disabled = false
    }else{
        mark.required = false
        mark.disabled = true
        mark.style.backgroundColor = "rgb(202, 201, 201)"
    }
};


function copyText() {
    let htmlEditor = document.getElementById("outputHeading");

    let container = document.createElement('div')
    container.innerHTML = htmlEditor.innerHTML
    container.style.position = 'fixed'
    container.style.pointerEvents = 'none'
    container.style.opacity = 0

    document.body.appendChild(container)
    window.getSelection().removeAllRanges()

    let range = document.createRange()
    range.selectNode(container)
    window.getSelection().addRange(range)
    document.execCommand('copy')
    document.body.removeChild(container);

    let  btn = document.getElementById("copy")
    btn.textContent = "Copied !!!"
    btn.style.backgroundColor= "yellow"
    btn.style.color= "black"
};
