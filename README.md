# Web de links personal
Proyecto para la visualización de enlaces a mis redes personales.

## Descripción
Este proyecto ha sido realizado con el framework de python reflex que permite realizar webs.
Para ello he utilizado y personalizado mi web con la ayuda del curso de [mouredev](https://www.youtube.com/watch?v=n2YrGsXJC6Y)


### Iniciar
Primero creamos el entorno virtual si no lo tenemos
```
python3 -m venv .venv
```

Nos metemos en el entorno virtual
```
source venv/bin/activate
```

Instalamos las dependencias si no lo estan aun
```
pip install -r requirements.txt
```

Y por ultimo para iniciarlo usamos
```
reflex run
```

### Build
```
reflex export --frontend-only
```
```
unzip frontend.zip -d public
```