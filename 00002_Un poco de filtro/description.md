Ya obtuvimos una columna de booleanos pero todavía no vimos todo su potencial, ¿para qué nos puede ser útil? 

Por ejemplo, con ella podemos _filtrar_ datos de nuestro dataset original y obtener uno nuevo. La forma de hacerlo es colocando una condición entre corchetes de la siguiente forma: `dataset[condicion]`. Basándonos en nuestro ejemplo anterior, si hiciéramos `arboles[arboles["altura"] >= 3]` obtendríamos un nuevo dataset con todos los árboles cuya altura sea mayor o igual a 3. 

¡Ahora te toca a vos!

> Ejecutá una consulta que nos permita obtener todos los árboles de CABA del barrio de `"Palermo"`.
