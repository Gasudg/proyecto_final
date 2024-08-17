# Proyecto Django: Blog y Mensajería
Este proyecto es una aplicación web desarrollada en Django que incluye un blog de paginas con funcionalidad de mensajería. Los usuarios pueden registrarse, iniciar sesión, crear y gestionar páginas de blog, y comunicarse entre sí a través de comentarios en las páginas.

## Funcionalidades

### Blog:
Listar Páginas: Visualiza una lista de páginas de blog con imagen, título, subtítulo, y botones para editar y eliminar (solo para administradores).
Detalles de Página: Muestra detalles de una página, incluyendo título, imagen, subtítulo y contenido.
Crear y Editar Páginas: Los usuarios autenticados pueden crear y editar páginas de blog. Los administradores pueden subir imágenes.

### Autenticación de Usuarios:
Registro: Los usuarios pueden registrarse proporcionando nombre de usuario, email y contraseña.
Inicio de Sesión: Los usuarios pueden iniciar sesión.
Cierre de Sesión: Los usuarios pueden cerrar sesión.
Perfil de Usuario: Los usuarios pueden ver y editar su perfil, incluyendo avatar, biografía, y fecha de nacimiento.

### Mensajería:
Comentarios en Páginas: Los usuarios pueden comentar en las páginas del blog. Los comentarios se muestran en cada página.


## Instalación y Configuración
### Requisitos

- Python 3.x
- Django 5.0.7 o superior

### Clonación del Repositorio
```
git clone https://github.com/Gasudg/proyecto_final.git
cd tu_repositorio
```

### Configuración
Base de Datos: Asegúrate de que sqlite3 esté instalado (se usa por defecto).

Migraciones: Aplica las migraciones iniciales.
```
python3 manage.py migrate
```

Ejecución del Proyecto
Inicia el servidor de desarrollo:

```
python3 manage.py runserver
```