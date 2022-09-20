A la hora de limpiar nuestros datos no solamente vamos a querer remover los valores nulos sino también aquellos que sean atípicos. Este tipo de valores, también conocidos como fuera de serie (o, en inglés, _outliers_), no necesariamente son un error de carga pero aún así los limpiaremos por no ser representativos de nuestra muestra 🧹. 

Observemos por ejemplo la altura y el diámetro máximos de nuestros árboles 🌲...

```python
ム arbolado["altura"].max()
COMPLETAR
ム arbolado["diametro"].max()
COMPLETAR
```

...y comparémoslos con sus promedios:

```python
ム arbolado["altura"].mean()
COMPLETAR
ム arbolado["diametro"].mean()
COMPLETAR
```

¡Hay mucha diferencia! Esto podría ser correcto, pero por las dudas verifiquemos qué sucede si quitamos el 2% más grande de ambas columnas utilizando `quantile`:  

```python
ム arbolado["altura"].quantile(0.98)
COMPLETAR
ム arbolado["diametro"].quantile(0.98)
COMPLETAR
```

¡Wow! ¡Cuánto cambió! Todo parece indicar que los árboles más altos están _fuera de serie_ y presentan una altura _desproporcionada_, que excede ampliamente la de los demás.  Parece que tenemos que pasar la tijera por acá ✂️.

> Escribí una expresión que nos permita obtener sólo aquellos árboles que tengan una altura y un diámetro que estén dentro del 98% más chicos.
