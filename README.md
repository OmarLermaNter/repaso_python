# EJERCICIO 1

**Omar Lerma El Atrassi**

## FUNCIONAMIENTO

Al iniciar el programa aparecerá el siguiente menú por consola (en caso de seleccionar cualquier cosa distinta a 7 se volverá a mostrar, en caso de seleccionar una opción del 1-6,
se realizará la acción primero)
```plaintext
=== Gestión de Empleados ===
1. Agregar empleado
2. Buscar empleado por ID
3. Eliminar empleado por ID
4. Mostrar todos los empleados
5. Guardar empleados en un archivo
6. Cargar empleados desde un archivo
7. Salir
```

* OPCION 1

Permite agregar un empleado, el id será auto incremental de forma que no habrá que introducirlo, lo que evitará la repetición de ids, se reinicia cada vez que se ejecuta el programa

Pedirá los atributos nombre, edad, departamento y salario. La introducción de datos estará controlada de forma que sólo se podrán introducir número no decimales en la edad y el sueldo;
en cambio departamento y nombre admitirá únicamente caracteres no decimales(se admiten tildes pero no caracteres especiales)

* OPCION 2

Permite buscar un empleado por id, en caso de encontrarse se mostrará por consola y en caso contrario se mostrará que no se ha encontrado un usuario con ese id

* OPCION 3
  
Permite eliminar un empleado por id, en caso de que sea eliminado se mostrará por consola y en caso contrario se mostrará que no se ha encontrado un usuario con ese id

* OPCION 4

Se muestra una lista con todos los empleados existentes, en caso de no existir ninguno se mostrará una lista vacía

* OPCION 5

Permitirá introducir los empleados existentes en un fichero, pasando la ruta del fichero, esta controlado que **OBLIGATORIAMENTE** se pase la ruta de un fichero *.json*, en caso de
no existir este fichero, primero se creará y luego se almacenarán los datos

* OPCION 6

Permitirá mostrar por consola los empleados existentes en un fichero, pasando la ruta del fichero, esta controlado que **OBLIGATORIAMENTE** se pase la ruta de un fichero *.json*, en caso de no existir este fichero, primero se creará y luego se mostrará el siguiente mensaje ***"fichero ya creado, pero está vacío, añade algunos parámetros"***

* OPCION 7

Finalizará el programa y este mostrará un mensaje despidiendose