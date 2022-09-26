Nuevamente te recordamos que este filtrado no altera el dataset original y que podríamos "guardar" los sauces en una variable escribiendo: 

```python
sauces = arboles[arboles["comm_name"].str.startswith('Sauce')]
```

Cómo te podrás imaginar estas no son las únicas operaciones de strings que podemos utilizar. De hecho hay muchas más que las que ya trabajamos y podés conocerlas [acá](https://pandas.pydata.org/docs/user_guide/text.html)