# InventSystem

Sistema de Inventario desarrollado con Django Rest Framework.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/josegru123/InventSystem.git
cd InventSystem
```

### 2. Crear entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Crear las migraciones para las aplicaciones users y api:

```bash
python manage.py makemigrations users
python manage.py makemigrations api
python manage.py makemigrations
```

Aplicar las migraciones a la base de datos:

```bash
python manage.py migrate
```

### 5. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: http://127.0.0.1:8000/

## Uso del sistema

### Registro de usuario

1. Accede a la página de registro en: http://127.0.0.1:8000/register/
2. Completa el formulario con tus datos
3. Inicia sesión con tu usuario y contraseña

## Licencia

Este proyecto está licenciado bajo [Licencia MIT](LICENSE).