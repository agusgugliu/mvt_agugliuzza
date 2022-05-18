# MVT_AGUGLIUZZA - WalkThrough
 
## 1. Creamos la carpeta del Proyecto
`C:/User/Usr/Documents/GitHub/`**mvt_agugliuzza**

## 2. Creamos el Proyecto con la terminal interactiva
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza`
```
django-admin startproject ProyectoFamilia
```

## 3. Realizamos las migraciones y la generación de la base de datos
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/`
```
python manage.py migrate
```
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/`
```
python manage.py runserver
```

## 4. Creamos la Aplicación
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/` 
```
python manage.py startapp AppFamilia
```

## 5. Creamos los modelos
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/AppFamilia/models.py`

```
from django.db import models
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_documento = models.IntegerField()
```

## 6. Informamos a Django de la nueva aplicación
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/settings.py`
```
INSTALLED_APPS = [
    '-----',
    '-----',
    'AppFamilia',
    ]
```
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia/`
```
python manage.py check AppFamilia
```

## 7. Creamos el Modelo de Base de Datos
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia`
```
python manage.py makemigrations
```
```
python manage.py sqlmigrate AppFamilia 0001
```
```
python manage.py migrate
```

## 8. Insertamos los Datos a la Base de Datos
`C:/User/Usr/Documents/GitHub/mvt_agugliuzza/ProyectoFamilia`
```
python manage.py shell
```
```
from AppFamilia.models import Familiar
familiar = Familiar(nombre='Agustín',apellido='Gugliuzza Piccinini',fecha_nacimiento='1995-04-09',numero_documento=40567020)
familiar.save()
```