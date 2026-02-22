# Gestor de Tareas | Framework Django (JWT & Docker)

API REST para la gestión de tareas, construida con **Django**, **Django Rest Framework (DRF)**, **PostgreSQL**, y **Docker**.

## ✨ Características
- **Autenticación JWT:** Seguridad mediante JSON Web Tokens.
- **Gestión de Tareas:** CRUD completo de tareas con dueño.
- **Privacidad:** Los usuarios solo pueden ver, editar o eliminar sus propias tareas.
- **Dockerizado:** Configuración lista para desarrollo

## 🛠️ Stack Tecnológico
- **Backend:** Django 4.2+ & Django Rest Framework.
- **Base de Datos:** PostgreSQL.
- **Autenticación:** SimpleJWT.
- **Contenedores:** Docker & Docker Compose.

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/jfrancca/Tareas.git
cd tareas
```

### 2. Levantar con Docker
```bash
docker-compose up --build
El servidor estará disponible en: http://localhost:8000
```

### 3. Ejecutar Migraciones
```bash
docker-compose exec web python manage.py migrate

