# 🗄️ Esquema de Base de Datos - Diagrama ER

Este documento contiene la representación visual y formal del Modelo Entidad-Relación (ER) para las 5 apps del sistema (`usuarios`, `consorcios`, `economia`, `mantenimientos`, `reunions`).

```mermaid
erDiagram
    %% App usuarios
   USUARIO {
        bigint id PK
        string username UK
        string email UK
        string first_name
        string last_name
        string password
        string rol "administrador / vecino"
        string telefono "nullable"
        boolean is_active
        boolean is_staff
        boolean is_superuser
        datetime date_joined
        datetime last_login "nullable"
    }

    %% App consorcios
   CONSORCIO {
        bigint id PK
        string nombre
        string direccion
        string cuit
        bigint administrador_id FK "nullable"
    }

    UNIDAD {
        bigint id PK
        bigint consorcio_id FK
        bigint propietario_id FK "nullable"
        string piso
        string departamento
        decimal porcentaje_fiscal
    }

    %% App economia
   GASTO {
        bigint id PK
        bigint consorcio_id FK
        bigint liquidacion_id FK "nullable"
        string descripcion
        decimal monto
        date fecha
        string tipo "ordinario / extraordinario"
    }

  LIQUIDACION {
        bigint id PK
        bigint consorcio_id FK
        int mes
        int anio
        decimal monto_total
        string estado "abierta / cerrada"
    }

    PAGO {
        bigint id PK
        bigint unidad_id FK
        bigint liquidacion_id FK
        bigint registrado_por FK "nullable"
        decimal monto
        date fecha_pago
        string comprobante "nullable"
        string estado "pendiente / confirmado"
    }

    %% App mantenimientos (Diseñado / Pausado)
    MANTENIMIENTO {
        bigint id PK
        bigint consorcio_id FK
        string titulo
        string descripcion
        decimal monto "nullable"
        date fecha_solicitud
        date fecha_inicio "nullable"
        date fecha_fin "nullable"
        string estado "pendiente / en_proceso / finalizado"
        text observaciones "nullable"
    }

    %% App reunions (Diseñado / Pausado)
    REUNION {
        bigint id PK
        bigint consorcio_id FK
        string titulo
        text temario
        datetime fecha_hora
        string lugar_o_enlace "nullable"
        string estado "pendiente / finalizada / cancelada"
    }

    %% Relaciones
    USUARIO ||--o{ CONSORCIO : "administra"
    USUARIO ||--o{ UNIDAD : "posee / habita"
    USUARIO ||--o{ PAGO : "registra"
    CONSORCIO ||--|{ UNIDAD : "contiene"
    CONSORCIO ||--o{ GASTO : "registra"
    CONSORCIO ||--o{ LIQUIDACION : "genera"
    CONSORCIO ||--o{ MANTENIMIENTO : "registra"
    CONSORCIO ||--o{ REUNION : "convoca"
    UNIDAD ||--o{ PAGO : "realiza"
    LIQUIDACION ||--o{ PAGO : "recibe"
    LIQUIDACION ||--o{ GASTO : "incluye"
    ```