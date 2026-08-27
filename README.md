# 📘 Proyecto: Aplicación de Gestión de Consorcios

## 👥 Tutora: 
- Sofia Raia
  
## 👥 Equipo 188
- Laura Diaco  
- Matias Mansilla

---

# 🏢 Consorcio360

## 📋 Introducción

Como grupo decidimos desarrollar **Consorcio360**, una aplicación web para la **gestión integral de consorcios**, pensada para centralizar en un único lugar la administración económica, el seguimiento de mantenimientos y la comunicación entre administradores y vecinos.

La idea surge de una situación cotidiana: en muchos consorcios, la información sobre gastos, reparaciones, reuniones y decisiones se encuentra distribuida entre distintos medios, dificultando tanto la administración como el acceso de los vecinos a la información.

Consorcio360 busca resolver esta problemática ofreciendo una plataforma simple y centralizada que permita **organizar la información, facilitar el seguimiento y promover la transparencia y la participación vecinal**.

El sistema contará con dos roles principales:

- 👤 **Administrador:** gestiona el consorcio, unidades, gastos, liquidaciones, presupuestos, mantenimientos, reuniones y votaciones.
- 🏠 **Vecino:** consulta la información de su unidad, liquidaciones, pagos y mantenimientos, y puede participar en reuniones y votaciones.

---

# 🎯 Objetivo del proyecto

El objetivo de Consorcio360 es desarrollar una primera versión funcional que permita cubrir el **circuito principal de gestión de un consorcio**, desde su configuración inicial hasta la participación de los vecinos.

El flujo general del sistema será:

**Crear consorcio → cargar unidades → registrar gastos → generar liquidaciones → consultar y registrar pagos → gestionar mantenimientos → realizar reuniones → votar → registrar actas.**

El proyecto se desarrollará mediante un enfoque incremental, donde cada etapa incorpora nuevas funcionalidades sobre la versión anterior hasta alcanzar un sistema integrado y funcional.

---

# 🔄 Flujo del sistema

## 👤 Flujo del Administrador

El administrador será el encargado de configurar y gestionar el consorcio.

### 1. Alta del consorcio

- Crear el consorcio.
- Cargar las unidades habitacionales.
- Asignar el porcentaje fiscal correspondiente a cada unidad.

Esta información será la base para realizar posteriormente las liquidaciones.

### 2. Gestión económica

- Registrar gastos.
- Generar liquidaciones mensuales.
- Prorratear los gastos según el porcentaje fiscal.
- Consultar el estado general de las liquidaciones.
- Registrar gastos extraordinarios.
- Crear presupuestos para futuros trabajos.

### 3. Mantenimientos

- Registrar tareas de mantenimiento.
- Asignar estados:
  - 🔴 **Pendiente**
  - 🟡 **En proceso**
  - 🟢 **Finalizado**
- Agregar fotografías.
- Registrar comentarios.
- Realizar el seguimiento de los trabajos.

### 4. Reuniones y votaciones

- Crear reuniones virtuales.
- Publicar información relacionada con la reunión.
- Crear votaciones.
- Consultar resultados.
- Subir las actas correspondientes.

---

## 🏠 Flujo del Vecino

El vecino podrá acceder a la información correspondiente a su unidad y participar de las actividades del consorcio.

### 1. Acceso

- Iniciar sesión.
- Acceder a su perfil.
- Consultar la información de su unidad.

### 2. Liquidaciones y pagos

- Consultar la liquidación mensual.
- Consultar el histórico.
- Ver el estado de cuenta.
- Registrar pagos simulados.

### 3. Mantenimientos

- Consultar el estado de los mantenimientos.
- Visualizar el semáforo de cada tarea.
- Ver fotografías.
- Consultar comentarios y avances.

### 4. Reuniones y participación

- Acceder a reuniones virtuales.
- Consultar actas.
- Participar en votaciones.
- Consultar los resultados.

---

# 🚀 Desarrollo del MVP

El **Producto Mínimo Viable (MVP)** se desarrollará durante **9 semanas**, mediante entregas progresivas.

