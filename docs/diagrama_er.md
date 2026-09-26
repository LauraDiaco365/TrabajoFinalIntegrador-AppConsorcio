# 🗄️ Esquema de Base de Datos - Diagrama ER

Este documento contiene la representación visual y formal del Modelo Entidad-Relación (ER) para las 5 apps del sistema (`usuarios`, `consorcios`, `economia`, `mantenimientos`, `reunions`).

```mermaid
erDiagram
    %% App usuarios
    USUARIO {
        bigint id PK
        string username
        string email
        string password
        string rol "ADMINISTRADOR | VECINO"
        string first_name
        string last_name
        string telefono
        boolean is_active
        datetime date_joined
    }

    %% App consorcios
    CONSORCIO {
        bigint id PK
        string nombre
        string direccion
        string cuit
    }

    UNIDAD {
        bigint id PK
        bigint consorcio_id FK
        bigint usuario_id FK
        string piso
        string departamento
        decimal porcentaje_fiscal
    }

    %% App economia
    GASTO {
        bigint id PK
        bigint consorcio_id FK
        string concepto
        decimal monto
        date fecha
    }

    LIQUIDACION {
        bigint id PK
        bigint consorcio_id FK
        int mes
        int anio
        decimal monto_total
    }

    PAGO {
        bigint id PK
        bigint unidad_id FK
        bigint liquidacion_id FK
        decimal monto
        datetime fecha_pago
        string comprobante
    }

    %% App mantenimientos (Diseñado / Pausado)
    MANTENIMIENTO {
        bigint id PK
        bigint consorcio_id FK
        string titulo
        string descripcion
        string estado "PENDIENTE | EN_PROCESO | FINALIZADO"
        datetime fecha_creacion
    }

    %% App reunions (Diseñado / Pausado)
    REUNION {
        bigint id PK
        bigint consorcio_id FK
        datetime fecha_hora
        string orden_del_dia
        string canal_enlace
    }

    %% Relaciones
    USUARIO ||--o{ UNIDAD : "posee / habita"
    CONSORCIO ||--|{ UNIDAD : "contiene"
    CONSORCIO ||--o{ GASTO : "registra"
    CONSORCIO ||--o{ LIQUIDACION : "genera"
    CONSORCIO ||--o{ MANTENIMIENTO : "requiere"
    CONSORCIO ||--o{ REUNION : "convoca"
    UNIDAD ||--o{ PAGO : "realiza"
    LIQUIDACION ||--o{ PAGO : "recibe"