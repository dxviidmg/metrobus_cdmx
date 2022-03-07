# Metrobus_cdmx

Proyecto Django con rest y graphql para mostrar las unidades de metrobus junto con su localización

## Instalación

Esta aplicación web de Django necesita una gran cantidad de paquetes adicionales de Python, por favor ejecute el siguiente comando:

```bash
$ pip install -r requirements.txt
```

### Construye la BD de la aplicación Web de Django, por favor ejecute el siguiente comando:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runscript insert_data
```
### Crear usuario administrador de Django

Esta aplicación web de Django necesita crear un usuario administrador de Django, para acceder y administrar la interfaz de administrador, ejecute el siguiente comando:

**Sugerencia:** para esta instalación local use al usuario como **admin** y la contraseña como **admin**.

```bash
$ python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: your-user@mail.com
Password: 
Password (again): 
Superuser created successfully.
```

## Ejecute la aplicación web Django

Necesita ejecutar el servidor de Django, ejecute el siguiente comando:

```bash
$ python manage.py runserver
```

- Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) y vea la aplicación web Django.

- Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) y vea la interfaz de administración de Django, use el usuario **admin** y contraseña **admin**.