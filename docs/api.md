# Especificación de API REST - Sistema de Gestión de Consorcios

**Módulo:** Documentación Técnica de Backend  
**Formato de Intercambio:** `application/json`  
**Autenticación:** JWT (JSON Web Tokens) / Bearer Token  

---

## 1. Módulo de Autenticación y Usuarios (`/api/v1/auth`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `POST` | `/api/v1/auth/register/` | Registro de nuevo usuario (Admin/Vecino). | Público | `201 Created` / `400` |
| `POST` | `/api/v1/auth/login/` | Iniciar sesión y obtener Tokens (Access & Refresh). | Público | `200 OK` / `401` |
| `POST` | `/api/v1/auth/refresh/` | Renovar Token de Acceso expirado. | Público | `200 OK` / `401` |
| `GET` | `/api/v1/auth/me/` | Obtener el perfil y unidades asignadas del usuario activo. | `ADMIN`, `VECINO` | `200 OK` |

---

## 2. Módulo de Consorcios y Unidades (`/api/v1/consorcios`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `GET` | `/api/v1/consorcios/` | Listar consorcios asignados al usuario. | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/consorcios/` | Crear un nuevo consorcio. | `ADMIN` | `201 Created` / `400` |
| `GET` | `/api/v1/consorcios/{id}/` | Detalle de un consorcio. | `ADMIN`, `VECINO` | `200 OK` / `404` |
| `GET` | `/api/v1/consorcios/{id}/unidades/` | Listar unidades funcionales de un consorcio. | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/consorcios/{id}/unidades/` | Alta de unidad funcional con asignación fiscal. | `ADMIN` | `201 Created` / `400` |

---

## 3. Módulo de Gastos y Liquidaciones (`/api/v1/liquidaciones`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `GET` | `/api/v1/consorcios/{id}/liquidaciones/` | Listar liquidaciones del consorcio. | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/consorcios/{id}/liquidaciones/` | Abrir nueva liquidación para el periodo. | `ADMIN` | `201 Created` / `400` |
| `POST` | `/api/v1/liquidaciones/{id}/gastos/` | Registrar gasto (Ordinario/Extraordinario). | `ADMIN` | `201 Created` / `400` |
| `PATCH` | `/api/v1/liquidaciones/{id}/cerrar/` | Cerrar liquidación y congelar montos. | `ADMIN` | `200 OK` / `400` |

---

## 4. Módulo de Pagos y Comprobantes (`/api/v1/pagos`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `GET` | `/api/v1/liquidaciones/{id}/pagos/` | Listar pagos (Admin ve todos, Vecino solo suyos). | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/liquidaciones/{id}/pagos/` | Registrar pago (monto, fecha y comprobante). | `ADMIN`, `VECINO` | `201 Created` / `400` |
| `PATCH` | `/api/v1/pagos/{id}/confirmar/` | Aprobar/Rechazar un pago registrado. | `ADMIN` | `200 OK` / `400` |

---

## 5. Módulo de Mantenimiento (`/api/v1/mantenimiento`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `GET` | `/api/v1/consorcios/{id}/mantenimiento/` | Listar tareas de mantenimiento edilicio. | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/consorcios/{id}/mantenimiento/` | Registrar nueva orden de reparación. | `ADMIN` | `201 Created` / `400` |
| `PATCH` | `/api/v1/mantenimiento/{id}/` | Actualizar estado (`PENDIENTE`, `EN_PROCESO`, `FINALIZADO`). | `ADMIN` | `200 OK` |

---

## 6. Módulo de Reuniones y Asambleas (`/api/v1/reuniones`)

| Método | Endpoint | Descripción | Roles Permitidos | Código Respuesta |
| :--- | :--- | :--- | :---: | :---: |
| `GET` | `/api/v1/consorcios/{id}/reuniones/` | Consultar convocatorias a asambleas. | `ADMIN`, `VECINO` | `200 OK` |
| `POST` | `/api/v1/consorcios/{id}/reuniones/` | Programar nueva convocatoria a asamblea. | `ADMIN` | `201 Created` / `400` |
| `PATCH` | `/api/v1/reuniones/{id}/` | Actualizar estado o cargar resumen/acta. | `ADMIN` | `200 OK` |

---

## 7. Estructura de Respuestas y Manejo de Errores

### Respuesta Exitosa (`200 OK` / `201 Created`)
```json
{
  "status": "success",
  "data": {
    "id": 12,
    "monto": 45000.00,
    "estado": "CONFIRMADO"
  }
}