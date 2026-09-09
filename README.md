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

## 6. Documentación de Prompts (Ejemplo para tu entrega)
- *Prompt:* "Actúa como un arquitecto de software y diséñame un sistema de restaurante usando FastAPI y WebSockets..."
- *Conceptos de Prompt Engineering:* Context setting, Role prompting, Constraint definitions (restricciones de tecnología).
