Otra de las soluciones posibles para el tratamiento de los datos faltantes es la eliminación de casos completos, es decir eliminar toda las filas que contienen un dato faltante 🗑️. Esto lo podemos hacer utilizando `dropna` de la siguiente forma:

```python
dataset.dropna()
```
Incluso podríamos eliminar aquellas filas que tengan más de un dato faltante haciendo:

```python
dataset.dropna(thresh=2)
```

A diferencia de los filtrados anteriores, con `dropna` podemos eliminar estas filas en nuestro dataset original utilizando `inplace=True` como argumento así:

```python
dataset.dropna(inplace=True)

dataset.dropna(thresh=2, inplace=True)
```

> ¡Vamos a probarlo! Eliminá del dataset `arboles` todas las filas que tengan algún valor nulo. 
