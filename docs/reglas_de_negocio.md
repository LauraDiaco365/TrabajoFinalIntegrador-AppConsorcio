# Reglas de Negocio (RN) - Sistema de Gestión de Consorcios

Este documento especifica las restricciones operativas, contables y de dominio que rigen la lógica del backend y la base de datos PostgreSQL.

---

## 1. Reglas de Estructura y Catastro (Consorcios y Unidades)

* **RN-01 (Asignación de Administración):**  
  Un usuario con rol `ADMINISTRADOR` puede gestionar múltiples consorcios, pero un consorcio solo pertenece a un administrador responsable a la vez.

* **RN-02 (Invariante Fiscal del 100%):**  
  La suma acumulada de los coeficientes fiscales (`porcentaje_fiscal`) de todas las unidades funcionales de un mismo consorcio debe ser estrictamente igual a `100.00%`.  
  * *Enforcement:* El sistema valida este balance en el modelo/backend e impide habilitar la emisión o cierre de liquidaciones si la suma no es exacta.

* **RN-03 (Unicidad Territorial de Unidad):**  
  Dentro de un mismo consorcio, no pueden existir dos unidades funcionales con la misma combinación de piso y departamento.  
  * *Enforcement:* Restricción de base de datos `UNIQUE (consorcio_id, piso, departamento)`.

* **RN-04 (Multi-unidad y Propiedad Activa):**  
  Un `VECINO` puede ser propietario de una o más unidades funcionales (departamentos, cocheras, bauleras) en el mismo o en distintos consorcios. La sesión del vecino opera en base a una "Unidad Activa" seleccionada para garantizar el filtrado correcto de datos.

---

## 2. Reglas Económicas, Liquidaciones y Expensas

* **RN-05 (Unicidad de Liquidación por Periodo):**  
  No puede existir más de una liquidación registrada para el mismo consorcio en el mismo mes y año.  
  * *Enforcement:* Restricción de base de datos `UNIQUE (consorcio_id, mes, año)`.

* **RN-06 (Inmutabilidad Contable al Cierre):**  
  Una liquidación inicia en estado `ABIERTA` (borrador). Al cambiar a estado `CERRADA`, el `monto_total` y los registros de `GASTO` asociados se congelan de forma inalterable. Se prohíbe la adición, edición o eliminación de gastos en liquidaciones cerradas.

* **RN-07 (Cálculo de Expensa Individual):**  
  El monto de expensa asignado a cada unidad funcional en una liquidación cerrada se calcula como:  
  $$\text{Monto Expensa} = \text{Monto Total Gastos} \times \left( \frac{\text{porcentaje\_fiscal}}{100} \right)$$

---

## 3. Reglas de Pagos y Comprobantes

* **RN-08 (Flujo de Confirmación de Pagos):**  
  Todo registro de pago efectuado por un `VECINO` ingresa con el estado `PENDIENTE`. El monto pagado solo impacta contablemente en el saldo de la unidad cuando el `ADMINISTRADOR` cambia el estado a `CONFIRMADO`.

* **RN-09 (Soporte de Pagos Parciales):**  
  Una liquidación y unidad funcional aceptan múltiples registros de pago (relación $1:N$). El saldo adeudado de la unidad para el periodo se calcula dinámicamente como:  
  $$\text{Saldo Pendiente} = \text{Monto Expensa} - \sum \text{Pagos Confirmados}$$

---

## 4. Reglas de Mantenimiento y Convocatorias

* **RN-10 (Read-Only de Vecinos en Mantenimiento):**  
  Los registros de reparaciones edilicias son gestionados operativamente por el `ADMINISTRADOR`. Los usuarios `VECINO` tienen permiso exclusivamente de lectura ("read-only") para el seguimiento de obras.

* **RN-11 (Ciclo de Vida Manual de Asambleas):**  
  El estado de las convocatorias a reuniones (`PENDIENTE`, `FINALIZADA`, `CANCELADA`) es gestionado manualmente por el `ADMINISTRADOR`. Al pasar a `FINALIZADA`, es obligatorio registrar la síntesis/acta con los puntos tratados para consulta de los vecinos.
  * **RN-12 (Imputación de Gastos Extraordinarios en Cuotas):**  
  Los gastos extraordinarios que se financien o prorrateen en múltiples periodos se registrarán en la liquidación correspondiente a cada mes por el valor de la cuota individual a liquidar en dicho periodo (ejemplo: *"Reparación de Ascensor - Cuota 1/6"*). La liquidación mensual procesará exclusivamente el monto imputable al periodo en curso.