Cada entrega tendrá un objetivo concreto y dejará una parte del sistema funcionando, permitiendo validar el avance antes de continuar con la siguiente etapa.

---

## 📦 Entrega 1 — Base del sistema

### ⏱️ Semanas 1 y 2

**Objetivo:** construir la estructura sobre la que funcionará toda la aplicación.

### Se desarrolla

- Modelo de datos.
- Usuarios y roles.
- Consorcios.
- Unidades habitacionales.
- Porcentaje fiscal.
- Configuración de PostgreSQL.
- Estructura inicial de Django.

### 📌 Entrega

Una primera versión con la estructura básica del sistema y la base de datos configurada.

El administrador podrá contar con un consorcio y sus unidades correctamente definidos.

---

## 📦 Entrega 2 — Backend y gestión económica

### ⏱️ Semanas 3 y 4

**Objetivo:** implementar la lógica principal del sistema.

### Se desarrolla

- Backend con Django.
- API REST con Django REST Framework.
- Login y permisos según rol.
- Registro de gastos.
- Liquidaciones mensuales.
- Prorrateo según porcentaje fiscal.
- Consulta de liquidaciones.
- Registro de pagos.
- Estado de cuenta.
- Mantenimientos básicos.

### 📌 Entrega

Una versión funcional del backend capaz de gestionar el circuito económico principal.

**Consorcio → Gastos → Liquidación → Vecino → Estado de cuenta**

---

## 📦 Entrega 3 — Interfaz web

### ⏱️ Semanas 5 y 6

**Objetivo:** construir una interfaz clara y accesible para utilizar las funcionalidades del sistema.

### Se desarrolla

- Frontend con React.
- TypeScript.
- Login.
- Panel del administrador.
- Panel del vecino.
- Gestión de unidades.
- Visualización de gastos.
- Liquidaciones e histórico.
- Estado de cuenta.
- Mantenimientos.
- Semáforo de estados.

### 📌 Entrega

Una interfaz navegable donde administrador y vecino puedan acceder a las funcionalidades correspondientes a cada rol.

---

## 📦 Entrega 4 — Integración

### ⏱️ Semana 7

**Objetivo:** integrar frontend, backend y base de datos.

### Se desarrolla

- Integración React + API REST.
- Conexión con PostgreSQL.
- Validaciones.
- Manejo de errores.
- Pruebas de permisos.
- Pruebas del flujo principal.

### 📌 Entrega

Una versión integrada donde las acciones realizadas desde la interfaz se reflejen correctamente en el backend y en la base de datos.

---

## 📦 Entrega 5 — Funcionalidades complementarias

### ⏱️ Semana 8

**Objetivo:** completar las funcionalidades definidas para el MVP.

### Se desarrolla

- Gastos extraordinarios.
- Presupuestos.
- Mantenimientos completos.
- Fotografías y comentarios.
- Reuniones virtuales.
- Actas.
- Votaciones.
- Registro de votos.
- Tareas programadas con Celery + Redis.
- Almacenamiento de archivos con MinIO/S3.

### 📌 Entrega

La versión completa del MVP, incorporando la gestión de mantenimientos, situaciones extraordinarias y participación vecinal.

---

## 📦 Entrega final — Pruebas y documentación

### ⏱️ Semana 9

**Objetivo:** preparar el proyecto para su entrega y presentación.

### Se realiza

- Pruebas funcionales.
- Corrección de errores.
- Validación de roles y permisos.
- Prueba del flujo completo.
- Deploy.
- Documentación técnica.
- Documentación de uso.
- Actualización del repositorio.
- Preparación de la presentación.

### 📌 Entrega

Una versión funcional, probada y documentada de **Consorcio360**, lista para su presentación final.

---

# 📊 Roadmap

