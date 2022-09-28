Cuando hablamos de limpiar nuestro dataset claro que no vamos a pasarle la escoba para sacarle el polvo 🧹. Limpieza de datos se refiere por ejemplo a verificar si faltan datos o si a alguna de las columnas debe hacerseles una corrección de notación o de tipo de dato, etc.

Una forma de obtener esta información es con el ya conocido `info` que, entre otras cosas, nos permite saber qué datos están faltantes o, dicho de otra forma, son nulos. Pero vamos a conocer otra manera de hacerlo con `isna`. 

> Probá en tu cuaderno hacer `arboles[arboles["street"].isna()]` y verificá si se eliminan árboles. ¿Cuántos quedan?
