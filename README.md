
# QA Automation Framework


![QA Automation Tests](https://github.com/DuvanLope/QA-Automation-Framework/actions/workflows/qa-tests.yml/badge.svg)


Framework de automatización de pruebas de API REST desarrollado con Python, Pytest y Requests.

## Descripción

Este proyecto permite ejecutar pruebas automatizadas para validar el funcionamiento de servicios REST.

Incluye validaciones funcionales, escenarios positivos y negativos, validación de esquemas JSON y generación de reportes HTML.

## Tecnologías utilizadas

- Python 3.12
- Pytest
- Requests
- JSON Schema
- pytest-html
- Visual Studio Code

## Funcionalidades

- Automatización de peticiones GET, POST, PUT y DELETE
- Validación de códigos HTTP (200, 201 y 404)
- Validación del contenido de respuestas JSON
- Validación de headers HTTP
- Validación de JSON Schema
- Pruebas positivas y negativas
- Pruebas parametrizadas
- Fixtures de Pytest
- Manejo de errores de conexión y timeout
- Datos de prueba reutilizables
- Generación de reportes HTML

## API utilizada

Las pruebas utilizan JSONPlaceholder:

https://jsonplaceholder.typicode.com

Esta API permite practicar operaciones REST. Las operaciones POST, PUT y DELETE son simuladas y no guardan cambios permanentes.

## Estructura del proyecto

    QA-Automation-Framework/
    |
    |-- tests/
    |   |-- conftest.py
    |   |-- test_api_posts.py
    |   |-- test_basico.py
    |
    |-- reports/
    |-- config.py
    |-- schemas.py
    |-- test_data.py
    |-- pytest.ini
    |-- requirements.txt
    |-- .gitignore
    |-- README.md

## Instalación

1. Clonar o descargar el repositorio.

2. Crear un entorno virtual:

    python -m venv .venv

3. Activar el entorno virtual en PowerShell:

    .\.venv\Scripts\Activate.ps1

4. Instalar las dependencias:

    python -m pip install -r requirements.txt

## Ejecutar las pruebas

Desde la carpeta principal del proyecto:

    python -m pytest

## Generar reporte HTML

Ejecutar:

    python -m pytest --html=reports/reporte_qa.html --self-contained-html

El reporte generado se puede abrir en un navegador.

## Casos de prueba implementados

- Consulta de posts existentes
- Consulta de recursos inexistentes
- Creación simulada de posts
- Actualización simulada de posts
- Eliminación simulada de posts
- Validación de respuestas mediante JSON Schema
- Validación negativa de esquemas JSON
- Pruebas parametrizadas con múltiples IDs

## Resultados

Última ejecución confirmada:

- 12 pruebas automatizadas
- 12 pruebas exitosas
- 0 pruebas fallidas

## Estado del proyecto

Framework en desarrollo, creado como proyecto de portafolio para demostrar conocimientos prácticos de QA Automation y API Testing.