| Tiempo | Entrega | Resultado |
|---|---|---|
| **Semanas 1–2** | 🧱 Base del sistema | Usuarios, roles, consorcio, unidades y PostgreSQL |
| **Semanas 3–4** | ⚙️ Backend | Gastos, liquidaciones, pagos y mantenimientos |
| **Semanas 5–6** | 🎨 Frontend | Paneles de administrador y vecino |
| **Semana 7** | 🔗 Integración | Frontend + backend + PostgreSQL |
| **Semana 8** | 🚀 MVP completo | Presupuestos, reuniones, actas, votaciones, archivos y funcionalidades complementarias |
| **Semana 9** | ✅ Entrega final | Pruebas, documentación, deploy y presentación |

---

# 🧱 Modelo conceptual

La información del sistema se organizará mediante un **modelo relacional utilizando PostgreSQL**.

Las principales entidades contempladas son:

### Gestión administrativa

- `Usuario`
- `Consorcio`
- `Unidad`

### Gestión económica

- `Gasto`
- `Liquidacion`
- `Pago`
- `Presupuesto`

### Gestión de mantenimiento

- `Mantenimiento`
- `Comentario`
- `Foto`

### Reuniones y participación

- `Reunion`
- `Acta`
- `Votacion`
- `Voto`

Las relaciones entre estas entidades permitirán representar el funcionamiento del sistema y mantener la información organizada.

---

# ⚙️ Tecnologías

| Área | Tecnología |
|---|---|
| **Backend** | Python + Django |
| **API** | Django REST Framework |
| **Frontend** | React + TypeScript |
| **Base de datos** | PostgreSQL |
| **Tareas programadas** | Celery + Redis |
| **Almacenamiento de archivos** | MinIO / S3 |
| **Control de versiones** | GitHub |
| **Deploy** | Railway / Render |

## 🗄️ PostgreSQL

Se utilizará **PostgreSQL** como sistema de gestión de base de datos relacional.

Permitirá almacenar y relacionar la información estructurada del sistema:

- Usuarios.
- Consorcios.
- Unidades.
- Gastos.
- Liquidaciones.
- Pagos.
- Presupuestos.
- Mantenimientos.
- Reuniones.
- Votaciones.

## 📁 MinIO / S3

Se utilizará para almacenar archivos asociados al sistema, como:

- Fotografías de mantenimientos.
- Comprobantes.
- Actas.
- Documentación de gastos y presupuestos.

De esta manera, **PostgreSQL** se encargará de la información estructurada y sus relaciones, mientras que **MinIO/S3** estará destinado al almacenamiento de archivos.

---

# 📅 Plan general

El proyecto seguirá un desarrollo incremental:

**Modelado → Backend → Frontend → Integración → Funcionalidades complementarias → Pruebas → Deploy**

Cada etapa se apoyará en la anterior, permitiendo construir progresivamente el producto y mantener un alcance realista durante todo el desarrollo.

---

# 📌 Alcance del MVP

El MVP se enfocará en las funcionalidades necesarias para cubrir el flujo principal de gestión de un consorcio.

## ✅ Incluye

### Gestión de usuarios

- Registro e inicio de sesión.
- Roles de **Administrador** y **Vecino**.
- Acceso a funcionalidades según el rol.

### Gestión del consorcio

- Alta del consorcio.
- Registro de unidades habitacionales.
- Asignación de porcentaje fiscal.

### Gestión económica

- Registro de gastos.
- Liquidaciones mensuales.
- Prorrateo según porcentaje fiscal.
- Consulta de liquidaciones.
- Histórico de liquidaciones.
- Registro de pagos simulados.
- Estado de cuenta.
- Gastos extraordinarios.
- Presupuestos.

### Gestión de mantenimientos

- Registro de mantenimientos.
- Estados **Pendiente, En proceso y Finalizado**.
- Visualización mediante semáforo.
- Registro de fotografías.
- Comentarios y seguimiento de los trabajos.

### Reuniones y participación

- Creación de reuniones virtuales.
- Publicación de actas.
- Creación de votaciones.
- Registro de votos.
- Consulta de resultados.

### Servicios complementarios

- Tareas programadas mediante **Celery + Redis**.
- Almacenamiento de archivos mediante **MinIO/S3**.

