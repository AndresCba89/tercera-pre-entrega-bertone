# Tercera preentrega Proyecto Django Bertone Andres

El proyecto de web incluye las posibilidad para registrar ususurio, pacientes, derivantes (instituciones de salud) y analisis o estudios medicos a realizar, asi como realizar la busqueda de usuarios por su dni en la plantilla principal

# Pasos para ejecutar:
1. Clona el repositorio en la terminal de tu maquina: 
git clone https://github.com/AndresCba89/tercera-pre-entrega-bertone.git


2. Activa el entorno virtual: 
source asb_env/Scripts/activate

3. Inicia el servidor:
python manage.py runserver

4. Accede desde el navegador al inicio del proyecto:
http://127.0.0.1:8000/

# PESTAÑAS:

1. Pagina de inicio - Buscar usuarios por dni:
- URL /inicio/ o haciendo click en "inicio" en la barra de navegacion
- Descripcion: Es la pagina principal del proyecto donde se visualiza el nombre del centro medico y debajo se puede buscar los usuarios registrados por su dni.
En la parte superior derecha se encuetra los accesos a "Usuarios", "Derivantes","Pacientes", "Analisis"

2. Usuarios:
- URL /us_form/ o haciendo click en "Usuarios" en la parte superior derecha.
- Descripcion: En esta pagina se realiza el regsitro de los usuarios a sistema del servicio de salud. Donde debe registrar un "nombre" y su dni. Debe presinar el boton "Enviar".

3. Registro Derivantes:
- URL /dev_form/ o haciendo click en "Derivantes" en la parte superior derecha.
- Descripcion: En esta seccion se realiza el regsitro del derivante, lo que seria a que institucion de sasud pertenece el usuario principal solcitante del servicio de analisis o estudio. Se debe registrar con el nombre de la institucion, apellido, email y profesion. Luego de completar los campos presione Enviar

4. Pacientes:
- URL /pte_form/ O haciendo click en "Pacientes" en la parte superior derecha.
- Descripcion: Se realiza la carga de los pacientes que tengan los usuarios, con el registro de su nombre, apellido y email, una vez completo el campo. Debe presinar el boton "Enviar".


5. Registro Analisis:
- URL /an_form/ o haciendo click en "Analisis" en la parte superior derecha.
- Descripcion: Aca solicita el tipo de analisis o estudio medico que desea realizar al paciente que el derivante registro en el paso anterior. Coloca el nombre y presione "Enviar".
