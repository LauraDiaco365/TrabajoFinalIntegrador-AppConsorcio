# 🏢 Consorcio360

**Consorcio360** es una aplicación web diseñada para la gestión integral y transparente de consorcios. La plataforma centraliza la administración económica, el seguimiento operativo de mantenimientos y la comunicación entre administradores y vecinos.

---

## 🎯 Objetivo y Circuito del Sistema

El objetivo del proyecto es desarrollar un sistema funcional que cubra el flujo completo de la vida cotidiana de un consorcio.

### 🔄 Circuito principal que posibilita la aplicación:

**1. Configuración del Consorcio:** Alta del consorcio, registro de unidades habitacionales y asignación del porcentaje fiscal correspondiente a cada unidad.

**2. Gestión Económica:** Registro de gastos ordinarios y extraordinarios, generación de liquidaciones mensuales, cálculo automático del prorrateo según el porcentaje fiscal y emisión de estados de cuenta.

**3. Registros de Pago:** Posibilidad de que los vecinos registren sus pagos simulados y el administrador los confirme o valide.

**4. Seguimiento de Mantenimientos:** Registro de trabajos edilicios o reparaciones con un semáforo de seguimiento (`pendiente`, `en_proceso`, `finalizado`) y observaciones del estado de las obras.

**5. Convocatoria a Reuniones:** Creación de convocatorias a asambleas o reuniones de consorcio con fecha, hora, lugar o enlace y temario de los puntos a tratar.

---

## 📌 Decisión de Alcance y Registro de Cambios

Para garantizar la claridad del proyecto y responder punto por punto a las devoluciones de la tutora, documentamos las siguientes decisiones:

### 📩 Ajustes de la 1.ª Entrega
* **Ajuste del Stack Tecnológico:** A partir de las observaciones de la primera entrega, simplificamos la arquitectura y dejamos fuera de esta etapa inicial tecnologías complejas como Celery, Redis, almacenamiento en MinIO/S3 y TypeScript. Decidimos enfocarnos en un MVP sólido y funcional basado en **Python 3.12, Django 5.x, Django REST Framework, React 18 y PostgreSQL 16**.

### 📩 Ajustes de la 2.ª Entrega
* **Unificación del Alcance:** Definimos este `README.md` como el **único documento de alcance vigente**. Para evitar contradicciones, el borrador inicial (`README_anterior.md`) fue movido a la carpeta `docs/historial/` únicamente como registro histórico del proyecto.
* **Inclusión de los Módulos (`mantenimientos` y `reunions`):** En respuesta al señalamiento sobre las apps que ya estaban creadas en el repositorio, confirmamos que **ambas se mantienen dentro del alcance del proyecto**. En esta entrega sumamos sus entidades y reglas de negocio al diseño conceptual y al Diagrama ER, pausando el desarrollo de código hasta que la documentación técnica esté aprobada.
* **Higiene del Repositorio (`.gitignore`):** Agregamos un archivo `.gitignore` para proyectos Django y React, y quitamos del seguimiento de Git la carpeta del entorno virtual (`venv/`), los archivos de base de datos local (`*.sqlite3`) y las carpetas de caché (`__pycache__/`).
* **Respeto al Proceso de Diseño:** Tomamos en cuenta la indicación de validar el diseño antes de programar, por lo que no avanzaremos con nueva lógica en código (backend o frontend) hasta contar con la aprobación formal de esta entrega.

---
## 🛠️ Stack tecnológico

### Backend
- **Python 3.12** — lenguaje principal.
- **Django 5.x** — framework MVC: ORM, autenticación, panel de administración.
- **Django REST Framework** — API REST para la comunicación frontend ↔ backend.
- **SimpleJWT** — autenticación con tokens JWT (sesiones seguras y stateless).

