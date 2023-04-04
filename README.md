# Data Projects + Tutorial Render y FastAPI
![logo](https://builtin.com/sites/www.builtin.com/files/styles/og/public/2022-11/data-science-projects.jpg)

# Como levantar un proyecto de Data general

## 1) Crear entorno virtual
Todas las dependencias y librerías van a quedar instaladas acá:
```
python -m venv venv
```
Esto nos posibilita solo trabajar con las librerías necesarias del proyecto, y no con todas las que se tengan instaladas localmente. Permite que otros usuarios o compañeros de trabajo puedan replicar e instalar sencillamente lo mismo que nosotros, y que no interfiera con las cosas que tengan también previamente descargadas. 

## 2) Crear archivos necesarios
Desde la consola Gitbash:
```
touch .gitignore
touch main.py
touch requirements.txt
```
## 3) venv + .gitignore
Poner el entorno virtual dentro del archivo .gitignore:
```
/venv
```
Si no funciona, probar de distintas formas:
```
/venv
venv
venv/

```

# Tutorial de Render y FastApi

![image](images/fastapi.png)

## Git init + Instalaciones
Desde la misma terminal de VSCode, realizar los siguientes pasos:
```
git init
pip install uvicorn
pip install fastapi
```
Cualquier otra librería que se vaya a utilizar también puede ser descargada en este momento, o cuando sea necesario.

## Pip freeze
Una vez que ya están todas las librerías descargadas en nuestro entorno virtual, podemos hacer el freeze de los requirements.  
 Es importante para este tutorial no abusar de demasiadas dependencias, porque en algunos casos, luego las aplicaciones no pueden deployar nuestros modelos. 
```
pip freeze > requirements.txt
```
Si luego se necesita instalar otra librería más, se vuelve a ejecutar este comando.  

Cualquier persona que quiera usar nuestro código, va a poder instalar lo mismo que instalamos nosotros. 
## main.py
Ahora ya esta listo para poder codear toda tu API con Fastapi.
## Creación repo Github
Para más información, se puede leer el documento en el siguiente [enlace](https://drive.google.com/file/d/1lzKIUTFJ2lnKluZ21hfResGvTJU7fA2k/view?usp=sharing)
- Crear un nuevo repo en Github. Dejarlo en modo público.
![image](images/repo.jpg)
- Seguir los pasos para conectarlo con nuestro repositorio local
![image](images/steps.jpg)
## Render
1. Entrar en `render.com` y crearse una nueva cuenta de usuario. 
2. Elegir la opción `Web Service`
3. Ir al apartado que se encuentra abajo de `Public Git repository`. Copiar y pegar el enlace del repositorio que crearon anteriormente (recuerden que sea público).
![image](images/public.jpg)
4. Llenar los campos necesarios. En branch seleccionen `main`. Runtime tiene que ser `Python 3`.
![image](images/fill.jpg)
5. El resto de los campos se deben llenar con la misma información que en la imagen:
![image](images/campos.jpg)
6. Seleccionar la opción `Create Web Service`
7. Una vez terminados los pasos anteriores, se va a comenzar a cargar nuestra aplicación. Puede tardar unos minutos. 
![image](images/logs.jpg)
8. Entrar al enlace de arriba a la izquierda:
![image](images/enlace.jpg)
9. Nos va a direccionar a nuestra API. Si les aparece un "Not found", no se preocupen, agreguenle un /docs a su enlace.

Con todos esos pasos, la API que crearon ya está lista para poder ser consumida!
