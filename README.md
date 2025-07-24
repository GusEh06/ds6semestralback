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

## 🏗️ Arquitectura del Sistema

```
parque-nacional-api/
├── 📁 api/                     # Aplicación principal
│   ├── 📄 models.py           # Modelos de datos
│   ├── 📄 serializers.py      # Serializadores API
│   ├── 📄 views.py            # Vistas y endpoints
│   ├── 📄 urls.py             # Configuración de URLs
│   └── 📁 services/           # Lógica de negocio
│       ├── 📄 dashboard_service.py
│       ├── 📄 usuario_service.py
│       └── 📄 sendero_service.py
├── 📁 docs/                   # Documentación
├── 📁 migrations/             # Migraciones de BD
├── 📄 requirements.txt        # Dependencias
└── 📄 .env.example           # Variables de entorno
```

---

### 🗂️ Índice de Documentación

| Sección | Descripción | Enlace |
|---------|-------------|--------|
| 📊 **Dashboard API** | Endpoints para estadísticas y reportes | [📄 Dashboard](docs/dashboard.md) |


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
**Versión:** 1.0