### Frontend
- **React 18** — interfaz de usuario (SPA).
- **Vite (Node.js / npm)** — servidor de desarrollo y build del frontend.
- **CSS tradicional** — estilos propios, sin frameworks, para mantener el desarrollo simple y transparente.

### Base de datos
- **PostgreSQL 16** — base relacional (port `5432`).
- **Docker Compose** *(opcional)* — levanta PostgreSQL con un comando sin instalarlo en el sistema.

### Pruebas
- **Pytest + pytest-django** — tests unitarios del backend (reglas de prorrateo, permisos).

### Versionado y deploy
- **Git + GitHub** — repositorio con historial de cambios.
- **Render** — deploy del backend y la base de datos en la nube.

> **Criterio de selección:** se priorizó un stack conocido, maduro y de bajo "costo de configuración". Django entrega de fábrica autenticación segura, ORM y panel de administración, lo que permite dedicar el tiempo del proyecto a la lógica de negocio del dominio (prorrateo, liquidaciones, pagos) en lugar de a infraestructura.

---
## Documentación del Proyecto

* 📄 **[Requerimientos Funcionales y no funcionales, matriz de permisos por rol y flujos de procesos principales](docs/requerimientos_funcionales.md)**
* 📐 **[Diagrama ER y Modelo Relacional](docs/diagrama_er.md)**
* 🗄️ **[Script SQL de la Base de Datos](database/schema.sql)**
* 📝 **[Registro de Cambios y Decisiones de Diseño](decisiones_de_diseno.md)**
* 📝 **[Diseño de API REST para el backend](api.md)**
- 📄 **[Reglas de Negocio Detalladas](./docs/reglas_de_negocio.md)**

---

## 📁 Estructura del Repositorio

El proyecto mantiene una organización modular dividiendo la documentación técnica, los scripts relacionales de la base de datos, el backend con Django y la interfaz de usuario con React:

```text
TrabajoFinalIntegrador-AppConsorcio/
├── assets/                            # Recursos estáticos (logos, capturas de pantalla, esquemas)
├── backend/                           # Proyecto Backend Django
│   ├── config/                        # Configuración global de Django (settings.py, urls.py, wsgi.py)
│   ├── consorcios/                    # App: Gestión de consorcios y catastro de unidades
│   ├── economia/                      # App: Gastos, liquidaciones, expensas y pagos
│   ├── mantenimientos/                # App: Seguimiento de obras y reparaciones edilicias
│   ├── reunions/                      # App: Convocatorias a asambleas y resúmenes/actas
│   ├── usuarios/                      # App: Autenticación, perfiles y roles (RBAC)
│   └── manage.py                      # Script ejecutable de Django (ubicado en la raíz de backend)
├── database/                          # Definición física de la base de datos PostgreSQL
│   └── schema.sql                     # Script DDL/DML con tablas, constraints y claves foráneas
├── docs/                              # Documentación técnica y académica del proyecto
│   ├── requerimientos_funcionales.md  # RF, RNF, Matriz RBAC y Casos de Uso (CU-00 a CU-04)
│   ├── reglas_de_negocio.md           # Invariantes (100% fiscal), fórmulas de prorrateo y restricciones
│   ├── api.md                         # Especificación de la API REST (Endpoints, JSONs, JWT)
│   ├── decisiones_de_diseno.md        # Justificaciones arquitectónicas, changelog y notas de cátedra
│   ├── diagrama_er.md                 # Diagrama Entidad-Relación y diccionario de datos
│   └── historial/                     # Registro histórico de versiones previas
│       └── README_anterior.md
├── frontend/                          # Proyecto React + Vite (Interfaz de usuario)
├── .gitignore                         # Archivos excluidos del versionado (venv, db.sqlite3, .env)
├── README.md                          # Documentación principal y portal del repositorio
└── requirements.txt                   # Dependencias de Python para el backend

/* Archivos locales de desarrollo (excluidos por .gitignore): */
├── venv/                              # Entorno virtual local de Python (no se sube a Git)
└── db.sqlite3                         # Base de datos SQLite local para pruebas rápidas (no se sube a Git)
```
> **Nota sobre la simplificación de infraestructura:**  
> A partir de las observaciones de la cátedra para prevenir la sobre-ingeniería (*scope creep*), **se eliminó la configuración de `docker-compose.yml`**. El entorno de desarrollo opera de forma nativa con entornos virtuales de Python (`venv`) y PostgreSQL local, mientras que el despliegue en producción se realiza mediante la plataforma PaaS **Render**, que aprovisiona el runtime de Python y PostgreSQL de manera directa.
---

