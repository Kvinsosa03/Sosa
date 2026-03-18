let datos = [];
let ordenAsc = true;
let editIndex = null; // índice del elemento que se está editando

const formulario = document.getElementById("formulario");
const tablaBody = document.querySelector("#tabla tbody");
const filtro = document.getElementById("filtro");

// Añadir o guardar elemento
formulario.addEventListener("submit", e => {
    e.preventDefault();
    const nombre = document.getElementById("nombre").value;
    const categoria = document.getElementById("categoria").value;
    const anio = document.getElementById("anio").value;

    if (editIndex !== null) {
        // Guardar cambios en edición
        datos[editIndex] = { nombre, categoria, anio };
        editIndex = null;
    } else {
        // Añadir nuevo elemento
        datos.push({ nombre, categoria, anio });
    }

    mostrarTabla();
    formulario.reset();
});

// Mostrar tabla
function mostrarTabla() {
    tablaBody.innerHTML = "";
    let filtrados = datos
        .map((d, i) => ({ ...d, index: i }))
        .filter(d => d.nombre.toLowerCase().includes(filtro.value.toLowerCase()));

    filtrados.forEach(d => {
        let fila = document.createElement("tr");
        fila.innerHTML = 
            `<td>${d.nombre}</td>
            <td>${d.categoria}</td>
            <td>${d.anio}</td>
            <td class="acciones"></td>`;

        const acciones = fila.querySelector(".acciones");

        const btnEditar = document.createElement("button");
        btnEditar.textContent = "Editar";
        btnEditar.addEventListener("click", () => editar(d.index));

        const btnEliminar = document.createElement("button");
        btnEliminar.textContent = "Eliminar";
        btnEliminar.addEventListener("click", () => eliminar(d.index));

        acciones.appendChild(btnEditar);
        acciones.appendChild(btnEliminar);

        tablaBody.appendChild(fila);
    });
}

// Eliminar
function eliminar(i) {
    datos.splice(i, 1);
    mostrarTabla();
}

// Editar usando el formulario
function editar(i) {
    const elemento = datos[i];
    document.getElementById("nombre").value = elemento.nombre;
    document.getElementById("categoria").value = elemento.categoria;
    document.getElementById("anio").value = elemento.anio;
    editIndex = i; // guardamos el índice para saber que estamos editando
}
    // Filtrar
filtro.addEventListener("input", mostrarTabla);

// Ordenar
document.querySelectorAll("#tabla th[data-campo]").forEach(th => {
    th.addEventListener("click", () => {
        const campo = th.getAttribute("data-campo");
        datos.sort((a, b) => {
            if (a[campo] < b[campo]) return ordenAsc ? -1 : 1;
            if (a[campo] > b[campo]) return ordenAsc ? 1 : -1;
            return 0;
        });
        ordenAsc = !ordenAsc;
        mostrarTabla();
    });
});