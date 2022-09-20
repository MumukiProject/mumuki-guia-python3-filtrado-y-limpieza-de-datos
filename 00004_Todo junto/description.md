Ya obtuvimos todos los árboles de Palermo y también todos los sauces, ¿se te ocurre cómo podemos obtener todos los sauces de Palermo? 

Vamos a conocer distintas formas de hacerlo:

1. Si por algún motivo necesitamos los árboles de Palermo en general y los sauces en particular podríamos encadenar nuestros filtrados de la siguiente manera:

```python
arboles_de_palermo =  arboles[arboles["barrio"] == "Palermo"]

sauces_de_palermo = arboles_de_palermo[arboles_de_palermo["nombre_com"].str.startswith('Sauce')]
```

2.  Si, en cambio, lo que necesitamos son los sauces en general y los de Palermo en particular podríamos invertir las condiciones anteriores así:

```python
sauces =  arboles[arboles["nombre_com"].str.startswith('Sauce')]

sauces_de_palermo =  sauces[sauces["barrio"] == "Palermo"]
```

3. Peeeero, si lo que realmente nos interesa son solamente los sauces de Palermo podemos filtrar las dos condiciones al mismo tiempo utilizando la conjunción lógica de la siguiente forma:

```python
arboles[(arboles["barrio"] == "PALERMO") & (arboles["nombre_com"].str.startswith("Sauce"))]
```

> ¡Veamos si se entendió! Obtené en la consola aquellos árboles de CABA que se encuentren en la comuna 10 y que sean de la familia de las Meliáceas.