## 🗄️ Diseño de la base de datos

Para evitar inconsistencias y mantener una única fuente de verdad en el proyecto, el diseño completo de la base de datos se encuentra centralizado y documentado en:

👉 **[Ver Diagrama ER y Especificación Oficial de la Base de Datos](docs/diagrama_er.md)**

### Resumen de Entidades Principales

* **Usuario (`usuarios_usuario`):** Cuentas de usuarios del sistema con roles definidos (`administrador`, `vecino`, etc.).
* **Consorcio (`consorcios_consorcio`):** Datos del consorcio/edificio. Vinculado a su Administrador responsable (`administrador_id`).
* **Unidad (`consorcios_unidad`):** Departamentos o unidades funcionales. Identificadas por `piso` y `departamento` (`UNIQUE (consorcio_id, piso, departamento)`) y vinculadas a su `propietario_id`.
* **Gasto (`economia_gasto`):** Gastos registrados por el consorcio, clasificados por tipo (`ordinario`/`extraordinario`).
* **Liquidación (`economia_liquidacion`):** Periodos de liquidación de expensas (mes/año) con estado (`abierta`/`cerrada`) El monto total se calcula dinámicamente durante el periodo abierto y se congela al momento del cierre para preservar los saldos históricos.
* **Pago (`economia_pago`):** Registro de pagos efectuados por las unidades, con estado de confirmación (`pendiente`/`confirmado`).
* **Mantenimiento (`mantenimiento_mantenimiento`):** Novedades, reclamos o trabajos de mantenimiento con sus fechas y observaciones.
* **Reunión (`reuniones_reunion`):** Asambleas o reuniones de consorcio con su temario, enlace/lugar y estado.

## 📋 Reglas de Negocio Principales

- **Consorcio y Unidades:** Un Administrador gestiona uno o más consorcios. Cada consorcio agrupa sus unidades funcionales (departamentos, cocheras, locales), las cuales se vinculan a un vecino propietario.
  - **Invariante Fiscal (100%):** La suma acumulada del `porcentaje_fiscal` de todas las unidades debe dar exactamente **100.00%**. El backend exige este balance para permitir el cierre de liquidaciones.
  - **Unicidad Territorial:** Se restringe por BD la duplicación de `(consorcio_id, piso, departamento)`.
  - **Multi-unidad y Selección Propiedad Activa:** Un vecino puede poseer varias unidades (incluso en diferentes consorcios) y selecciona en sesión sobre cuál operar.

- **Gestión Económica y Liquidaciones:**
  - **Restricción de Liquidación Única:** Restricción por BD de `UNIQUE (consorcio_id, mes, año)`.
  - **Cierre e Inmutabilidad:** Al pasar a estado `CERRADA`, el `monto_total` y los gastos cargados se congelan para garantizar la inmutabilidad histórica del cálculo de expensas.

- **Pagos y Saldos:**
  - **Flujo de Aprobación:** Los pagos registrados nacen en estado `PENDIENTE` y requieren verificación del Administrador para cambiar a `CONFIRMADO`.
  - **Pagos Parciales:** La relación 1:N entre liquidación/unidad y pagos admite entregas en cuotas, calculando el saldo pendiente dinámicamente: $\text{Monto Expensa} - \sum \text{Pagos Confirmados}$.

