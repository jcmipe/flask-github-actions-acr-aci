# Entregable 4 - Flask + Docker + GitHub Actions + Azure ACR + ACI

## Descripción

Aplicación web desarrollada con Python y Flask que expone dos endpoints:

- `/`: devuelve un mensaje JSON de la aplicación.
- `/health`: devuelve el estado de salud del servicio.

El proyecto implementa un flujo CI/CD con GitHub Actions: pruebas automáticas,
construcción y validación de una imagen Docker, publicación en Azure Container
Registry y despliegue en Azure Container Instances.

## Ejecución local

```powershell
python -m pip install -r requirements.txt
python app.py
```

La aplicación queda disponible en:

```text
http://localhost:5000/
http://localhost:5000/health
```

## Pruebas

```powershell
python -m pytest -q
```

## Docker

```powershell
docker build -t flask-entregable4:local .
docker run --rm -p 5000:5000 flask-entregable4:local
```

## Arquitectura CI/CD

1. GitHub Actions se ejecuta al hacer `push` a `main` o manualmente.
2. Instala las dependencias y ejecuta `pytest`.
3. Construye la imagen Docker.
4. Ejecuta las pruebas dentro de la imagen.
5. Levanta un contenedor temporal y realiza pruebas HTTP.
6. Publica la imagen en Azure Container Registry con tags `latest` y SHA.
7. Despliega en Azure Container Instances mediante la API REST de Azure.

## Secretos de GitHub Actions

El workflow requiere:

- `AZURE_BEARER_TOKEN`
- `AZURE_SUBSCRIPTION_ID`
- `RESOURCE_GROUP`
- `DNS_NAME_LABEL`
- `REGISTRY_LOGIN_SERVER`
- `REGISTRY_USERNAME`
- `REGISTRY_PASSWORD`

El proyecto no guarda credenciales en el repositorio. El token Bearer de Azure
es temporal y debe regenerarse si el despliegue devuelve HTTP 401.

## URL pública

```text
http://flask-e4-jcmipe.westeurope.azurecontainer.io:5000/
http://flask-e4-jcmipe.westeurope.azurecontainer.io:5000/health
```
