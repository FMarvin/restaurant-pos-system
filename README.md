LINK REPO: 
https://github.com/FMarvin/restaurant-pos-system

# Documentación del Proyecto: Sistema de Restaurante

## 1. Elección de Stack
- **Backend:** Python con FastAPI. (No se usó Node.js/Express).
- **Base de Datos:** PostgreSQL. (No se usó SQLite; es una DB empresarial).
- **Frontend:** HTML5, JS Vanilla, Tailwind CSS, WebSockets.

## 2. Elección de Arquitectura
- **Arquitectura N-Tier (Capas):** El backend está separado en routers, services, repositories y models.
- **Patrón de Inyección de Dependencias:** Usado nativamente a través de `Depends` de FastAPI.

## 3. Clasificación de Sistema
- **Clasificación:** TPS (Transaction Processing System). 
- **Justificación:** Registra transacciones operativas diarias (pedidos, preparación y facturación) en tiempo real, garantizando propiedades ACID.

## 4. Prácticas de Código Limpio
- **Nomenclatura Clara:** Variables descriptivas.
- **Responsabilidad Única (SRP):** Repositorios solo hacen SQL, servicios aplican reglas de negocio, routers manejan HTTP.
- **Inyección de Dependencias:** Desacoplamiento de la Base de Datos.

## 5. Instrucciones de Ejecución
1. Levantar la base de datos: `docker-compose up -d`
2. Crear entorno virtual (opcional): `python -m venv venv` y activarlo.
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar el proyecto: `uvicorn app.main:app --reload`
5. Abrir `http://localhost:8000/` en el navegador.

## Documentación de Prompts e Ingeniería de Prompts

Para este desarrollo se aplicaron técnicas avanzadas de ingeniería de prompts con IA, estructurando las instrucciones bajo los siguientes conceptos:

* **Role Prompting & Architectural Constraints**
  * *Prompt:* "Actúa como un Arquitecto de Software Senior especializado en FastAPI. Diseña una capa de servicios y repositorios desacoplada (Patrón N-Tier) para un sistema de restaurante, asegurando que las consultas SQL residan estrictamente en la capa de persistencia y la lógica de negocio en los servicios, aplicando inversión de dependencias mediante 

* **Behavioral & Real-Time Workflow Prompting**
  * *Prompt:* "Implementa un administrador de conexiones WebSocket asíncrono para FastAPI que actúe como un bus de eventos bidireccional. Cuando el mesero registre una orden, debe transmitirse instantáneamente a la pantalla de cocina (KDS); y cuando la cocina marque el estado a 'LISTO', debe emitir una alerta en tiempo real al panel del mesero sin recargar la página.

* **Output Schema Enforcement**
  * *Prompt:* "Escribe las consultas DDL en SQL para PostgreSQL que modelen un sistema transaccional (TPS) de restaurante. Incluye llaves foráneas estrictas, restricciones en cascada para los platillos de una comanda, estados enumerados para mesas y pedidos, y un conjunto de datos iniciales (seed) de 6 mesas y 6 platillos."
* **Contextual UI/UX Scaffolding**
  * *Prompt:* "Diseña las interfaces frontend en un archivo HTML único por vista utilizando Tailwind CSS mediante CDN. La vista del mesero debe integrar un mapa de salón interactivo con colores dinámicos (verde para libre, rojo para ocupado), un formulario de comanda con notas libres para alergias y un panel de caja para liberación de mesas."