- **Mantenimiento y Asambleas:**
  - **Seguimiento Read-Only:** El vecino consulta el avance de obras y reparaciones en modo solo lectura.
  - **Convocatoria y Resumen de Asambleas:** El Administrador gestiona el ciclo de vida de las reuniones (`PENDIENTE`, `FINALIZADA`, `CANCELADA`) y publica la síntesis o acta de lo tratado al concluir.

---

## 🧩 Módulos del Sistema

| Módulo (app Django) | Responsabilidad | Estado actual |
|---|---|---|
| `usuarios` | Login, registro y gestión de roles (Administrador / Vecino) | Diseñado / Código inicial validado |
| `consorcios` | Alta de consorcios, registro de unidades y porcentaje fiscal | Diseñado / Código inicial validado |
| `economia` | Gastos, liquidaciones mensuales, cálculo de prorrateo y pagos simulados | Diseñado / Código inicial validado |
| `mantenimientos` | Registro de tareas edilicias, observaciones y semáforo de seguimiento | Diseñado (Pausado de codificación) |
| `reunions` | Convocatoria a reuniones de consorcio, asignación de temario y canal | Diseñado (Pausado de codificación) |

---

## 🗺️ Roadmap del Proyecto

| Etapa | Contenido | Estado |
|---|---|---|
| **1. Diseño y Base** | Stack, modelo ER (5 apps), arquitectura, `.gitignore` y documentación técnica | 🔵 En curso |
| **2. Backend API** | Endpoints REST, JWT, CRUD de consorcios, unidades y gastos | ⬜ |
| **3. Lógica Económica** | Liquidaciones, prorrateo verificado y registro de pagos simulados | ⬜ |
| **4. Mantenimientos y Reuniones** | Endpoints para estados de mantenimientos y convocatorias | ⬜ |
| **5. Frontend React** | Interfaz para administradores y vecinos (paneles, estados de cuenta, mantenimientos) | ⬜ |
| **6. Integración y Deploy** | Pruebas de integración, correcciones, deploy en Render y presentación final | ⬜ |

---

### 🚀 Mejoras Futuras (Fuera del MVP)

Las siguientes funcionalidades quedan identificadas como evolución de la plataforma para versiones posteriores:

* **Mantenimientos avanzados:** Adjuntos de fotos y módulo de comentarios de seguimiento por obra.
* **Asambleas y Actas:** Integración de reuniones virtuales, generación y firma de actas digitalizadas, y sistema de votaciones en línea.
* **Gestión Financiera Avanzada:** Elaboración de presupuestos, categorización por rubros de gastos, cálculo de prorrateo diferenciado por grupos (coeficientes A/B/C) e intereses moratorios automáticos.
* **Notificaciones y Automatización:** Envío de avisos automáticos por correo/WhatsApp mediante **Celery + Redis**.
* **Infraestructura y Servicios:** Almacenamiento de archivos y comprobantes en **MinIO / Amazon S3** e integración con pasarelas de **pagos reales**.

---

## 🧪 Verificación del Diseño y Pruebas Iniciales

> ⚠️ **Nota sobre el alcance de desarrollo:** Siguiendo las indicaciones de las entregas académicas, el código existente en el repositorio se utilizó únicamente como una **prueba de concepto para validar la viabilidad del diseño de datos** (especialmente el cálculo dinámico del prorrateo). El desarrollo formal de nuevos endpoints, la codificación de las apps `mantenimientos` y `reunions`, y el frontend en React se encuentran en pausa hasta la validación de esta documentación.

### 🚀 Guía de Instalación y Ejecución Local

#### Prerrequisitos
- **Python 3.12+**
- **Node.js 18+** y **npm** (requeridos para el motor de ejecución de React y Vite).
- **PostgreSQL 16** corriendo en local (puerto `5432`) con la base de datos `consorcio_db` creada.

---

