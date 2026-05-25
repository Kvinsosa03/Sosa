const Button1 = document.getElementById("Button1")
const Email = document.getElementById("email")
const Mensaje = document.getElementById("mensaje")
const Lista = document.getElementById("list")

function addTask() {

    const newElement = document.createElement("li")
    newElement.textContent = Email.value

    Lista.appendChild(newElement)
}

Button1.addEventListener("click",() => {

    if(Email.value === "") return

    if(Email.value.includes("@") && Email.value.endsWith(".com")){
        Mensaje.textContent = `Correo electronico valido: ${Email.value}`
        addTask()
        Email.value = ""
    }else{
        Mensaje.textContent = `Error: Correo electronico incorrecto. Verifique que utilice "@" y ".com"`
    }
})
