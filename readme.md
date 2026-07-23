💈 BarberShop — Web con Sistema de Reservas y Panel de Administrador

Sitio web para una barbería con sistema de reservas de citas en tiempo real, cuentas de cliente, y panel de administrador, desarrollado con HTML, CSS, JavaScript, Flask (Python) y MySQL.

🌐 Demo
Sitio completo servido por Flask, con registro/login de clientes, reservas conectadas a base de datos, y panel de administrador protegido con contraseña.

📋 Funcionalidades
- Landing page responsive con presentación de servicios
- Galería de trabajos
- Registro e inicio de sesión de clientes (contraseñas encriptadas)
- Sistema de reservas de citas con persistencia en MySQL, disponible solo para clientes con sesión iniciada
- Panel de administrador protegido con contraseña, para visualizar todas las reservas
- Backend API construido con Flask

🧰 Tecnologías utilizadas

Frontend:
- HTML5 semántico + plantillas Jinja2
- CSS3 (Flexbox, Grid, variables CSS, sistema de espaciado, diseño responsive)
- Tipografía: Playfair Display (títulos) + Inter (texto), vía Google Fonts
- JavaScript (Fetch API, manejo de eventos, async/await)

Backend:
- Python 3 con Flask
- Flask sessions (autenticación de clientes y administrador)
- Werkzeug security (hash de contraseñas)
- Flask-CORS
- MySQL (persistencia de datos)
- python-dotenv (manejo seguro de credenciales)

📂 Estructura del proyecto
barbershop/
├── templates/
│ ├── index.html
│ ├── admin.html
│ ├── login.html
│ ├── registro.html
│ └── cuenta_login.html
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
├── app.py
├── .env (no incluido en el repositorio)
├── .gitignore
└── readme.md
🗄️ Estructura de la base de datos

Tabla `reservas`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INT | Identificador único (autoincremental) |
| nombre | VARCHAR | Nombre del cliente (tomado de su cuenta) |
| servicio | VARCHAR | Servicio seleccionado |
| fecha | DATE | Fecha de la cita |
| hora | TIME | Hora de la cita |
| fecha_creacion | DATETIME | Momento en que se registró la reserva |

Tabla `usuarios`
| Campo | Tipo | Descripción |
|---|---|---|
| id | INT | Identificador único (autoincremental) |
| nombre | VARCHAR | Nombre completo del cliente |
| correo | VARCHAR | Correo electrónico (único) |
| password_hash | VARCHAR | Contraseña encriptada (nunca se guarda en texto plano) |
| fecha_registro | DATETIME | Momento del registro |

⚙️ Instalación y configuración
1. Clona el repositorio
2. Instala las dependencias de Python:
pip install flask flask-cors mysql-connector-python python-dotenv
3. Crea una base de datos MySQL con las tablas `reservas` y `usuarios` (ver estructuras arriba)
4. Crea un archivo `.env` en la raíz del proyecto:
DB_PASSWORD=tu_contraseña_de_mysql
ADMIN_PASSWORD=tu_contraseña_de_administrador
SECRET_KEY=una_cadena_larga_y_aleatoria
5. Inicia el servidor:
python app.py
6. Abre `http://127.0.0.1:5000/` en tu navegador (el sitio ya se sirve completo desde Flask)

🔄 Flujo de la aplicación
- **Registro/login:** Cliente completa formulario → Flask valida/crea cuenta en MySQL → sesión iniciada
- **Reserva:** Cliente con sesión activa llena el formulario → JavaScript (fetch) → Flask (`/reservar`, protegido) → MySQL
- **Panel de administrador:** Ruta `/admin` protegida por sesión de administrador (`/login`) → consulta todas las reservas en MySQL → se muestran en tabla

🔐 Seguridad
- Contraseñas de clientes encriptadas con hash (Werkzeug), nunca almacenadas en texto plano
- Panel de administrador protegido por contraseña independiente, no enlazado desde el menú público
- Credenciales sensibles (`DB_PASSWORD`, `ADMIN_PASSWORD`, `SECRET_KEY`) fuera del control de versiones vía `.env` + `.gitignore`

🎨 Diseño
Paleta oscura con acentos en tono cobre/dorado. Tipografía Playfair Display para títulos e Inter para texto, sistema de espaciado consistente, encabezado fijo (sticky) al hacer scroll. Diseño completamente responsive (funciona en escritorio, tablet y móvil).

🚀 Próximas mejoras
- [ ] Validación de disponibilidad de horarios (evitar reservas duplicadas)
- [ ] Cancelar/eliminar reservas desde el panel de administrador
- [ ] Historial de reservas por cliente en su propia cuenta
- [ ] Despliegue del proyecto (frontend + backend) en un servicio como Render o Railway
- [ ] Migración de imágenes placeholder a fotos reales de la barbería

Autor
Sebastián David Jiménez Sarmiento — Ingeniero de Sistemas