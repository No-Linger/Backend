# Backend

## Tecnologías Utilizadas y Configuración

- **Flask (3.0.0):** Un micro framework para aplicaciones web en Python, proporcionando ligereza y modularidad.
- **Firebase Admin (6.2.0) y Google Cloud Firestore (2.13.1):** Herramientas para manejar servicios de Firebase y Firestore, respectivamente.
- **PyMongo (4.5.0):** Utilizado para interactuar con MongoDB, una base de datos NoSQL.
- **Requests (2.31.0):** Librería para realizar solicitudes HTTP en Python.
- **Jinja2 (3.1.2) y Werkzeug (3.0.0):** Utilizados para generar contenido HTML dinámico y para desarrollar aplicaciones web en Python.
- **Cryptography (41.0.5):** Proporciona herramientas criptográficas para Python.

## Código Comentado

Los archivos `db.py`, `planograms.py`, `statistics.py`, `stores.py`, y `routes.py` están bien comentados, explicando el propósito de las clases, sus métodos y atributos, facilitando su comprensión y mantenimiento.

En `db.py`, se presenta una interfaz para interactuar con MongoDB, manejar excepciones y conectar a la base de datos. `planograms.py` y `statistics.py` definen clases para representar planogramas y datos estadísticos, respectivamente, con métodos para convertir e insertar estos datos en MongoDB. `stores.py` describe una clase para manejar información de tiendas, incluyendo métodos para insertar y recuperar datos de MongoDB.

## Descripción de Rutas

- **/createPlanogram (POST):** Inserta planogramas en MongoDB. El request recibe datos en JSON y el response retorna un mensaje de éxito o error.
- **/getPlanograms (GET):** Obtiene planogramas por región. Requiere autenticación y retorna una lista de planogramas o un mensaje de error.
- **/saveStatistics (POST):** Guarda datos estadísticos. Recibe estadísticas en JSON y retorna confirmación o error.
- **/getStatistics (GET):** Recupera datos estadísticos, retornando una lista de estadísticas o un mensaje de error.
- **/saveStore (POST):** Inserta información de tiendas. Recibe datos de tiendas en JSON y retorna éxito o error.
- **/getStores (GET):** Obtiene información de tiendas por región. Requiere autenticación y retorna una lista de tiendas o error.
- **/createUser (POST) y /getUsers (GET):** Para crear nuevos usuarios y obtener información de usuarios, respectivamente.
