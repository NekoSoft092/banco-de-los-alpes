# Setup Banco de los Alpes

## Base de datos

Desde el archivo docker-compose.yml tenemos configurada la base de datos en postgresql desde una imagen en docker hub

Para inicializar la base de datos de manera local deberas usar el comando

-   docker-compose up

Nota:

-   Antes de correr este comando debes tener instalado docker
-   Luego de correr el comando debes abrir otra terminal ya que si cierras la consola de la base de datos estarias parando el proceso que nos da el servicio de base de datos

## Inicializar entorno de desarrollo venv

Para inicializar el entorno de desarrollo virtual en python deberas antes tener instalado una version de python mayor o igual a 3.9

Para iniciaizar el entonro usaremos el siguente comando

-   python3 -m venv venv

### Mac o Linux

Para activar el entorno venv usaremos el comando

-   source venv/bin/activate

### Windows

Para activar el entorno venv usaremos el comando

-   source venv/Scripts/activate

## Instalar dependencias

Luego deberas instalar las dependencias declaradas en el archivo pyproject.toml

-   pip install -e ".[all]" (new pip version)
-   pip install ".[all]" (old pip version if it's not working with "-e")

## Archivo .env

En el archivo .env guardaremos variables confidenciales, por lo cual deberas copiar el archivo .env.example y pegarlo con el nombre .env

## Correr el proyecto

Para correr el proyecto deberas usar el comando

-   python3 src/main.py
