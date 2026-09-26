-- Script DDL de creación de tablas para PostgreSQL
-- Proyecto: Consorcio360 - Trabajo Final Integrador

-- 1. Tabla Usuarios
CREATE TABLE usuarios_usuario (
    id BIGSERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'VECINO',
    telefono VARCHAR(20)
);

-- 2. Tabla Consorcios
CREATE TABLE consorcios_consorcio (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    cuit VARCHAR(13) UNIQUE NOT NULL
);

-- 3. Tabla Unidades
CREATE TABLE consorcios_unidad (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    usuario_id BIGINT REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    piso VARCHAR(10) NOT NULL,
    departamento VARCHAR(10) NOT NULL,
    porcentaje_fiscal NUMERIC(5, 2) NOT NULL,
    CONSTRAINT unique_unidad_consorcio UNIQUE (consorcio_id, piso, departamento)
);

-- 4. Tabla Gastos
CREATE TABLE economia_gasto (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    concepto VARCHAR(200) NOT NULL,
    monto NUMERIC(12, 2) NOT NULL,
    fecha DATE NOT NULL
);

-- 5. Tabla Liquidaciones
CREATE TABLE economia_liquidacion (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    mes INTEGER NOT NULL,
    anio INTEGER NOT NULL,
    monto_total NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT unique_liquidacion_mes_anio UNIQUE (consorcio_id, mes, anio)
);

-- 6. Tabla Pagos
CREATE TABLE economia_pago (
    id BIGSERIAL PRIMARY KEY,
    unidad_id BIGINT NOT NULL REFERENCES consorcios_unidad(id) ON DELETE CASCADE,
    liquidacion_id BIGINT NOT NULL REFERENCES economia_liquidacion(id) ON DELETE CASCADE,
    monto NUMERIC(12, 2) NOT NULL,
    fecha_pago TIMESTAMP WITH TIME ZONE NOT NULL,
    comprobante VARCHAR(100)
);

-- 7. Tabla Mantenimientos (Módulo en pausa)
CREATE TABLE mantenimientos_mantenimiento (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE',
    fecha_creacion TIMESTAMP WITH TIME ZONE NOT NULL
);

-- 8. Tabla Reuniones (Módulo en pausa)
CREATE TABLE reunions_reunion (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    fecha_hora TIMESTAMP WITH TIME ZONE NOT NULL,
    orden_del_dia TEXT NOT NULL,
    canal_enlace VARCHAR(255)
);