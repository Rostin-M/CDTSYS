
# CDTSYS

CDTSYS es una aplicación web desarrollada en **Python** utilizando el framework **Reflex**. Su objetivo principal es facilitar el proceso de apertura de Certificados de Depósito a Término (CDTs) en Colombia, proporcionando una interfaz donde los usuarios pueden:

- Registrarse e iniciar sesión.
- Consultar una IA especializada en apertura de CDTs, que responde preguntas y realiza cálculos específicos.
- Recibir recomendaciones sobre las mejores entidades para abrir un CDT según sus condiciones y necesidades.

**Nota:** La aplicación se encuentra en fase beta, y la funcionalidad del video en el chat, que incluye un avatar 3D que responde a las preguntas, está en desarrollo.

## Instalación y Configuración

Sigue estos pasos para instalar y configurar la aplicación en tu entorno local.

### Prerrequisitos

- Python
- Framework Reflex

### Instalación

1. **Clona el repositorio:**

    ```
    git clone <https://github.com/Rostin-M/CDTSYS.git>
    cd CDTSYS
    ```

2. **Configura las API Keys:**

    Abre el archivo `config.py` en el directorio `CDTSYS/config` y añade tus claves y tokens de acceso:

    ```python
    DATABASE_URI = '<TU_DATABASE_URI>'
    GOOGLE_API_KEY = '<TU_GOOGLE_API_KEY>'
    ```

3. **Instala las dependencias:**

    Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

    ```
    pip install -r requirements.txt
    ```

4. **Inicia el proyecto en Reflex:**

    Ejecuta el siguiente comando para inicializar Reflex:

    ```
    reflex init
    ```

5. **Ejecuta el proyecto:**

    Finalmente, inicia la aplicación con:

    ```
    reflex run
    ```

6. **Accede a la aplicación:**

    Abre tu navegador y ve a `http://localhost:3000` para acceder a la aplicación.

## Funcionalidades

- **Registro e Inicio de Sesión:** Los usuarios pueden crear una cuenta y acceder a la plataforma.
- **Chat con IA Especializada:** Una vez iniciada la sesión, los usuarios pueden interactuar con una IA que responde consultas sobre CDTs, realiza cálculos de rendimientos y recomienda las mejores entidades para la apertura de CDTs en Colombia.
- **Video Interactivo con Avatar 3D (Beta):** Una funcionalidad en desarrollo que busca integrar un avatar 3D interactivo que responderá las preguntas de los usuarios de forma visual y personalizada.

## Estructura del Proyecto

- `assets/`: Archivos estáticos de la aplicación.
- `CDTSYS/`: Código principal de la aplicación.
  - `config/`: Archivos de configuración, incluidas las API Keys.
  - `pages/`: Definición de las páginas de la aplicación.
  - `components/`: Componentes reutilizables de la interfaz.
  - `state/`: Gestión del estado de la aplicación.

## Licencia

© Todos los derechos reservados
