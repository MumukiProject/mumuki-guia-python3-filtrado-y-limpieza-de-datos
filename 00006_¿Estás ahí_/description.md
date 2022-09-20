Si quisiéramos saber qué árboles están en los barrios de Floresta y Recoleta nos podríamos tentar a hacer: 

```python
arboles[(arboles["barrio"] == "Floresta") | (arboles["barrio"] == "Recoleta")]
```

Y quizás no parece tan grave. Pero ¿qué sucede si queremos los árboles de Floresta, Recoleta, Belgrano y Nuñez? Si bien podríamos hacer esto…

```python
arboles[(arboles["barrio"] == "Floresta") | (arboles["barrio"] == "Recoleta") | (arboles["barrio"] == "Belgrano") | (arboles["barrio"] == "Nuñez")]
```

… no parece lo más cómodo, ¿verdad?

Por suerte existe `isin` que nos puede ahorrar bastante tiempo. Para obtener el resultado anterior podríamos hacer simplemente:

```python
arboles[arboles["barrio"].isin(["Floresta", "Recoleta", "Belgrano", "Nuñez"])]
```

> ¿No nos creés? Ejecutá en la consola en orden las siguientes consultas:
>
> ```python
> arboles[(arboles["barrio"] == "Floresta") | (arboles["barrio"] == "Recoleta") | (arboles["barrio"] == "Belgrano") | (arboles["barrio"] == "Nuñez")]
> ```
>
> ```python
> arboles[arboles["barrio"].isin(["Floresta", "Recoleta", "Belgrano", "Nuñez"])]
> ```
> ¿Arrojan ambas los mismos resultados?
