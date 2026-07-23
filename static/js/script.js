document.addEventListener('DOMContentLoaded', function () {

    const formulario = document.getElementById('formularioCita');

    formulario.addEventListener('submit', async function (evento) {
        evento.preventDefault();

        const servicio = document.getElementById('servicio').value;
        const fecha = document.getElementById('fecha').value;
        const hora = document.getElementById('hora').value;

        try {
            const respuesta = await fetch('/reservar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ servicio, fecha, hora })
            });

            if (respuesta.ok) {
                alert(`¡Reserva confirmada!\n\nServicio: ${servicio}\nFecha: ${fecha}\nHora: ${hora}`);
                formulario.reset();
            } else if (respuesta.status === 401) {
                alert('Debes iniciar sesión para reservar una cita.');
                window.location.href = '/cuenta/login';
            } else {
                alert('Hubo un error al guardar la reserva. Intenta de nuevo.');
            }
        } catch (error) {
            console.error('Error de conexión:', error);
            alert('No se pudo conectar con el servidor. ¿Está corriendo app.py?');
        }
    });

});