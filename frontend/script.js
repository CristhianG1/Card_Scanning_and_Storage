const input = document.getElementById("codigoInput");
const respuesta = document.getElementById("respuesta");

let temporizador;

input.addEventListener("input", function() {
    clearTimeout(temporizador);
    temporizador = setTimeout(enviarCodigo, 250);
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