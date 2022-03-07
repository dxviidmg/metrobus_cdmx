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

## Ejecute la aplicación web Django

Necesita ejecutar el servidor de Django, ejecute el siguiente comando:

```bash
$ python manage.py runserver
```

- Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) y vea la aplicación web Django.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runscript insert_data
```

## Peticiones rest
- Lista de unidades disponibles (http://127.0.0.1:8000/metrobuses/metrobus/)
- Unidad por id (http://127.0.0.1:8000/metrobuses/metrobus/1/)
- Lista de alcaldias (http://127.0.0.1:8000/alcaldias/alcaldia/)
- Lista de unidades por alcaldia (http://127.0.0.1:8000/alcaldias/alcaldia/1/)

## Peticiones grapqhl
 - Lista de unidades disponibles

```
{
	allMetrobuses {
  	number
	} 
}
```

- Unidad por id

```
{
	metrobus (id: 1) {
    number
    latitude
    longitude
    townhall {
      name
    }
  }
}
```

- Lista de alcaldias

```
{
	allTownhalls {
    name
  }
}
```

- Lista de unidades por alcaldia

```
{
  townhall (id: 1) {
    name
    
  metrobuses {
    number
  }}
}
```