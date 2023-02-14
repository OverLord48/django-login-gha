# Servicio de Login
_Microservicios hechos en django-rest y Fastapi_

## Instalación 🔧

_Adecuar entorno de ejecucion para levantar el servicio_

_De la siguiente forma_

```
- Crear el .env partiendo del .env.example que esta en la raiz del proyecto

- Asignar credenciales correspondientes a cada variable dejada en el .env.example (Opcional, se pueden dejar tal cual estan en el .example)

- En caso de tener docker pasar a los pasos del despliegue.

- En caso de no poseer docker usar las siguientes indicaciones:

    - Debe tener virtualenv o anaconda para generar entorno virtual de ejecucion para este servicio

    - Ejecutar el archivo como pip install -r requirements.txt respectivo para adecuar el entorno
```

## Despliegue 📦

_Ejecutar el deploy_
 ``` 
  - IMPORTANTE: dividiremos el deploy en dos pasos (con docker y sin docker)

  - Con Docker:
  
    - docker-compose up

    - docker-compose up -d en caso de no querer ver los logs

    nota: para acceder a la api signIn http://0.0.0.0:8080/docs ,
        para acceder a la api signOut http://0.0.0.0:8000/docs
  
  - Sin Docker:

    - Crear la base de datos en postgres (cargar nombre en el .env y credenciales del postgres)
  
    - Ejecutar migraciones python manage.py migrate

    - Levantar el servicio con python manage.py runserver

    nota : recordar que debe tener el entorno virtual encendido
 ```

## Construido con 🛠️


* [django-rest-framework](https://www.django-rest-framework.org/) 
* [Fastapi](https://fastapi.tiangolo.com/) 

## Desarrollado por: ✒️

* **Cesar Padrino** - [OverLord48](https://github.com/OverLord48)