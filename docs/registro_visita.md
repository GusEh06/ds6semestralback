# Registro de Visitas - Parque Nacional Camino de Cruces

## 📝 Endpoints de Registro de Visitas

### 1. Registrar Visitante Nuevo y su Visita

**POST** `/api/registrar_visitante_y_visita/`

Permite registrar a un visitante nuevo en el sistema junto con su primera visita. Los datos sensibles del visitante (nombre, cédula, teléfono, etc.) se guardan encriptados.

#### Cuerpo de Petición (JSON)

```json
{
  "visitante": {
    "cedula_pasaporte": "A123456789",
    "nombre_visitante": "Ana Ruiz",
    "nacionalidad": "Panameña",
    "adulto_nino": "Adulto",
    "telefono": "60000000",
    "genero": "Femenino"
  },
  "visita": {
    "motivo": "Turismo ecológico",
    "sendero": 1
  }
}
```

#### Respuesta Exitosa (201 Created)

```json
{
  "mensaje": "Visitante y visita registrados exitosamente"
}
```

#### Errores Comunes

```json
{
  "error": "Faltan campos obligatorios",
  "detalle": "No se proporcionó el campo 'telefono'"
}
```

---

### 2. Registrar Visita para Visitante Existente

**POST** `/api/registrar_visita_existente/`

Registra una nueva visita de un visitante ya existente (identificado por su cédula o pasaporte).

#### Cuerpo de Petición (JSON)

```json
{
  "cedula": "A123456789",
  "motivo": "Educativo",
  "sendero": 1
}
```

#### Respuesta Exitosa (201 Created)

```json
{
  "mensaje": "Visita registrada exitosamente"
}
```

#### Errores Comunes

```json
{
  "error": "Visitante no encontrado"
}
```

```json
{
  "error": "Token de desencriptación inválido",
  "detalle": "La clave de encriptación configurada no coincide con los datos existentes"
}
```

---

### 3. Consultar Nombre del Visitante

**GET** `/api/obtener_nombre_visitante/?cedula=A123456789`

Retorna el nombre desencriptado del visitante correspondiente a la cédula proporcionada.

#### Respuesta Exitosa (200 OK)

```json
{
  "nombre": "Ana Ruiz"
}
```

#### Respuesta de Error (404)

```json
{
  "error": "Visitante no encontrado"
}
```

---

### 4. Listar Senderos Disponibles

**GET** `/api/listar_senderos_simplificado/`

Retorna una lista de senderos activos con su `id` y `nombre` para ser usados en el frontend (combobox, select, etc.).

#### Respuesta Exitosa (200 OK)

```json
[
  { "id": 1, "nombre": "Sendero Las Cruces" },
  { "id": 2, "nombre": "Sendero El Charco" }
]
```

---

## 🔧 Notas Técnicas Importantes

- Los campos sensibles se guardan cifrados con Fernet y clave en `.env`
- `fecha_visita` se registra automáticamente con `auto_now_add=True`
- El sistema soporta visitas múltiples para un mismo visitante
- Todos los errores tienen formato estandarizado con `error` y `detalle`

---

**Última actualización:** Julio 2025\
**Versión:** 1.0

