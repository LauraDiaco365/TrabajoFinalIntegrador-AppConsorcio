# Especificación de Requerimientos Funcionales

**Proyecto:** Sistema de Gestión de Consorcios  
**Módulo:** Documentación de Ingeniería de Software  

---

## 1. Módulo de Gestión de Usuarios , Autenticación y Control de Acceso
* **RF-01: Perfiles y Roles Unificados:**  
  El sistema debe permitir el registro y gestión de usuarios asignando de forma obligatoria uno de dos roles del sistema: `ADMINISTRADOR` o `VECINO`.

* **RF-02: Autenticación de Usuarios:**  
  El sistema debe permitir el inicio de sesión seguro mediante credenciales únicas (`username` o `email` y `password`), habilitando las funcionalidades según el rol activo.

* **RF-03: Integridad de Identidad Obligatoria (`NOT NULL`):**  
  Para la creación de cualquier perfil de usuario, el sistema exigirá obligatoriamente los campos `first_name` y `last_name`, garantizando la identificación completa de las personas ante la emisión de liquidaciones, recibos y convocatorias.

* **RF-04: Soporte Multi-unidad y Selección de Propiedad Activa:**  
  Un usuario con rol `VECINO` podrá ser propietario de una o más unidades funcionales, incluso en diferentes consorcios. El sistema permitirá al usuario seleccionar la unidad/propiedad activa sobre la cual desea operar en su sesión.

* **RF-05: Aislamiento de Visibilidad para Vecinos (Multitenancy):**  
  El sistema debe limitar el acceso del `VECINO` para que únicamente consulte la información (liquidaciones, avisos, reuniones y mantenimientos) correspondiente al consorcio de la unidad seleccionada, prohibiendo el acceso a datos de otros consorcios.

* **RF-06: Privacidad de Cuentas entre Vecinos:**  
  Un `VECINO` solo podrá visualizar sus propios comprobantes de pago y el saldo/estado de cuenta de su propia unidad funcional. El sistema no permitirá la lectura de pagos ni la información crediticia de otros vecinos.

* **RF-07: Alcance de Gestión Scoped para Administradores:**  
  Un usuario con rol `ADMINISTRADOR` solo podrá gestionar, consultar y modificar los consorcios donde figure explícitamente asignado como administrador responsable, impidiendo cualquier operación sobre consorcios ajenos.

---

## 2. Módulo de Consorcios y Unidades
* **RF-03: Administración de Consorcios:** El sistema debe permitir al usuario con rol `ADMINISTRADOR` registrar, editar y gestionar consorcios, vinculándolos a su cuenta.
* **RF-04: Registro de Unidades Funcionales:** El sistema debe permitir dar de alta unidades habitacionales asociadas a un consorcio, identificadas de manera única por la combinación de `piso` y `departamento` (`UNIQUE`), y vinculadas a un vecino propietario.
* **RF-05: Asignación de Coeficiente Fiscal:** Cada unidad funcional debe tener asignado un `porcentaje_fiscal` (`NUMERIC(5,2)`).
* **RF-06: Invariante del 100% Fiscal:** El sistema debe verificar que la suma total de los porcentajes fiscales de todas las unidades de un mismo consorcio equivalga exactamente al **100.00%**.

---

## 3. Módulo de Gestión Económica y Liquidaciones
* **RF-07: Carga de Gastos:** El sistema debe permitir al `ADMINISTRADOR` registrar gastos asociados a un consorcio y a un periodo específico, clasificándolos en `ORDINARIO` o `EXTRAORDINARIO`.
* **RF-08: Generación y Prorrateo de Liquidaciones:** El sistema debe calcular el monto de expensas correspondientes a cada unidad en función de su `porcentaje_fiscal` sobre los gastos acumulados en la liquidación mientras esta permanezca en estado `ABIERTA`.
* **RF-09: Control de Liquidación Única:** El sistema debe impedir la creación de más de una liquidación para un mismo consorcio en el mismo periodo (`mes` y `año`).
* **RF-10: Cierre e Inmutabilidad de Liquidaciones:** Al momento de pasar una liquidación de estado `ABIERTA` a `CERRADA`, el sistema debe validar automáticamente la regla del 100% de coeficiente fiscal y **congelar el `monto_total` y los gastos asociados**, garantizando la inmutabilidad de los saldos históricos.

---

