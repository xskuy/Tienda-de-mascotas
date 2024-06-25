# Tienda de Mascotas

Este proyecto es una aplicación web de una tienda de mascotas desarrollada con Django.

## Descripción

La Tienda de Mascotas es una plataforma en línea que permite a los usuarios ver y comprar productos para mascotas, incluyendo alimentos, juguetes, accesorios y más.

## Características

- Catálogo de productos para diferentes tipos de mascotas
- Sistema de carrito de compras
- Proceso de pago (simulado)
- Panel de administración para gestionar productos e inventario
- Sistema de autenticación de usuarios

## Tecnologías utilizadas

- Python
- Django
- HTML/CSS
- JavaScript
- SQLite (base de datos por defecto de Django)

## Instalación

1. Clona este repositorio: git clone https://github.com/tuusuario/tienda-de-mascotas.git

2. Navega al directorio del proyecto: cd tienda-de-mascotas

3. Crea un entorno virtual y actívalo: python -m venv env source env/bin/activate # En Windows usa env\Scripts\activate

4. Instala las dependencias: pip install -r requirements.txt

5. Realiza las migraciones: python manage.py migrate

6. Crea un superusuario: python manage.py createsuperuser

7. Inicia el servidor de desarrollo: python manage.py runserver

## Uso

- Accede a la aplicación en tu navegador: `http://localhost:8000`
- Para acceder al panel de administración, ve a: `http://localhost:8000/admin`

## Contribuir

Si quieres contribuir a este proyecto, por favor:

1. Haz un Fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es de uso educativo
