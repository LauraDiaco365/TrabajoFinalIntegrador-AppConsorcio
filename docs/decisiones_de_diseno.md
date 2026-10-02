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

  ### 📩 Ajustes respecto a la Devolución de la Entrega 2 (parte2)
A partir de las observaciones realizadas por la tutora en la devolución de la segunda entrega, se llevaron a cabo ajustes integrales en el proyecto. 

En primer lugar, se trabajó en la **unificación del diseño y modelo de la base de datos**, dado que se detectaron inconsistencias y contradicciones entre el `README.md`, el esquema SQL (`database/schema.sql`), el diagrama ER (`docs/diagrama_er.md`) y el código del backend. 

Para resolver esto, se estableció **`docs/diagrama_er.md` como la única fuente de verdad oficial** para las especificaciones del modelo de datos. En consecuencia, el `README.md` fue modificado para apuntar directamente a dicha documentación en lugar de duplicar el diagrama, garantizando que el `schema.sql` y las futuras actualizaciones del código sigan estrictamente los lineamientos allí definidos.

---

### 1. Modificaciones en el Modelo de Datos

#### 1.1. Entidad UNIDAD (`consorcios_unidad`)
* **Unificación de atributos de localización:** Se consolidó el uso exclusivo de los campos `piso` y `departamento` para la identificación física de la unidad dentro de un consorcio.
* **Redefinición de la clave foránea a Propietario:** Se renombró la relación `usuario_id` a `propietario_id` (`nullable`) en `schema.sql` y en la documentación oficial, clarificando que representa la titularidad legal de la unidad.
* **Restricción de unicidad:** Se definió la restricción compuesta `UNIQUE (consorcio_id, piso, departamento)` para evitar duplicación de unidades en un mismo consorcio.
* **Soporte para múltiples propiedades:** Se explicitó que el campo `propietario_id` no posee restricción `UNIQUE`, permitiendo que un mismo usuario/propietario sea dueño de múltiples unidades dentro del mismo consorcio o en consorcios distintos.
* **Atributo `porcentaje_fiscal`:** Se definió el tipo de dato `NUMERIC(5, 2)` para permitir decimales precisos. Se estableció la regla de integridad de negocio donde la suma de los porcentajes fiscales de todas las unidades de un mismo consorcio debe totalizar exactamente el 100.00%.
#### 1.2. Entidad CONSORCIO (`consorcios_consorcio`)
* **Relación con Administrador:** Se agregó el campo `administrador_id` (FK a `usuarios_usuario`) para vincular formalmente cada consorcio con su administrador.
* **Soporte multiconsorcio:** Se estableció que `administrador_id` no posee restricción `UNIQUE`, dando soporte a la regla de negocio de que un único usuario administrador puede gestionar múltiples consorcios.
#### 1.3. Entidad GASTO (`economia_gasto`)
* **Unificación de atributos:** Se adoptó `descripcion` como campo oficial para el detalle del gasto.
* **Inclusión del tipo de gasto:** Se incorporó el campo `tipo` (`ordinario` / `extraordinario`) en `schema.sql`, `diagrama_er.md` y documentación, dando cumplimiento al alcance funcional para la distinción de expensas.
* **Ciclo de vida y asociación a Liquidación (`liquidacion_id`):** Se confirmó la clave foránea `liquidacion_id` (`nullable`). Cuando el administrador registra un gasto diario, el campo nace nulo (`NULL`). Cuando se procesa o liquida el mes, dichos gastos se asocian oficialmente a la `liquidacion_id` correspondiente, quedando vinculados de forma inmutable al momento de cerrar la liquidación.
* **Estandarización de Enums/CHECK en SQL:** Se definió que los valores de tipo Enum/CHECK en el DDL de PostgreSQL irán formalmente en mayúsculas (por ejemplo, `'ORDINARIO'`, `'EXTRAORDINARIO'`), garantizando la compatibilidad y convención estándar de bases de datos relacionales.
#### 1.4. Entidad LIQUIDACIÓN (`economia_liquidacion`) y Regla de Cierre
* **Inclusión del campo `estado`:** Se incorporó la columna `estado` (`ABIERTA` / `CERRADA`) en `schema.sql` y `diagrama_er.md`.
* **Corrección de la postura sobre `monto_total` y Prorrateo:**
  * **Aclaración sobre la observación del README:** Anteriormente, el `README.md` indicaba que el prorrateo se calculaba únicamente de forma dinámica y no se persistía en la base de datos. Sin embargo, se identificó que este enfoque provocaba un fallo de integridad: cualquier modificación o carga posterior de un gasto en una liquidación pasada alteraba retroactivamente las deudas y expensas históricas de los vecinos.
  * **Nuevo criterio adoptado:** Se decidió **persistir el `monto_total`** en la tabla `economia_liquidacion`. 
  * **Funcionamiento:** Mientras la liquidación permanece `ABIERTA`, el importe a pagar por cada unidad se calcula dinámicamente según su porcentaje fiscal sobre los gastos vigentes. Al pasar al estado `CERRADA`, el sistema congela y guarda de forma definitiva el `monto_total` y la lista de gastos asociados, garantizando la inmutabilidad de los saldos e importes históricos emitidos.
  **Validación de la regla del 100% en Porcentaje Fiscal:** Se definió la regla de negocio que exige que la suma de los campos `porcentaje_fiscal` de todas las unidades pertenecientes a un mismo consorcio debe ser exactamente igual a 100.00% ($\sum = 100.00\%$). El backend validará esta condición previa al procesamiento y cierre de la liquidación para asegurar un prorrateo matemáticamente exacto. Si la suma no alcanza o excede el 100.00%, la aplicación bloqueará la operación y notificará al administrador.
  **Soporte Relacional de Pagos Parciales:** La relación $1:N$ entre `LIQUIDACION` y `PAGO` permite registrar múltiples cobros para una misma expensa de la unidad. El saldo pendiente se calcula dinámicamente como $\text{Monto Expensa} - \sum \text{Pagos Confirmados}$, habilitando pagos en cuotas o adelantos.
