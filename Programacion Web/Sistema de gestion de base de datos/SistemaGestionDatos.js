let empleados = [];

const form = document.getElementById("formEmpleado");
const tablaBody = document.querySelector("#tablaEmpleados tbody");

// Añadir empleado
form.addEventListener("submit", e => {
    e.preventDefault();

    const empleado = {
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        email: document.getElementById("email").value,
        telefono: document.getElementById("telefono").value,
        salario: document.getElementById("salario").value,
        fechaNacimiento: document.getElementById("fechaNacimiento").value,
        imagen: document.getElementById("imagen").value || "https://via.placeholder.com/50"
    };

    empleados.push(empleado);
    mostrarEmpleados();
    form.reset();
});

// Mostrar empleados
function mostrarEmpleados() {
    tablaBody.innerHTML = "";
    empleados.forEach((emp, i) => {
        let fila = document.createElement("tr");
        fila.innerHTML =` 
            <td><img src="${emp.imagen}" alt="Foto"></td>
            <td>${emp.nombre}</td>
            <td>${emp.apellido}</td>
            <td>${emp.email}</td>
            <td>${emp.telefono}</td>
            <td>${emp.salario}</td>
            <td>${emp.fechaNacimiento}</td>
            <td><button class="eliminar" onclick="eliminarEmpleado(${i})">Eliminar</button></td>`
        ;
        tablaBody.appendChild(fila);
    });
}

// Eliminar empleado
function eliminarEmpleado(i) {
    empleados.splice(i, 1);
    mostrarEmpleados();
}