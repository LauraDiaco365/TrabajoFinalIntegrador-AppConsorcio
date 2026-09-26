# 📐 Decisiones de Diseño y Registro de Cambios — Consorcio360

Este documento recopila las decisiones de arquitectura, diseño de datos, ajuste de alcance y el registro de cambios (changelog) realizados a partir de las observaciones de las entregas académicas.

---

## 1. Registro de Cambios y Ajustes (Changelog)

### 📩 Ajustes respecto a la Devolución de la Entrega 1
* **Definición del Stack Tecnológico:** A partir de las observaciones de la primera entrega, se acotó y simplificó el stack de tecnologías. Se resolvió postergar tecnologías complejas que figuraban en la propuesta inicial (tales como Celery, Redis, almacenamiento en MinIO/S3 y TypeScript) para enfocarse en un MVP robusto basado en **Python 3.12, Django, Django REST Framework, React y PostgreSQL**.

### 📩 Ajustes respecto a la Devolución de la Entrega 2
* **Incorporación de las apps `mantenimientos` y `reunions` al Diseño:** Se identificó que ambas apps ya existían creadas en el repositorio de Django pero carecían de definición en el Diagrama ER y en las reglas de negocio. Se tomó la decisión explícita de **mantener ambas apps dentro del alcance del proyecto**, completando su modelado conceptual en esta instancia de diseño sin realizar codificación.
* **Consolidación del Alcance y Limpieza:** Se archivó el borrador inicial (`README_anterior.md`) dentro de `docs/historial/` para eliminar contradicciones y se estableció el `README.md` principal como único documento de alcance vigente.
* **Higiene del Repositorio y Versionado (Git):** En respuesta al punto de higiene del repositorio, se procedió a incorporar un archivo `.gitignore` técnico adecuado para proyectos Python/Django y React. Asimismo, se removieron del seguimiento de Git (tracking) la carpeta de entorno virtual `venv/`, los archivos de base de datos local `*.sqlite3`, las carpetas de caché `__pycache__/` y de entorno `.env`, garantizando que solo permanezca en el repositorio el código fuente y la documentación técnica.
* **Proceso de Diseño vs. Codificación:** Se toma nota de la observación de la tutora respecto al código de prueba previo (modelos y tests de prorrateo). Se establece el compromiso explícito de no continuar con la etapa de codificación (Frontend, Backend o lógica) hasta que el diseño y la documentación de esta segunda entrega estén completamente aprobados.

---

## 2. Decisiones de Alcance del MVP

El alcance del proyecto fue refinado deliberadamente para garantizar la entrega de un sistema 100% funcional y probado en el tiempo académico disponible.

### Funcionalidades dentro del MVP actual:
* **Autenticación y Roles:** Usuarios con rol Administrador y Vecino (modelo único de Usuario).
* **Gestión de Consorcios y Unidades:** Alta de consorcios y asignación de unidades con porcentaje fiscal.
* **Gestión Económica:** Registro de gastos, generación de liquidaciones mensuales, cálculo automático de prorrateo (campo no persistido) y registro de pagos simulados.
* **Mantenimientos (Módulo en diseño):** Seguimiento del estado operativo de los arreglos del edificio mediante semáforo de estados.
* **Reuniones (Módulo en diseño):** Convocatoria a reuniones de vecinos con orden del día/temario.

### Funcionalidades diferidas (Mejoras Futuras fuera del MVP):
* Integración con servicios de almacenamiento externo (MinIO / S3) para fotos y archivos de actas.
* Tareas automáticas y diferidas con Celery + Redis.
* Pagos reales mediante pasarelas de pago o APIs bancarias.
* Votaciones complejas en línea y firma digital.

---

## 3. Modelo de Datos: Módulos Mantenimientos y Reuniones

En respuesta al requerimiento de la 2.ª entrega, se detalla el diseño conceptual de los modelos correspondientes a las apps `mantenimientos` y `reunions`.

### A. Módulo `mantenimientos`

* **Propósito:** Permitir al administrador registrar y realizar el seguimiento de los arreglos o tareas operativas dentro del consorcio, brindando visibilidad a los vecinos.
* **Entidad `Mantenimiento`:**
  * `id`: Identificador único (PK).
  * `consorcio_id`: Referencia al consorcio (FK).
  * `titulo`: Título descriptivo de la tarea (ej. "Reparación de bomba de agua").
  * `descripcion`: Detalle del trabajo a realizar.
  * `observaciones`: Campo de texto libre para notas de seguimiento, novedades o datos del proveedor.
  * `estado`: Estado de la tarea mediante semáforo (`pendiente`, `en_proceso`, `finalizado`).
  * `fecha_inicio`: Fecha de inicio o programación.
  * `fecha_fin`: Fecha de finalización (opcional/null si está pendiente).

* **Reglas de negocio:**
  * Un consorcio gestiona múltiples mantenimientos.
  * Los mantenimientos reflejan la operatividad del edificio; en esta etapa no generan cargos económicos automáticos en la liquidación de expensas.

---

### B. Módulo `reunions`

* **Propósito:** Permitir al administrador convocar a asambleas o reuniones de consorcio y publicar el temario para conocimiento de los vecinos.
* **Entidad `Reunion`:**
  * `id`: Identificador único (PK).
  * `consorcio_id`: Referencia al consorcio (FK).
  * `titulo`: Título o motivo de la reunión.
  * `fecha_hora`: Fecha y hora programada.
  * `lugar_o_enlace`: Ubicación física (ej. "SUM del edificio") o enlace simple para reunión virtual.
  * `temario`: Lista de puntos u orden del día a tratar durante la reunión.
  * `estado`: Estado de la convocatoria (`programada`, `realizada`, `cancelada`).

* **Reglas de negocio:**
  * Un consorcio convoca múltiples reuniones.
  * La entidad se limita a la convocatoria e información previa a tratar (temario), dejando la gestión de actas escaneadas o archivos adjuntos para etapas de mejoras futuras.