## 4. Módulo de Pagos y Comprobantes
* **RF-11: Registro de Pagos:** El sistema debe permitir al `VECINO` o al `ADMINISTRADOR` registrar un pago asociado a una liquidación y a una unidad específica, capturando monto, fecha y adjuntando opcionalmente un `comprobante`.
* **RF-12: Flujo de Verificación de Pagos:** Todo pago registrado debe nacer en estado `PENDIENTE` y requerir la revisión y posterior confirmación por parte del `ADMINISTRADOR` para pasar a estado `CONFIRMADO`.
* **RF-13: Soporte de Pagos Parciales:**  
  El sistema debe permitir asociar múltiples registros de pago a una misma liquidación y unidad funcional, actualizando el saldo pendiente hasta cubrir la totalidad del monto de la expensa.

---

## 5. Módulo de Mantenimiento Edilicio
* **RF-14: Seguimiento de Reclamaciones e Incidencias:** El sistema debe permitir al `ADMINISTRADOR` dar de alta y actualizar trabajos o reparaciones edilicias para un consorcio.
* **RF-15: Traza Temporal y Operativa de Mantenimiento:** Cada registro de mantenimiento debe controlar su ciclo de vida a través de los estados (`PENDIENTE`, `EN_PROCESO`, `FINALIZADO`), registrando `fecha_solicitud`, `fecha_inicio`, `fecha_fin` y `observaciones` de avance.
* **RF-16: Costo Informativo de Mantenimiento:** El sistema permitirá registrar de forma informativa el `monto` estimado/real de la reparación en la orden de mantenimiento, manteniendo la separación funcional con el módulo de gastos para evitar duplicaciones contables.
* **RF-17: Visibilidad de Seguimiento en Modo Lectura para Vecinos:**  
  El sistema debe permitir a los usuarios con rol `VECINO` consultar y realizar el seguimiento en modo solo lectura ("read-only") de los mantenimientos registrados en su consorcio (título, monto,descripción, avance/estado, fechas de inicio y fin), proscribiendo cualquier permiso de modificación, edición o eliminación de dichos registros.

---

## 6. Módulo de Asambleas y Reuniones
* **RF-18: Convocatoria a Reuniones:** El sistema debe permitir al `ADMINISTRADOR` programar y publicar asambleas o reuniones de consorcio, especificando `titulo`, `temario`, `fecha_hora`, y `lugar_o_enlace` (presencial o virtual).
* **RF-19: Control Manual del Estado de Convocatoria:**  
  El `ADMINISTRADOR` será el único habilitado para gestionar y actualizar manualmente el ciclo de vida de la reunión entre los estados `PENDIENTE`, `FINALIZADA` y `CANCELADA`.

* **RF-20: Recepcion y Consulta de Convocatorias y Resumen de Asamblea para Vecinos:**  
  Los usuarios con rol `VECINO` recibirán y podrán consultar en su panel de usuario todas las convocatorias a asambleas programadas para su consorcio (con fecha, hora, lugar y temario propuesto). Tras la realización de la asamblea, el vecino podrá visualizar el estado final y la síntesis o puntos tratados registrados por la administración (en modo vista no edicion)

---

# Requisitos No Funcionales (RNF)

### 1. Seguridad y Privacidad
* **RNF-01 (Protección de Contraseñas):** Las contraseñas de los usuarios no deben almacenarse en texto plano bajo ninguna circunstancia. Se deben encriptar mediante algoritmos de hashing seguros (PBKDF2 / Argon2 nativo de Django).
* **RNF-02 (Seguridad por Rol / RBAC):** La aplicación debe aplicar un control de acceso basado en roles (Role-Based Access Control) tanto en la capa de vista/interfaz como a nivel de endpoints/API, garantizando el aislamiento de datos entre vecinos y la gestión exclusiva para administradores.

### 2. Integridad y Consistencia de Datos
* **RNF-03 (Consistencia Relacional):** La base de datos relacional (PostgreSQL) debe aplicar restricciones de clave foránea (`FOREIGN KEY`), restricciones de unicidad (`UNIQUE`) y restricciones de chequeo de valores (`CHECK`) para evitar la inconsistencia de datos a nivel de motor.
* **RNF-04 (Inmutabilidad Contable):** El sistema debe garantizar transaccionalmente que los registros financieros asociados a una liquidación en estado `CERRADA` no puedan ser alterados ni eliminados.

### 3. Usabilidad e Interfaz
* **RNF-05 (Diseño Responsivo):** La interfaz web debe ser adaptable y legible tanto en navegadores de escritorio como en dispositivos móviles (smartphones y tablets), facilitando el uso por parte de los vecinos para el envío de comprobantes de pago.

