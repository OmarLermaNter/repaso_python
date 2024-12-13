id_empleados = 0
empleados = []
#Esta será la función llamada para mostrar el menú tantas veces como sea necesario
def mostrar_menu():
    print('''
=== Gestión de Empleados ===
1. Agregar empleado  
2. Buscar empleado por ID  
3. Eliminar empleado por ID  
4. Mostrar todos los empleados  
5. Guardar empleados en un archivo  
6. Cargar empleados desde un archivo  
7. Salir
''')
    
#Esta será la función llamada para comprobar que el formato de los parámetros pasados por consola son correctos, pasando en su llamada el parámetro y el formato que se quiere comprobar.
#Pudiendo ser : 
# #numero -> comprueba que sea una sucesión de números decimales
# #cadena -> comprueba que sea una sucesión de caracteres normales(incluyendo tildes pero excluyendo caracteres como -*/_.:,)
def comprobar_input(input: str,formato_comprobar: str):
    import re
    if(formato_comprobar == 'cadena'):
        return re.match('^[a-záéíóúñ]+$',input.lower())
    elif(formato_comprobar == 'numero'):
        return re.match('^[0-9]+$',input)

#Esta será la función encargada de pedir los atributos necesarios para crear un empleado, comprobando el formato de cada una de las entradas por consola, en caso de que no tenga un formato correcto
#se mostrará un mensaje con el formato deseado y se volverá a pedir la entrada de datos. Retorna un array con los atributos que se usarán para crear el empleado
#El id será autoincremental, evitando que se repitan, en caso de que no haya ningún empleado se asignará 1
def pedir_atributos_empleado(id_empleados : int):
    id = id_empleados
    nombre = ''
    edad = ''
    departamento = ''
    salario = ''
    while True:
        print('Ingresa el nombre del empleado') 
        nombre_input = input() 
        if(comprobar_input(nombre_input, 'cadena')):
            nombre = nombre_input
            break
        else:
            print('Ingresa una cadena sin caracteres especiales')

    while True:
        print('Ingresa el edad del empleado') 
        edad_input = input() 
        if(comprobar_input(edad_input, 'numero')):
            edad = edad_input
            break
        else:
            print('Ingresa un número sin decimales')

    while True:
        print('Ingresa el departamento del empleado') 
        departamento_input = input() 
        if(comprobar_input(departamento_input, 'cadena')):
            departamento = departamento_input
            break
        else:
            print('Ingresa una cadena sin caracteres especiales')

    while True:
        print('Ingresa el salario del empleado') 
        salario_input = input() 
        if(comprobar_input(salario_input, 'numero')):
            salario = salario_input
            break
        else:
            print('Ingresa un número sin decimales')
    
    return [id,nombre,edad,departamento,salario]


#Esta será la función empleada para poder obtener todos los empleados reflejados en el fichero, habrá que pasar en la llamada de la función la ruta del fichero
def obtener_empleados_fichero(ruta):
    import json
    import os
    if(os.path.exists(ruta)):
        with open(ruta,'r') as fichero:
            empleados_fichero = json.load(fichero)
        print(empleados_fichero)
    else:
        print(f'no existe el fichero {ruta}, se va a crear...')
        open(ruta,'x')
        print(f'fichero ya creado, pero está vacío, añade algunos parámetros')

#Esta será la función empleada para poder reflejar los empleados del programa en un archivo
def sobrescribir_archivo(ruta):
    import os
    import json
    if os.path.exists(ruta):
        with open(ruta,'w') as archivo:
            json.dump(empleados,archivo)
    else:
        open(ruta,'x')
        with open(ruta,'w') as archivo:
            json.dump(empleados,archivo)

#Esta será la función empleada para poder obtener todos los empleados
def obtener_empleados():
    print(empleados)
    
#Esta será la función empleada para poder añadir empleados
def annadir_empleado(id_empleado: int):
    atributos = pedir_atributos_empleado(id_empleados)
    empleado_annadir = {'id':atributos[0],'nombre':atributos[1],'edad':atributos[2],'departamento':atributos[3],'salario':atributos[4]}
    empleados.append(empleado_annadir)

#Esta será la función empleada para poder eliminar empleados
def eliminar_empleado(id):
    tamanno = len(empleados)
    for empleado in empleados:
        if empleado.get('id') == int(id):
            empleados.remove(empleado)
            print('Se ha eliminado correctamente')
    if tamanno == len(empleados):
        print('No se ha encontrado ningún empleado con ese id')

#Esta será la función empleada para poder buscar un empleado por id
def buscar_empleado(id):
    busqueda = list(filter(lambda empleado: empleado.get('id') == int(id),empleados))
    if(len(busqueda)>0):
        print(busqueda[0])
    else:
        print('No se ha encontrado ningún empleado')

opcion = ''
while opcion != '7':
    mostrar_menu()
    opcion = input()
    if opcion == '1':
        id_empleados += 1
        annadir_empleado(id_empleados)
    elif opcion == '2':
        while True:
            print('Introduce el id por el que quieres buscar')
            id_buscar = input()
            if comprobar_input(id_buscar,'numero'):
                break
        buscar_empleado(id_buscar)
    elif opcion == '3':
        while True:
            print('Introduce el id del empleado que quieres eliminar')
            id_eliminar = input()
            if comprobar_input(id_eliminar,'numero'):
                break
        eliminar_empleado(id_eliminar)
    elif opcion == '4':
        obtener_empleados()
    elif opcion == '5':
        while True:
            print('Introduce la ruta de un archivo json')
            ruta = input()
            if ruta.endswith('.json'):
                break
        sobrescribir_archivo(ruta)
    elif opcion == '6':
        while True:
            print('Introduce la ruta de un archivo json')
            ruta = input()
            if ruta.endswith('.json'):
                break
        obtener_empleados_fichero(ruta)
    elif opcion == '7':
        print('Se va a salir del programa...')
    else:
        print('Opción no válida, introduce un número del 1-7')