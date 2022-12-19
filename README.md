# Prueba Python Fullstack 2022

### ¿Cómo inicio está aplicación?


Cree un entorno virtual y actívelo. Esta aplicación fue probada con la versión de python 3.10.6
```sh
cd env/Scripts
activate
```

Ejecute pip install -r requirements.txt. Esto instalará los paquetes necesarios. 
```sh
pip install -r .\requirements.txt
```
Si todo salió en orden, ahora solo queda correr la app y abrirla en http://localhost:8000/
```sh
python manage.py runserver
```


### Sobre la estructura de carpetas
La estructura de carpetas es una muy típica, dónde hay una carpeta contenedora que almacena las "apps", incluyendo una app, llamada *shared*, como su nombre indica, almaceno las cosas en comun, o compartidas. La app principal es core.

El proyecto tiene 5 aplicaciones authentication, film, home, shared y user. Separando entonces así la lógica del negocio a nivel de *sujeto*.

![](http://corralesdev.com/wp-content/uploads/2022/12/estructura-de-carpetas.png)

#### ¿Necesita documentación?
Puede navegar (http://localhost:8000/swagger/) 

### ¿Quiere conocer mi backoffice?
No tengo nada que mostrar en está ocasión, fueron un par de hojas de cuaderno rayadas. Prefiero escribir ideas a mano que de forma digital

#### Evidencias

#### S3
![](http://corralesdev.com/wp-content/uploads/2022/10/s3_bucket_standard.png)

#### Render
![](http://corralesdev.com/wp-content/uploads/2022/10/render_web_service.png)

#### RDS
![](http://corralesdev.com/wp-content/uploads/2022/10/aws_rds_postgresql.png)