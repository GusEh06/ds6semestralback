# 🌿 Sistema de Gestión - Parque Nacional Camino de Cruces

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-REST-orange.svg)](https://restframework.djangorest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción del Proyecto

Sistema web integral para la gestión de visitantes, senderos y análisis estadístico del Parque Nacional Camino de Cruces. Incluye funcionalidades de registro de visitantes, encuestas de satisfacción, dashboard administrativo y gestión de senderos con sus respectivas fotografías.
## Información General

**Base URL:** `http://localhost:8000/api/dashboard/`  
**Formato de respuesta:** JSON  
**Método de autenticación:** Pendiente de implementar


---

---
## 🏗️ Arquitectura del Sistema
```
proyecto-api/
├── 📁 api/                          # Aplicación principal Django
│   ├── 📁 migrations/               # Migraciones de base de datos
│   ├── 📁 services/                 # Capa de servicios (lógica de negocio)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 comentario_service.py  # Gestión de comentarios
│   │   ├── 📄 dashboard_service.py   # Métricas y dashboard
│   │   ├── 📄 foto_sendero_service.py # Management de fotos
│   │   ├── 📄 sendero_service.py     # Lógica de senderos
│   │   ├── 📄 usuario_service.py     # Gestión de usuarios
│   │   └── 📄 valoracion_service.py  # Sistema de valoraciones
│   ├── 📄 __init__.py
│   ├── 📄 admin.py                  # Configuración admin Django
│   ├── 📄 apps.py                   # Configuración de la app
│   ├── 📄 models.py                 # Modelos de datos (ORM)
│   ├── 📄 serializers.py            # Serializadores DRF
│   ├── 📄 tests.py                  # Tests unitarios
│   ├── 📄 urls.py                   # Rutas de la API
│   └── 📄 views.py                  # Vistas y endpoints
├── 📁 docs/                         # Documentación del proyecto
│   └── 📄 dashboard.md              # Documentación del dashboard
├── 📁 parque_api/                   # Configuración principal del proyecto
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py                   # Configuración ASGI
│   ├── 📄 settings.py               # Configuración Django
│   ├── 📄 urls.py                   # URLs principales
│   └── 📄 wsgi.py                   # Configuración WSGI
├── 📄 .gitignore                    # Archivos ignorados por Git
├── 📄 README.md                     # Documentación principal
├── 📄 manage.py                     # Script de gestión Django
└── 📄 requirements.txt              # Dependencias del proyecto
```
---

### 🗂️ Índice de Documentación

| Sección | Descripción | Enlace |
|---------|-------------|--------|
| 📊 **Dashboard API** | Endpoints para estadísticas y reportes | [📄 Dashboard](docs/dashboard.md) |
| 📊 **Registro-Visita API** | Endpoints para visitantes y registro de visitantes | [📄 RegistroVisitante](docs/registro_visita.md) |

---
## 🌐 API Endpoints

### 📊 Dashboard (Estadísticas)
```
GET /api/dashboard/visitas-recientes/     # Últimas visitas
GET /api/dashboard/visitantes-hoy/        # Conteo diario
GET /api/dashboard/encuestas-hoy/         # Encuestas completadas
GET /api/dashboard/visitantes-por-pais/   # Estadísticas geográficas
GET /api/dashboard/visitantes-por-sendero/ # Popularidad de rutas
```

---
**Última actualización:** Julio 2025  
**Versión:** 1.0.
