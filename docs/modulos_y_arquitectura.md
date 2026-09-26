```markdown
# 🏗️ Módulos y Arquitectura del Proyecto

## 🧩 Listado de Módulos Funcionales

| Módulo (app Django) | Responsabilidad | Estado actual | Prioridad |
|---|---|---|---|
| `usuarios` | Login, autenticación, gestión de perfiles y roles (Administrador / Vecino) | Diseñado (Código validación) | Alta (MVP) |
| `consorcios` | Alta de consorcios, registro de unidades y porcentaje fiscal | Diseñado (Código validación) | Alta (MVP) |
| `economia` | Gastos, liquidaciones mensuales, cálculo de prorrateo y pagos | Diseñado (Código validación) | Alta (MVP) |
| `mantenimientos` | Registro de tareas edilicias, observaciones y seguimiento de estado | Diseñado (Pausado) | Media |
| `reunions` | Convocatoria a reuniones de consorcio, asignación de temario y enlace | Diseñado (Pausado) | Media |

---

## 🏛️ Arquitectura del Proyecto

Se ha seleccionado una **arquitectura desacoplada basada en cliente-servidor con API REST**:

- **Backend (API REST):** Desarrollado en **Python 3.12** y **Django REST Framework (DRF)**, utilizando autenticación basada en **JWT (JSON Web Tokens)**. La lógica del backend opera mediante controladores de vistas y serializadores para exponer endpoints limpios y seguros.
- **Frontend (SPA):** Desarrollado con **React 18** y **Vite**, gestionando la interfaz del Administrador y del Vecino mediante consumo de la API REST.
- **Base de Datos Relacional:** **PostgreSQL 16** para garantizar la integridad referencial de los datos y el soporte de transacciones para el área económica.