# 📘 Proyecto: Aplicación de Gestión de Consorcios

## 👥 Tutora: 
- Sofia Raia
- 
## 👥 Equipo 188
- Laura Diaco  
- Matias Mansilla
- 

---

## 📖 Introducción

Como grupo hemos decidido desarrollar una aplicación web para la **gestión integral de consorcios**. La idea surge de observar las dificultades que enfrentan tanto administradores como vecinos en la organización de gastos, mantenimientos y comunicación interna. Nuestro objetivo es ofrecer una herramienta moderna que centralice toda esta información y que, al mismo tiempo, promueva la transparencia y la participación vecinal.  

El administrador contará con un acceso que le permitirá registrar gastos, facturas y pagos, además de llevar un historial de mantenimientos y programar revisiones importantes (ascensores, tanque de agua, etc.). Los vecinos, por su parte, tendrán su propio acceso para consultar su estado administrativo, visualizar el historial de mantenimiento del edificio y participar en reuniones virtuales, con posibilidad de leer actas y votar decisiones simples.  

De esta manera, buscamos que la aplicación no solo organice mejor la administración, sino que también abra un canal de comunicación claro y confiable entre todas las partes.

---

## ⚙️ Tecnologías

- **Backend:** Python con Django + Django REST Framework  
- **Frontend:** React con TypeScript  
- **Base de Datos:** MongoDB  
- **Notificaciones y tareas programadas:** Celery + Redis  
- **Almacenamiento de archivos:** MinIO/S3  
- **Plataforma:** GitHub (repositorio único), deploy en Railway/Render  

---

## 📅 Plan de Trabajo

### Semana 1–2: Modelado de entidades y base de datos
- Definición de entidades principales: Usuario (administrador/vecino), Consorcio, Unidad, Gasto, Mantenimiento y Acta.  
- Uso de **MongoDB** para almacenar documentos flexibles (facturas, actas, registros).

### Semana 3–4: Backend con Django + Django REST Framework
- Implementación de la lógica del sistema en **Django**.  
- Creación de API REST con **Django REST Framework** para exponer datos en formato JSON.  
- Endpoints básicos: login, registro de gastos, consulta de expensas y mantenimientos.

### Semana 5–6: Frontend con React + TypeScript
- Construcción de la interfaz con **React**.  
- Uso de **TypeScript** para tipado y mayor seguridad en el código.  
- Paneles diferenciados:  
  - Administrador: gestión de gastos, mantenimientos y actas.  
  - Vecino: consulta de expensas, historial de mantenimiento y votaciones.

### Semana 7: Integración frontend-backend
- Conexión de React con la API de Django.  
- Validación de que las acciones en la interfaz se reflejen en la base de datos.

### Semana 8: Funcionalidades avanzadas
- Configuración de **Celery + Redis** para recordatorios automáticos.  
- Implementación de **MinIO/S3** para almacenamiento de archivos (fotos, comprobantes, actas).

### Semana 9: Deploy y documentación
- Publicación de la aplicación en **Railway** o **Render**.  
- Documentación del sistema y entrega final en el repositorio de **GitHub**.

## Conclusión
Este plan de trabajo nos permitirá avanzar de manera ordenada, integrando tecnologías modernas pero accesibles para estudiantes. La aplicación busca resolver un problema real y cotidiano, mostrando en el proceso nuestro dominio de herramientas de backend, frontend, bases de datos y servicios complementarios.
