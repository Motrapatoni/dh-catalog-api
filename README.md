# Implementación de POS CATALOG API - DH

## Descripción:

Aplicación creada con fines practicos con el fin de tener ejemplos funcionales con esta API.  
La implementación consta con:

- Agregar producto
- Actualizar precio
- Actualizar disponibilidad
- Actualización de varios productos(en lote)
- Descarga del catalogo
- Implementación de webhook para escucha de notificaciones

### Tecnologias utilizadas: 🛠️

- [Python] (https://www.python.org/) - Lenguaje base del proyecto
- [Flask] (https://flask.palletsprojects.com/en/latest/) - Framework mediante el cual se levantó el proyecto
- [Ngrok] (https://ngrok.com/docs/getting-started/) - Herramienta que nos permite crear un webhook disponible en la web
  a partir de nuestro localhost.

## Uso del proyecto.

### Instalación 🔧

Para descargar el proyecto pueden descargar el repositorio en formato zip.

1 - Descomprimir el archivo

2 - Abrir una terminal para ubicarnos en el proyecto:

### `cd implementacion de API DH`

3 - Instalar los paquetes necesarios con:

### `pip install -r requirements.txt`

4 - Una vez finalizado, ejecutar:

### `python main.py`

Tomar en cuanta que flask por defecto toma el puerto `5000`, podemos validar que el proyecto esta corriendo OK al
ingresar a `http://127.0.0.1:5000/` y visualizar en el explorador un `Hello world`

### Instalación con git clone 🔧

Se puede clonar el repositorio, ingresando a una terminal y ejecutando:  
`git clone https://github.com/Motrapatoni/dh-catalog-api.git`

Luego continuar desde el paso 2.

# ⚠️ IMPORTATE ⚠️

**Seguir los pasos de instalación de ngrok que se indican aca: `https://ngrok.com/docs/getting-started/`  
Instalar segun tu sistema operativo y realizar el login, una vez realizado esto, abrir una terminar en tu equipo y
ejecutar:  
`ngrok http 5000`  
Esto te proporcionará una url con este formato:  
`https://XXXXXXXXXXXXXXX.ngrok-free.dev`  
Esta sera tu url/webhook disponible desde cualquier lugar de la web.** 