* **Restricción de periodo único:** Se agregó la restricción `UNIQUE (consorcio_id, mes, anio)` para evitar liquidaciones duplicadas en un mismo mes/año para un consorcio.
#### 1.5. Entidad PAGO (`economia_pago`)
* **Inclusión de `estado` y flujo de verificación:** Se incorporó el campo `estado` (`pendiente` / `confirmado`) con valor por defecto `'pendiente'` en `schema.sql`, `diagrama_er.md` y `README.md`. Esto respalda la regla de negocio donde el pago registrado por el vecino requiere la posterior verificación y confirmación del administrador.
* **Unificación de atributos de auditoría y respaldo:** Se consolidaron los campos `comprobante` (referencia al archivo o comprobante adjunto, `nullable`) y `registrado_por` (FK a `usuarios_usuario`, `nullable`) para unificar la trazabilidad entre DDL, diagramas y documentación.
#### 1.6. Entidad MANTENIMIENTO (`mantenimiento_mantenimiento`)
* **Inclusión de `estado` y semáforo de seguimiento:** Se incorporó el campo `estado` (`pendiente` / `en_proceso` / `finalizado`) con valor por defecto `'pendiente'` en `schema.sql`, `diagrama_er.md` y `README.md`.
* **Incorporación de `monto` y deslinde contable:** Se agregó la columna `monto` (`NUMERIC(12, 2)`, `nullable`) para registrar el costo presupuestado/estimado de la obra o reparación edilicia. Se aclaró la regla de negocio: este campo es meramente informativo dentro del módulo de mantenimiento para dar visibilidad al vecino, evitando la duplicación contable ya que la erogación real se liquida formalmente a través de la entidad `GASTO` (`economia_gasto`).
* **Seguimiento temporal con `fecha_solicitud`, `fecha_inicio` y `fecha_fin`:** Se incorporó `fecha_solicitud` (`DATE`, por defecto la fecha actual), junto con `fecha_inicio` y `fecha_fin` (`DATE`, `nullable`) para controlar con precisión las distintas etapas del ciclo de vida de la reparación.
* **Incorporación de `observaciones`:** Se agregó el campo `observaciones` (`TEXT`, `nullable`) para permitir anotaciones operativas y notas de avance por parte del administrador.
#### 1.7. Entidad REUNIÓN (`reuniones_reunion`)
* **Inclusión de `estado` y ciclo de vida:** Se incorporó la columna `estado` (`pendiente` / `finalizada` / `cancelada`) con valor por defecto `'pendiente'` en `schema.sql`, `diagrama_er.md` y `README.md` para reflejar el estado operativo de la asamblea o reunión de consorcio.
* **Consolidación de campos de convocatoria:** Se estandarizaron las columnas `temario` (`TEXT`) y `lugar_o_enlace` (`VARCHAR(255)`, `nullable`), permitiendo gestionar tanto asambleas presenciales como encuentros virtuales asi como tambien listar los temas a tratar en la misma
* **Estandarización temporal:** Se definió la fecha y hora mediante `TIMESTAMP WITH TIME ZONE` para garantizar la correcta precisión horaria del encuentro.
#### 1.8. Entidad USUARIO (`usuarios_usuario`)
* **Incorporación de restricción `CHECK` en `rol`:** Se agregó la restricción `CHECK (rol IN ('administrador', 'vecino'))` con valor por defecto `'vecino'` en `schema.sql` y `diagrama_er.md` para garantizar la integridad de los perfiles de acceso.
* **Integridad de Identidad (`NOT NULL`):** Se definió la obligatoriedad estricta (`NOT NULL`) en los campos `first_name` y `last_name`, garantizando que todo usuario (vecino o administrador) esté plenamente identificado para la emisión de liquidaciones, recibos y convocatorias.
* **Compatibilidad con `AbstractUser` de Django:** Se alineó la DDL manteniendo las columnas del modelo de autenticación personalizado (`username`, `email`, `password`, `is_superuser`, `is_staff`, `is_active`, `date_joined`, `last_login`, `telefono`) asegurando restricciones de unicidad (`UNIQUE`) en `username` y `email`.

