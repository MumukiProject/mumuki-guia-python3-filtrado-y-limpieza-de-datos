`dropna` también nos permite decidir sobre qué columnas queremos hacer el filtrado con el argumento opcional `subset` de la siguiente forma:

```python
dataset.dropna(subset=[columna1, columna2,...])
```

Por ejemplo, hacer...

```python
arboles.dropna(subset=["diametro"])
```

... es equivalente a:

```python
arboles[arboles["diametro"].notna()]
```

La ventaja de esta opción es que ahora podemos eliminar filas más selectivamente, conservando aquellas que tengan `nan`s en columnas poco relevantes para nuestro análisis.

> ¡Probalo! Escribí una expresión que nos permita obtener los árboles de CABA que no tengan `nan` en su barrio ni en su comuna.
