-- Script DDL de creación de tablas para PostgreSQL
-- Proyecto: Consorcio360 - Trabajo Final Integrador

-- 1. Tabla Usuarios
CREATE TABLE usuarios_usuario (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    password VARCHAR(128) NOT NULL,
    rol VARCHAR(20) NOT NULL DEFAULT 'VECINO' CHECK (rol IN ('ADMINISTRADOR', 'VECINO')),
    telefono VARCHAR(20),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,
    is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- 2. Tabla Consorcios
CREATE TABLE consorcios_consorcio (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    cuit VARCHAR(20) UNIQUE NOT NULL,
    administrador_id BIGINT REFERENCES usuarios_usuario(id) ON DELETE SET NULL
);

-- 3. Tabla Unidades
CREATE TABLE consorcios_unidad (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    propietario_id BIGINT REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    piso VARCHAR(10) NOT NULL,
    departamento VARCHAR(10) NOT NULL,
    porcentaje_fiscal NUMERIC(5, 2) NOT NULL,
    CONSTRAINT unique_unidad_consorcio UNIQUE (consorcio_id, piso, departamento)
);

-- 4. Tabla Gastos
CREATE TABLE economia_gasto (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    liquidacion_id BIGINT REFERENCES economia_liquidacion(id) ON DELETE SET NULL,
    descripcion VARCHAR(255) NOT NULL,
    monto NUMERIC(12, 2) NOT NULL,
    fecha DATE NOT NULL,
    tipo VARCHAR(20) NOT NULL CHECK (tipo IN ('ORDINARIO', 'EXTRAORDINARIO'))
);

-- 5. Tabla Liquidaciones
CREATE TABLE economia_liquidacion (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    mes INT NOT NULL CHECK (mes BETWEEN 1 AND 12),
    anio INT NOT NULL,
    monto_total NUMERIC(12, 2) NOT NULL DEFAULT 0.00,
    estado VARCHAR(20) NOT NULL DEFAULT 'ABIERTA' CHECK (estado IN ('ABIERTA', 'CERRADA')),
    CONSTRAINT uq_consorcio_periodo UNIQUE (consorcio_id, mes, anio)
);
-- 6. Tabla Pagos
CREATE TABLE economia_pago (
    id BIGSERIAL PRIMARY KEY,
    unidad_id BIGINT NOT NULL REFERENCES consorcios_unidad(id) ON DELETE CASCADE,
    liquidacion_id BIGINT NOT NULL REFERENCES economia_liquidacion(id) ON DELETE CASCADE,
    registrado_por BIGINT REFERENCES usuarios_usuario(id) ON DELETE SET NULL,
    monto NUMERIC(12, 2) NOT NULL,
    fecha_pago DATE NOT NULL,
    comprobante VARCHAR(255),
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE' CHECK (estado IN ('PENDIENTE', 'CONFIRMADO'))
);

-- 7. Tabla Mantenimientos (Módulo en pausa)
CREATE TABLE mantenimiento_mantenimiento (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    monto NUMERIC(12, 2),
    fecha_solicitud DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_inicio DATE,
    fecha_fin DATE,
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE' CHECK (estado IN ('PENDIENTE', 'EN_PROCESO', 'FINALIZADO')),
    observaciones TEXT
);
-- 8. Tabla Reuniones (Módulo en pausa)
CREATE TABLE reuniones_reunion (
    id BIGSERIAL PRIMARY KEY,
    consorcio_id BIGINT NOT NULL REFERENCES consorcios_consorcio(id) ON DELETE CASCADE,
    titulo VARCHAR(150) NOT NULL,
    temario TEXT NOT NULL,
    fecha_hora TIMESTAMP WITH TIME ZONE NOT NULL,
    lugar_o_enlace VARCHAR(255),
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE' CHECK (estado IN ('PENDIENTE', 'FINALIZADA', 'CANCELADA'))
);