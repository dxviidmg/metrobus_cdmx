# Metrobus_cdmx

Proyecto Django con rest y graphql para mostrar las unidades de metrobus junto con su localización

# Prerequisitos
python 3.8
virtualenvwrapper
Postgres 13

## Instalación

Esta aplicación web de Django necesita una gran cantidad de paquetes adicionales de Python, por favor ejecute el siguiente comando:

```bash
$ pip install -r requirements.txt
```

### Construye la BD de la aplicación Web de Django, por favor ejecute el siguiente comando:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## inserción de datos

```bash
$ python manage.py runscript insert_data
```

## Ejecute las pruebas unitarias

Ejecute el siguiente comando:

```bash
$ python manage.py test
```

## Ejecute la aplicación web Django

Ejecute el siguiente comando:

```bash
$ python manage.py runserver
```

- Abra su navegador web con la siguiente URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) y vea la aplicación web Django.


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