### 4. Mantenibilidad y Arquitectura
* **RNF-06 (Arquitectura en Capas):** El sistema debe desarrollarse siguiendo el patrón de diseño MVT (Model-View-Template) de Django, manteniendo una clara separación entre los modelos de datos, la lógica de negocio y la capa de presentación.
* **RNF-07 (Trazabilidad y Auditoría):** Todas las tablas principales de la base de datos deben contar con campos de control de auditoría para rastrear el ciclo de vida de los datos (`fecha_creacion`, `registrado_por` o timestamps de estado).

---

#  Matriz de Permisos por Rol (RBAC)

La siguiente tabla especifica la matriz de Control de Acceso Basado en Roles (Role-Based Access Control) aplicada en los módulos del sistema:

| Módulo / Entidad | Operación / Acción | ADMINISTRADOR | VECINO | Observaciones y Límites de Visibilidad |
| :--- | :--- | :---: | :---: | :--- |
| **Usuarios** | Registro / Login | **CRUD** | Login | El Vecino solo gestiona su perfil. |
| **Consorcios** | Gestión de Consorcio | **CRUD** | Lectura | El Vecino solo lee datos del consorcio donde posee unidad. |
| **Unidades** | Asignación y Coeficientes | **CRUD** | Lectura | El Vecino solo ve los datos de su propia unidad. |
| **Gastos** | Carga y Clasificación | **CRUD** | - | Exclusivo del Administrador. |
| **Liquidaciones** | Generación y Cierre | **CRUD** | Lectura | Al pasar a `CERRADA`, el Admin pierde permisos de edición. |
| **Pagos** | Carga de Comprobante | Crear / Confirmar | Crear | El Vecino registra el pago; el Admin aprueba o rechaza. |
| **Pagos (Historial)** | Consulta de Pagos | Ver Todo | Propio | El Vecino **no** ve pagos ni deudas de otros vecinos. |
| **Mantenimiento** | Control de Obras/Costos | **CRUD** | Lectura | El Vecino realiza seguimiento en modo *solo lectura*. |
| **Reuniones** | Convocatoria y Estado | **CRUD** | Lectura | El Vecino recibe la convocatoria y lee el acta/resumen. |

*Leyenda: **CRUD** (Crear, Leer, Actualizar, Eliminar/Inactivar) | **-** (Sin acceso)*

---

# Casos de Uso y Flujos de Procesos Principales

### **CU-00: Registro e Inicialización de Usuario y Perfil (Onboarding)**
* **Actor Principal:** Usuario (Administrador / Vecino)
* **Actores Secundarios:** Sistema
* **Precondición:** Ninguna (Acceso público al módulo de registro/alta).
* **Flujo Principal:**
  1. El Usuario ingresa al formulario de registro.
  2. El Usuario completa sus credenciales obligatorias (`username`, `email`, `password`) y sus datos personales de identidad obligatorios (`first_name`, `last_name`). Opcionalmente ingresa su `telefono`.
  3. El Usuario selecciona el perfil/rol a solicitar o el Sistema le asigna el rol correspondiente (`ADMINISTRADOR` o `VECINO`).
  4. El Sistema valida que `username` y `email` no existan previamente en la base de datos (`UNIQUE`).
  5. El Sistema aplica el hash seguro sobre la contraseña (PBKDF2/Argon2) y persiste el registro en `usuarios_usuario` con estado `is_active = True`.
* **Flujos Alternativos / Excepciones:**
  * *2a. Campos Obligatorios Incompletos:* Si falta `first_name` o `last_name`, el Sistema rechaza el registro exigiendo la identificación completa.
  * *4a. Credenciales Duplicadas:* El Sistema advierte que el `username` o `email` ya se encuentra registrado y solicita corregir el formulario.

---

### **CU-00B: Alta de Consorcio y Catastro de Unidades Funcionales**
* **Actor Principal:** Administrador
* **Actores Secundarios:** Sistema
* **Precondición:** El Administrador ha iniciado sesión y cuenta con el rol `ADMINISTRADOR`.
* **Flujo Principal:**
  1. El Administrador registra un nuevo consorcio cargando `nombre`, `direccion`, `cuit` y `cantidad_unidades`. El Sistema lo vincula a su `administrador_id`.
  2. El Administrador procede a dar de alta las unidades funcionales del consorcio una a una.
  3. Para cada unidad, ingresa `piso`, `departamento`, selecciona el usuario `VECINO` propietario y asigna su `porcentaje_fiscal`.
  4. El Sistema valida la restricción de unicidad `UNIQUE (consorcio_id, piso, departamento)`.
  5. Una vez cargadas todas las unidades, el Sistema calcula la suma acumulada de los coeficientes fiscales.
  6. Si $\sum \text{porcentaje\_fiscal} = 100.00\%$, el catastro del consorcio queda habilitado para la emisión de liquidaciones.
