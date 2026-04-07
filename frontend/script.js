const input = document.getElementById("codigoInput");
const respuesta = document.getElementById("respuesta");

let temporizador;

input.addEventListener("input", function() {
    clearTimeout(temporizador);
    temporizador = setTimeout(enviarCodigo, 500);
});

input.focus();
async function enviarCodigo() {
    const codigo = input.value.trim();
    
    if (codigo === "") return;

    const response = await fetch("http://192.168.0.130:8000/escanear", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo: codigo})
    });

    const data = await response.json();
    respuesta.textContent = data.mensaje;
    input.value = "";
    input.focus();
}

async function toggleLogs() {
    const seccion = document.getElementById("seccionLogs");
    const btn = document.getElementById("btnLogs");

    // Verificamos si ya tiene la clase "abierto"
    if (!seccion.classList.contains("abierto")) {
        // 1. Cargamos los datos antes de mostrar (opcional, para que no se vea vacía)
        await cargarDatosTabla();
        
        // 2. Agregamos la clase que dispara la animación
        seccion.classList.add("abierto");
        btn.textContent = "Ocultar Logs";
    } else {
        // 3. Quitamos la clase para que se contraiga
        seccion.classList.remove("abierto");
        btn.textContent = "Ver Logs de Hoy";
    }
}

async function cargarDatosTabla() {
    const cuerpo = document.getElementById("cuerpoTabla");    
    const respuesta = await fetch("http://192.168.0.130:8000/logs");
    const data = await respuesta.json();

    cuerpo.innerHTML = ""; // Limpiamos la tabla por si había datos viejos

    // Recorremos los logs que vienen de la API
    data.logs.forEach(log => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td>${log[0]}</td>
            <td>${log[1]}</td>
            <td>${log[2]}</td>
            <td>${log[3]}</td>
            <td>${log[4]}</td>
            <td>${log[5]}</td>
            <td>${log[6]}</td>
            <td>${log[7]}</td>
        `;
        cuerpo.appendChild(fila);
    });
} 