---

## 🚫 No incluye inicialmente

Para mantener un alcance realista y poder completar el MVP dentro del tiempo establecido, quedan fuera de esta primera versión:

- Integración con bancos o billeteras virtuales.
- Pagos reales mediante plataformas externas.
- Aplicación móvil nativa.
- Firma digital de documentos.
- Automatizaciones contables avanzadas.
- Integraciones avanzadas con proveedores externos.

Estas funcionalidades podrán ser consideradas como **mejoras futuras** una vez finalizado el MVP.

---

# ✅ Criterios de finalización del MVP

El MVP se considerará finalizado cuando se cumplan los siguientes criterios:

- [ ] El administrador puede crear y configurar un consorcio.
- [ ] Se pueden registrar unidades habitacionales y sus porcentajes fiscales.
- [ ] Se pueden registrar gastos.
- [ ] El sistema puede generar liquidaciones mensuales.
- [ ] El prorrateo se realiza de acuerdo con el porcentaje fiscal de cada unidad.
- [ ] El vecino puede consultar su liquidación y su histórico.
- [ ] El vecino puede registrar un pago simulado y consultar su estado de cuenta.
- [ ] El administrador puede registrar y realizar el seguimiento de mantenimientos.
- [ ] Los mantenimientos pueden visualizarse mediante un semáforo de estados.
- [ ] Se pueden agregar fotografías y comentarios a los mantenimientos.
- [ ] El administrador puede crear reuniones y cargar actas.
- [ ] El administrador puede crear votaciones.
- [ ] El vecino puede participar en las votaciones.
- [ ] Se pueden consultar los resultados de las votaciones.
- [ ] Los diferentes módulos se encuentran integrados.
- [ ] Se respetan los permisos correspondientes a cada rol.
- [ ] La información queda correctamente almacenada en PostgreSQL.
- [ ] La aplicación puede ejecutarse de forma funcional.
- [ ] Se realizaron pruebas y se corrigieron los errores principales.
- [ ] El proyecto cuenta con documentación básica para su utilización y presentación.

## 🎯 Criterio principal

Más allá de que cada funcionalidad individual funcione correctamente, el MVP deberá permitir realizar de forma integrada el **flujo principal de gestión del consorcio**, conectando la administración, la información económica, los mantenimientos y la participación de los vecinos.

---

# 🎓 Proyecto Integrador

Consorcio360 forma parte del proyecto integrador académico del grupo y busca aplicar los conocimientos adquiridos durante la cursada en el desarrollo de una solución web para un problema real.

El proyecto integra conceptos de:

- Desarrollo backend.
- Desarrollo frontend.
- APIs REST.
- Bases de datos relacionales.
- Autenticación y roles.
- Gestión de archivos.
- Tareas programadas.
- Control de versiones.
- Deploy.

El objetivo final es obtener una aplicación funcional que permita centralizar la gestión de un consorcio y mejorar la comunicación, el seguimiento y el acceso a la información entre administradores y vecinos.

---

# 📝 Conclusión

Consorcio360 busca ofrecer una solución simple y centralizada para una problemática cotidiana: la gestión de la información y las actividades de un consorcio.

A través del MVP se propone integrar en una única plataforma la **administración económica, el seguimiento de mantenimientos y la participación de los vecinos**, permitiendo que cada usuario acceda a la información y funcionalidades correspondientes a su rol.

El desarrollo se plantea en **9 semanas y mediante entregas progresivas**, comenzando por el modelado y la estructura del sistema y avanzando hacia el backend, frontend, integración, funcionalidades complementarias y finalmente las pruebas y el deploy.

Este enfoque permite mantener un alcance realista, validar el funcionamiento durante el desarrollo y llegar a una versión final que pueda ser utilizada y demostrada.

De esta manera, el proyecto no solo busca cumplir con los objetivos técnicos de la cursada, sino también demostrar la capacidad del grupo para **identificar una problemática, diseñar una solución, planificar su desarrollo y construir un producto funcional**.