* **Flujos Alternativos / Excepciones:**
  * *4a. Unidad Duplicada:* El Sistema rechaza el alta si ya existe una unidad con el mismo piso y departamento en ese consorcio.
  * *6a. Coeficiente Fiscal Desbalanceado ($\neq 100.00\%$):* El Sistema advierte al Administrador el porcentaje faltante o excedente y bloquea el inicio del periodo de liquidación hasta que se corrija el prorrateo.

---

### **CU-01: Ciclo de Vida de Liquidación y Expensas**
* **Actor Principal:** Administrador
* **Actores Secundarios:** Vecino, Sistema
* **Precondición:** El consorcio tiene configuradas sus unidades con la suma del 100% de coeficiente fiscal.
* **Flujo Principal:**
  1. El Administrador abre una nueva liquidación para el consorcio en el periodo (`mes`/`año`).
  2. El Administrador registra los gastos del periodo clasificándolos como `ORDINARIO` o `EXTRAORDINARIO`.
  3. El Administrador solicita el **Cierre de Liquidación**.
  4. El Sistema valida que la suma de coeficientes de las unidades dé exactamente `100.00%`.
  5. El Sistema calcula el monto de expensa correspondiente a cada unidad (`porcentaje_fiscal` $\times$ `monto_total_gastos`).
  6. El Sistema cambia el estado de la liquidación a `CERRADA` y congela los gastos y montos totales (inmutabilidad).
  7. El Sistema publica las expensas habilitando la visibilidad para los Vecinos.
* **Flujos Alternativos / Excepciones:**
  * *4a. La suma de coeficientes es distinta del 100%:* El Sistema rechaza el cierre y muestra un mensaje de error exigiendo regularizar las unidades.

---

### **CU-02: Registro y Confirmación de Pago de Expensas**
* **Actor Principal:** Vecino
* **Actores Secundarios:** Administrador, Sistema
* **Precondición:** Existe una liquidación en estado `CERRADA` con saldo pendiente para la unidad activa del Vecino.
* **Flujo Principal:**
  1. El Vecino selecciona su propiedad activa y consulta las expensas adeudadas.
  2. El Vecino registra un pago ingresando monto, fecha y adjuntando opcionalmente el comprobante de transferencia.
  3. El Sistema registra el pago en estado `PENDIENTE`.
  4. El Administrador ingresa al panel de verificación de pagos de su consorcio y revisa el comprobante.
  5. El Administrador aprueba el pago cambiando su estado a `CONFIRMADO`.
  6. El Sistema recalcula el saldo adeudado de la unidad ($\text{Monto Expensa} - \sum \text{Pagos Confirmados}$).
* **Flujos Alternativos / Excepciones:**
  * *2a. Pago Parcial:* El Vecino ingresa un monto menor al total de la expensa. El Sistema lo acepta y recalcula el saldo restante pendiente.
  * *5a. Comprobante Inválido/Rechazado:* El Administrador rechaza el pago. El saldo adeudado del Vecino no se reduce y el pago pasa a estado `RECHAZADO`.

---

### **CU-03: Seguimiento de Mantenimiento Edilicio**
* **Actor Principal:** Administrador
* **Actores Secundarios:** Vecino
* **Flujo Principal:**
  1. El Administrador registra una nueva orden de reparación/mantenimiento (título, descripción, fecha inicio, estado `PENDIENTE` y monto estimado).
  2. El Administrador actualiza el estado a `EN_PROCESO` a medida que inician las obras.
  3. Los Vecinos del consorcio ingresan a su sección de Mantenimiento y consultan en modo *solo lectura* la evolución del trabajo.
  4. El Administrador finaliza la obra cargando la fecha de fin y actualizando el estado a `FINALIZADO`.

---

### **CU-04: Convocatoria y Cierre de Asamblea de Consorcio**
* **Actor Principal:** Administrador
* **Actores Secundarios:** Vecino
* **Flujo Principal:**
  1. El Administrador crea una convocatoria registrando título, temario propuesto, fecha, hora y enlace/lugar.
  2. El Sistema publica la reunión en estado `PENDIENTE` y la hace visible en el panel de todos los Vecinos del consorcio.
  3. Los Vecinos reciben y consultan la fecha, hora y temario en su panel para asistir.
  4. Una vez realizada la reunión, el Administrador cambia el estado a `FINALIZADA` e ingresa el resumen o acta de la asamblea.
  5. Los Vecinos consultan la síntesis de lo acordado en modo *solo lectura*.