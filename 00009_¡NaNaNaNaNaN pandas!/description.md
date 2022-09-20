En el ejercicio anterior obtuvimos aquellas filas que tienen `NaN` en la columna `calle`. `NaN` (por las siglas de _Not a Number_ en inglés) es un valor que se suele utilizar para representar la ausencia del dato (también conocida en inglés como _Not Available_ o _NA_). ¿Qué hacemos en estos casos? 

A decir verdad, no hay una única respuesta: dependiendo de nuestro lote de datos y de la variable en cuestión deberemos tomar distintas decisiones. Por ejemplo,  algo que podemos hacer es quitar aquellas filas que tienen un valor `NaN` en una columna específica utilizando `notna`  ✂️. `notna` funciona al revés que `isna` y nos devuelve verdadero cuando el valor no es nulo.

> Ejecutá en la consola la consulta que nos permita obtener sólo aquellos árboles que tengan cargada una calle. 
