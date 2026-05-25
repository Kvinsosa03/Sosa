const Button1 = document.getElementById("Button1")
const text = document.getElementById("text")
const mensaje = document.getElementById("mensaje")

function Comprobacion(){

    let palabra = text.value

    if(palabra === "") return

    let invertido = palabra.split("").reverse().join("")

    if(palabra === invertido){
        mostrarMensaje(`Es un Palíndromo, ${text.value};${invertido}`)
    }else {
        mostrarMensaje(`No es un Palíndromo, ${text.value};${invertido}`)
    }

     setTimeout(() => {
        text.value = "";
    }, 3000);
    
}
function mostrarMensaje(texto){
    mensaje.textContent = texto;
    setTimeout(() => {
        mensaje.textContent = "...";
    }, 3000);
}

Button1.addEventListener("click",Comprobacion);