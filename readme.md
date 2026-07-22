# 💈 BarberShop — Web con Sistema de Reservas

Sitio web para una barbería con sistema de reservas de citas en tiempo real, desarrollado con HTML, CSS, JavaScript, Flask (Python) y MySQL.

## 🌐 Demo

Página estática funcional con formulario de reservas conectado a base de datos.

## 📋 Funcionalidades

- Landing page responsive con presentación de servicios
- Galería de trabajos
- Sistema de reservas de citas con persistencia en MySQL
- Backend API construido con Flask

## 🧰 Tecnologías utilizadas

**Frontend:**
- HTML5 semántico
- CSS3 (Flexbox, Grid, variables CSS, diseño responsive)
- JavaScript (Fetch API, manejo de eventos, async/await)

**Backend:**
- Python 3 con Flask
- Flask-CORS (comunicación segura entre frontend y backend)
- MySQL (persistencia de datos)
- python-dotenv (manejo seguro de credenciales)

## 📂 Estructura del proyecto
barbershop/
├── index.html
├── app.py
├── .env (no incluido en el repositorio)
├── .gitignore
├── css/
│ └── style.css
├── js/
│ └── script.js
└── readme.md
## 🗄️ Estructura de la base de datos

### Tabla `reservas`

| Campo           | Tipo      | Descripción                          |
|------------------|-----------|---------------------------------------|
| id               | INT       | Identificador único (autoincremental) |
| nombre           | VARCHAR   | Nombre del cliente                    |
| servicio         | VARCHAR   | Servicio seleccionado                 |
| fecha            | DATE      | Fecha de la cita                      |
| hora             | TIME      | Hora de la cita                       |
| fecha_creacion   | DATETIME  | Momento en que se registró la reserva |

## ⚙️ Instalación y configuración

1. Clona el repositorio
2. Instala las dependencias de Python:
```bash
pip install flask flask-cors mysql-connector-python python-dotenv
```
3. Crea una base de datos MySQL con la tabla `reservas` (ver estructura arriba)
4. Crea un archivo `.env` en la raíz del proyecto:
DB_PASSWORD=tu_contraseña_aqui
5. Inicia el servidor backend:
```bash
python app.py
```
6. Abre `index.html` en tu navegador (doble clic o "Abrir con" → tu navegador)

## 🔄 Flujo de la aplicación
Usuario llena formulario → JavaScript (fetch) → Servidor Flask (/reservar) → MySQL
## 🎨 Diseño

Paleta oscura con acentos en tono cobre/dorado, tipografía condensada para títulos. Diseño completamente responsive (funciona en escritorio, tablet y móvil).

## 🚀 Próximas mejoras

- [ ] Validación de disponibilidad de horarios (evitar reservas duplicadas)
- [ ] Panel de administrador para ver todas las reservas
- [ ] Despliegue del frontend en Vercel
- [ ] Migración de imágenes placeholder a fotos reales de la barbería

## Autor

Sebastián David Jiménez Sarmiento — Ingeniero de Sistemas
