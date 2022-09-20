Una última alternativa posible para el manejo de datos faltantes es reemplazandolos. Si bien podemos hacerlo con un valor fijo, conviene usar valores calculados que tengan sentido para el conjunto de datos. Por ejemplo por ejemplo, podemos _llenarlos_ con la media obtenida a partir de los demás valores de dicha variable:

```python
dataset['columna_con_faltantes'].fillna(dataset['columna_con_faltantes'].mean())
```

Esta expresión devuelve un nuevo `Series` con los reemplazos, aunque podríamos reemplazarlos directamente en nuestro `DataFrame` haciendo:

```python
dataset['columna_con_faltantes'].fillna(dataset['columna_con_faltantes'].mean(), inplace=True)
```

> ¡Probémoslo! Reemplazá en nuestro `DataFrame` de árboles todas las inclinaciones faltantes por el promedio de esa columna. 