## 📝 Registro de Decisiones de Arquitectura y stack tecnologico
### 1. Reorganización de la Estructura del Backend y `manage.py`
- **Observación:** Existían inconsistencias en la ubicación de `manage.py` dentro de la carpeta `config/` y la falta de coincidencia entre la documentación del README y el árbol real.
- **Resolución:** 
  - Se reubicó `manage.py` en la raíz del directorio `backend/` (a la par de las aplicaciones y la carpeta `config/`), alineándolo al estándar oficial de Django.
  - Se vinculó explícitamente `manage.py` con `config.settings`.
  - Se actualizó el mapa del repositorio en el `README.md` reflejando de forma fidedigna la estructura física final.

### 2. Simplificación de Infraestructura y Eliminación de Servicios Heredados
- **Observación:** El repositorio conservaba servicios inactivos (Redis, MinIO) y la configuración de `docker-compose.yml` en conflicto con las decisiones de diseño expuestas.
- **Resolución:** 
  - Se eliminó el archivo `docker-compose.yml` para evitar sobre-ingeniería (*scope creep*).
  - El entorno local pasó a operar mediante entornos virtuales nativos (`venv`) y PostgreSQL local.
  - El almacenamiento de archivos e imágenes se gestiona directamente mediante `Pillow` y el sistema de archivos de Django (`MEDIA_ROOT`), descartando dependencias de MinIO/Redis.

### 3. Exclusión Estricta de Entornos Locales en Versionado
- **Observación:** Riesgo de subir binarios o bases de datos locales de prueba al repositorio de Git.
- **Resolución:** Inclusión explícita en `.gitignore` de la carpeta del entorno virtual (`venv/`) y la base de datos de pruebas locales (`db.sqlite3`), garantizando que la instalación limpia se ejecute desde `requirements.txt` y la base de datos relacional PostgreSQL.

### 4. Depuración de Dependencias y Sincronización de Testing (`requirements.txt` y Pytest)
- **Observación:** Faltaba `pytest` en `requirements.txt` a pesar de estar mencionado en la documentación, y existía duplicación en el driver de PostgreSQL (`psycopg` vs `psycopg-binary`).
- **Resolución:** 
  - Se unificó el conector a PostgreSQL conservando únicamente `psycopg-binary`.
  - Se incorporaron `pytest` y `pytest-django` al `requirements.txt`.
  - Se agregó el archivo `pytest.ini` en la raíz de `backend/` para conectar el runner de pruebas con `config.settings`, manteniendo compatibilidad total con la suite basada en `django.test.TestCase`.
  ### 5. Actualización y Estandarización de la Guía de Instalación Local (`README.md`)
- **Observación de la Cátedra:** La versión anterior del instructivo de instalación incluía pasos obsoletos vinculados a `docker compose up -d`, referencias a bases de datos opcionales en SQLite y comandos ejecutados sin especificar el directorio activo, lo que generaba ambigüedad en la ejecución de `manage.py` y en la gestión de dependencias.
- **Justificación del Cambio:**
  - **Alineación con la arquitectura nativa:** Se reestructuró la guía paso a paso reflejando la eliminación de Docker y formalizando el uso de **Python 3.12 (`venv`)** y **PostgreSQL 16** nativo en el puerto `5432`.
  - **Claridad operativa y navegación de directorios:** Se explicitó la navegación previa al directorio `backend/` para ejecutar los comandos de Django (`manage.py migrate`, `createsuperuser`, `runserver`) desde su ubicación física correcta, así como el uso de `requirements.txt`.
  - **Inclusión del entorno Frontend:** Se incorporó de forma transparente el flujo para React 18 + Vite (`cd frontend`, `npm install`, `npm run dev`) indicando expresamente el uso de una segunda terminal en paralelo para mantener ambos servicios activos (`localhost:8000` y `localhost:5173`).
  - **Verificación de Calidad:** Se integró la ejecución opcional del comando `pytest` dentro del flujo de setup del backend, permitiendo a la cátedra validar de forma inmediata la suite de pruebas unitarias al clonar el proyecto.
  ### 6. Desacoplamiento de Credenciales Sensibles mediante Variables de Entorno
- **Observación de la Cátedra:** Existían credenciales de base de datos escritas directamente en texto plano (*hardcoded*) dentro de `settings.py`, sin hacer uso efectivo de la librería `python-decouple` declarada en las dependencias.
- **Resolución y Refactorización:**
  - **Refactor de `settings.py`:** Se parametrizaron `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, el bloque de `DATABASES` (PostgreSQL) y la lista de orígenes permitidos en `CORS_ALLOWED_ORIGINS` utilizando la librería `decouple.config`.
  - **Creación de `.env.example`:** Se incorporó una plantilla pública de configuración en la raíz del backend (`backend/.env.example`) que documenta las claves necesarias para la inicialización del entorno.
  - **Protección de Secretos:** Se reforzó la regla en `.gitignore` para garantizar que el archivo `.env` local (con credenciales reales) nunca sea subido al repositorio de versionado.