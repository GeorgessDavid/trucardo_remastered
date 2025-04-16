<div align="center">
    <img src="https://cdn.discordapp.com/attachments/694311001696370739/1307867678425481296/logo_trucardo.png?ex=673bde31&is=673a8cb1&hm=fd911e301f5b51057f952cbb7b5b48eb475460e91e4282dc24dbfe2028654750&" alt="Logo del Trucardo" title="Trucardo">
</div>

# Trucardo Remastered

## Descripción
Versión de terminal del tradicional juego argentino, el truco.

### Integrantes
_Georges David_

_Iván Díaz_

_Felipe Figueredo_

_Luca Ravello_ (R.I.P)

#
### Intentalo vos mismo!
```
git clone https://github.com/GeorgessDavid/trucardo_remastered.git
cd .\trucardo_remastered\
pip install inquirer
python main.py
```

Y listo! A jugar!


### Cronograma
#
#### Hito 1
Utilización de Matrices, Tuplas, Rebanado, Comprensión de listas, Cadenas de Caracteres, Diccionarios y Conjuntos.

* _Matrices_: ./src/constantes.py
* _Tuplas_: ./src/constantes.py
* _Rebanado_: ./utilities/crearMazo.py
* _Comprensión de Listas_: ./utilities/crearMazo.py y otros archivos más.
* _Diccionarios_: ./utilities/calcuarPuntos.py
* _Conjuntos_: No utilizado.

#### Hito 2
Funciones Lambda, map, filter y reduce. Excepciones. Archivos. Expresiones regulares.
* _Lambda_: ./src/helper/checkName.py - ./utilities/calcularPuntos.py - ./utilities/crearMazo.py
* _Map_: ./utilities/crearMazo.py
* _Filter_: ./utilities/calcularPuntos.py 
* _Reduce_: No utilizado.
* _Excepciones_: ./src/controllers/log/showLogs.py
* _Archivos_: ./src/controllers/player/player.py
* _Expresiones Regulares_: ./src/helper/checkName.py

#### Hito 3
Repositorio Git, Recursividad, Pruebas Unitarias.

* _Git_: this.
* _Recursividad_: main.py
* _Pruebas Unitarias_: ./test/
