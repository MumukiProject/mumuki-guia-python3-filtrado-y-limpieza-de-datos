Ya estudiamos estrategias para tratar tanto datos faltantes como atípicos. Para finalizar vamos a hablar de otro caso común, ¡los duplicados! 👥 Es frecuente encontrar celdas duplicadas en los lotes, pero la buena noticia es que pueden ser removidas fácilmente de la siguiente forma:

```python
dataset.drop_duplicates(inplace=True)
```

En caso de no querer eliminarlas sino sólo obtener un nuevo `DataFrame` sin duplicados, podemos omitir `inplace=True`.

> ¡Pongámoslo a prueba! Remové los duplicados de nuestro dataset `arboles`.
