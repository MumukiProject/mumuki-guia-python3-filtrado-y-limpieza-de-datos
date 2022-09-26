Ya obtuvimos una columna de booleanos pero todavía no vimos todo su potencial 🔥, ¿para qué nos puede ser útil? 

Por ejemplo, con ella podemos _filtrar_ datos de nuestro dataset original y obtener uno nuevo, con sólo las filas que cumplan la condición. La forma de hacerlo es colocando una condición entre corchetes de la siguiente forma: `dataset[condicion]`. En nuestro ejemplo, si hiciéramos...

```python
arboles[arboles["height"] >= 7]
```

...obtendríamos un nuevo dataset con todos los árboles que midan 7 o más metros de alto.. 


> ¡Ahora te toca a vos! Escribí en una nueva celda de tu cuaderno una expresión que nos permita obtener todos los árboles del barrio de `"Palermo"`.