```bash
# 1. Clonar el repositorio y acceder al proyecto
git clone [https://github.com/LauraDiaco365/TrabajoFinalIntegrador-AppConsorcio.git](https://github.com/LauraDiaco365/TrabajoFinalIntegrador-AppConsorcio.git)
cd TrabajoFinalIntegrador-AppConsorcio

# 2. Configurar e iniciar el Backend (Django + PostgreSQL)
cd backend

# Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate          # En Windows
# source venv/bin/activate     # En Linux/Mac

# Instalar dependencias de Python (Django 5, DRF, SimpleJWT, Pytest, psycopg)
pip install -r requirements.txt

# Crear el archivo .env a partir de la plantilla
cp .env.example .env     # En Linux/Mac
# copy .env.example .env # En Windows (CMD/PowerShell)

# Aplicar migraciones en PostgreSQL local y crear el superusuario administrador
python manage.py migrate
python manage.py createsuperuser

# (Opcional) Ejecutar la suite de pruebas unitarias. Verifica que las reglas de negocio (prorrateo 100%, inmutabilidad, RBAC) pasen correctamente
pytest

# Levantar el servidor de desarrollo de la API REST (http://localhost:8000)
python manage.py runserver

# 3. Configurar e iniciar el Frontend (React 18 + Vite) — En otra terminal. El cliente Web quedará disponible en http://localhost:5173/
cd ../frontend
npm install
npm run dev
```

## Demo en el panel de administración

Después de levantar el servidor (`python manage.py runserver`), entrar a:

`http://127.0.0.1:8000/admin`

### Pasos de la demo
1. Iniciar sesión con el superusuario creado.
2. Crear **usuario vecino** de prueba
3. Cargar un **Consorcio** de prueba 
3. Agregar **2 Unidades** dentro de ese consorcio creado con porcentajes fiscales que sumen 100%, por ejemplo, 50% y 50% (las unidades pueden estar asignadas al mismo vecino de prueba)
4. Registrar **1 Gasto** (ejemplo: Luz $10.000) de tipo `ordinario`.
5. Crear la **Liquidación** del mes correspondiente.

### Resultado esperado
En el panel de administración y detalle de la liquidación:
- Mientras la liquidación está `abierta`, el importe por unidad se calcula dinámicamente según el porcentaje fiscal (ejemplo: `1A: $5.000,00`, `1B: $5.000,00`).
- Al pasar la liquidación a estado `cerrada`, el **monto_total** ($10.000,00) y los gastos quedan congelados en la base de datos, asegurando la inmutabilidad de los saldos históricos.

Esto confirma que la lógica de prorrateo y la regla de cierre funcionan correctamente tanto en los tests como en la interfaz del admin.


## 🧪 Tests de la app *economia*

El archivo `tests.py` de la app **economia** comprueba que el cálculo del prorrateo funciona correctamente.  
Ejemplo: un gasto de $10.000 se reparte 50/50 entre dos unidades, resultando $5.000 para cada una y validando la restricción del 100% en porcentajes fiscales.

### Cómo ejecutarlo
Desde la carpeta donde está `manage.py`:

```bash
python manage.py test economia
```


## 📌 Estado actual

- ✅ **Stack tecnológico** redefinido y ajustado al alcance del MVP.
- ✅ **Esquema relacional (Diagrama ER)** diseñado e integrado para las 5 apps (usuarios, consorcios, economia, mantenimientos, reunions).
- ✅ **Modelos conceptuales y reglas de negocio** documentados detalladamente
- ✅**Higiene del repositorio**: Archivo .gitignore configurado y desacople de entornos virtuales y bases de datos locales.
- ⬜ **Desarrollo de API REST con Django REST Framework y JWT** (Pausado hasta aprobación).
- ⬜ **Desarrollo del Frontend en React + Vite** (Pausado hasta aprobación).
- ⬜ **Pruebas de integración final y Deploy en producción** (Pausado hasta aprobación)


