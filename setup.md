# Guía de Instalación - Ads Ninja: Python para Marketers

Esta guía te ayudará a configurar todo el entorno necesario para el curso. Sigue los pasos según tu sistema operativo.

## Índice
- [Guía de Instalación - Ads Ninja: Python para Marketers](#guía-de-instalación---ads-ninja-python-para-marketers)
  - [Índice](#índice)
  - [Requisitos Mínimos](#requisitos-mínimos)
  - [Instalación de Python](#instalación-de-python)
    - [Windows](#windows)
    - [macOS](#macos)
    - [Linux](#linux)
  - [Instalación del IDE](#instalación-del-ide)
  - [Configuración del Entorno Virtual](#configuración-del-entorno-virtual)
  - [Instalación de Dependencias](#instalación-de-dependencias)
  - [Verificación de la Instalación](#verificación-de-la-instalación)
  - [Solución de Problemas Comunes](#solución-de-problemas-comunes)
    - [Error: "Python not found"](#error-python-not-found)
    - [Error: "pip not found"](#error-pip-not-found)
    - [Error al instalar dependencias](#error-al-instalar-dependencias)
    - [Problemas con Jupyter](#problemas-con-jupyter)

## Requisitos Mínimos
- Espacio en disco: 5GB libres
- RAM: 8GB mínimo recomendado
- Procesador: Intel/AMD dual core o superior
- Conexión a Internet estable

## Instalación de Python

### Windows
1. Descarga Python 3.8 o superior desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca la casilla "Add Python to PATH"
3. Verifica la instalación abriendo CMD y ejecutando:
```bash
python --version
```

### macOS
1. Instala Homebrew si no lo tienes:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Instala Python:
```bash
brew install python
```

### Linux
La mayoría de distribuciones Linux ya incluyen Python. Verifica la versión:
```bash
python3 --version
```

Si necesitas actualizarlo:
```bash
sudo apt-get update
sudo apt-get install python3.8
```

## Instalación del IDE

Recomendamos Visual Studio Code:

1. Descarga VS Code desde [code.visualstudio.com](https://code.visualstudio.com/download)
2. Instala las siguientes extensiones:
   - Python
   - Jupyter

## Configuración del Entorno Virtual

1. Abre una terminal en la carpeta del proyecto:
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

2. Activa el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

## Instalación de Dependencias

Con el entorno virtual activado:
```bash
pip install -r requirements.txt
```

Las principales librerías que se instalarán son:
- polars
- pandas
- plotly
- streamlit
- google-ads
- facebook-business
- google-analytics-data
- python-dotenv
- jupyter
- crewai
- langchain

## Verificación de la Instalación

Ejecuta el notebook de prueba:
```bash
python --version
```

## Solución de Problemas Comunes

### Error: "Python not found"
- Verifica que Python esté en el PATH del sistema
- Reinicia la terminal después de la instalación

### Error: "pip not found"
```bash
python -m ensurepip --default-pip
```

### Error al instalar dependencias
- Actualiza pip:
```bash
python -m pip install --upgrade pip
```
- Instala las dependencias una por una para identificar el error

### Problemas con Jupyter
- Reinstala Jupyter:
```bash
pip uninstall jupyter jupyter_core jupyter_client
pip install jupyter
```

Para cualquier otro problema, por favor:
1. Revisa los mensajes de error específicos
2. Consulta la documentación oficial de la librería
3. Abre un issue en el repositorio del curso