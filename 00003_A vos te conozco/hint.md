Para obtener todos los sauces deberíamos fijarnos que el `nombre` de nuestro árbol comience con el string `"Sauce"`. Tené cuidado con la sintaxis tan particular de esta consulta:

`dataset[dataset[columna].str.startswith(string_comienzo)]`