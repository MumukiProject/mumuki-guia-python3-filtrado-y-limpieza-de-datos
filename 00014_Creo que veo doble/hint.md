Uh, ¿pero cómo podríamos saber qué columnas son relevantes a la hora de remover duplicados? 😟 No hay una respuesta única y depende en gran medida de los datos con los que trabajemos. 😭 ¡Pero podemos aplicar algunas _intuiciones_! Por ejemplo, sabemos que las columnas de `arboles` son éstas:

* `long`
* `lat`
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...

¿Podría ser `long` una columna relevante? ¡Claro! Al fin y al cabo hay muchos árboles con el mismo valor de `long`:

```python
ム len(arboles) - arboles["long"].nunique()
# > 1000 ¡probalo!
```

* `long` :white_check_mark:
* `lat`
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...


⚠️ Pero cuidado, porque también podría haber dos árboles en la misma `long` pero diferente `lat`. De hecho, `lat` también es relevante, porque vas a encontrar árboles en la misma ubicación aproximada (igual `lat` y `long`)...

```
ム len(arboles) - len(arboles.drop_duplicates(subset=['long', 'lat']))
# ¡probalo!
```

* `long` :white_check_mark:
* `lat` :white_check_mark:
* `site_type`
* `tree_id`
* `height`
* `diameter`
* ...


…pero quizás de un tipo o altura diferente, así que tenemos que seguir analizando las demás columnas 🤷. ¿Y podría ser `site_type` una columna relevante?

No, porque si vemos su cantidad de valores únicos veremos que hay sólo uno...

```python
ム list(arboles["site_type"].unique())
['Árbol']
```

...y por tanto no nos da ninguna información y no es relevante.

* `long` :white_check_mark:
* `lat` :white_check_mark:
* `site_type` :negative_squared_cross_mark:
* `tree_id`
* `height`
* `diameter`
* ...

¡El resto te toca a vos!




