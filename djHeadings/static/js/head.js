document.getElementById("id_mark").disabled = true

document.getElementById("id_choice").addEventListener("click", check)
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

const copy = document.getElementById("copy")
if (copy) {
    copy.addEventListener("click", copyText)
}
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

    function buttonUpdate(text, background, textColor){
        let  btn = document.getElementById("copy")
        btn.textContent = text
        btn.style.backgroundColor= background
        btn.style.color= textColor
    }
    buttonUpdate("Copied !!!", "yellow", "black")

    setTimeout( () => {
        buttonUpdate("Copy", "black", "white")
    }, 4000)
};


const formValue = JSON.parse(document.getElementById('formDataDict').textContent);
// console.log(formValue)
document.getElementById("id_url").value = formValue.url? formValue.url: ''
document.getElementById("id_mark").value = formValue.mark? formValue.mark: ''
selectChoice(formValue.choice)

function selectChoice(choice) {
    // console.log(choice)
    if ("ol" === choice){
        document.getElementById("id_choice_0").checked = true
    }else if ("ul" === choice){
        document.getElementById("id_choice_1").checked = true
    }else if ("p" === choice){
        document.getElementById("id_choice_2").checked = true
    }
}
