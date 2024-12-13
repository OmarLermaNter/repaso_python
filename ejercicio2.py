'''
Ejercicio de Examen: Red Social Ficticia
Objetivo:
Desarrollar un programa en Python para gestionar una red social ficticia, donde puedas registrar usuarios, crear publicaciones, agregar comentarios a las publicaciones y listar todo el contenido. La información debe ser persistente, guardándose en archivos de texto (no en listas) y cargándose al iniciar el programa.
Requisitos:
Clase Usuario:
La clase Usuario debe tener los siguientes atributos:
id: Un identificador único para el usuario (número entero).
nombre: Nombre del usuario (cadena de texto).
email: Correo electrónico del usuario (cadena de texto).
publicaciones: Una lista interna de publicaciones del usuario (aunque no usaremos listas globales para almacenar, cada usuario tiene sus publicaciones asociadas).
La clase Usuario debe tener al menos los siguientes métodos:
crear_publicacion: Crear una nueva publicación (se le asociará un ID único).
ver_publicaciones: Mostrar todas las publicaciones del usuario.
Clase Publicacion:
La clase Publicacion debe tener los siguientes atributos:
id: Un identificador único para la publicación (número entero).
contenido: El contenido textual de la publicación (cadena de texto).
comentarios: Lista de comentarios (en cada comentario, almacenar el nombre del usuario que comentó y el texto del comentario).
La clase Publicacion debe tener los siguientes métodos:
agregar_comentario: Permitir agregar comentarios a la publicación.
ver_comentarios: Mostrar todos los comentarios de la publicación.
ver_detalles: Mostrar el contenido de la publicación junto con los comentarios.
Clase RedSocial:
La clase RedSocial será la encargada de manejar todas las interacciones y operaciones dentro de la red social:
registrar_usuario: Permite agregar un nuevo usuario a la red social.
crear_publicacion: Permite a los usuarios crear nuevas publicaciones.
listar_usuarios: Muestra todos los usuarios registrados.
listar_publicaciones: Muestra todas las publicaciones en la red social.
ver_publicacion: Muestra una publicación y sus comentarios.
Persistencia en Archivos:
Los usuarios deben almacenarse en un archivo de texto (usuarios.txt) con el formato:

id,nombre,email
1,Juan Pérez,juan@correo.com
2,Ana Gómez,ana@correo.com


Las publicaciones deben almacenarse en un archivo de texto (publicaciones.txt) con el formato:

id,usuario_id,contenido
1,1,"Mi primer post"
2,2,"Me encanta esta red social"


Los comentarios deben almacenarse en un archivo de texto (comentarios.txt) con el formato:

publicacion_id,usuario_nombre,comentario
1,Juan Pérez,"¡Qué genial!"
2,Ana Gómez,"Totalmente de acuerdo"


Menú de Interacción:
El programa debe permitir al usuario interactuar mediante un menú en consola:
Crear un usuario.
Crear una publicación (por un usuario).
Agregar un comentario a una publicación.
Ver los detalles de una publicación.
Listar todos los usuarios.
Listar todas las publicaciones.
Ver los comentarios de una publicación.

'''
def mostrar_menu():
    print("\nMenu:")
    print("1. Crear un usuario.")
    print("2. Crear una publicación (por un usuario).")
    print("3. Agregar un comentario a una publicación.")
    print("4. Ver los detalles de una publicación.")
    print("5. Listar todos los usuarios.")
    print("6. Listar todas las publicaciones.")
    print("7. Ver los comentarios de una publicación.")
    print("8. Salir.")
class Comentario:
    def __init__(self,nombre_usuario:str,texto_comentario:str):
        self.nombre_usuario = nombre_usuario
        self.contenido = texto_comentario
class Publicacion:
    ultimo_id = 0
    def __init__(self,contenido:str,comentarios: list[Comentario],):
        self.ultimo_id+=1
        self.id_publicacion = self.ultimo_id
        self.contenido = contenido
        self.comentarios = comentarios
    def ver_comentarios(self):
        print(self.comentarios)
    def ver_detalles(self):
        return {'contenido': self.contenido,'comentarios':self.comentarios}
class Usuario:
    ultimo_id = 0
    def __init__(self,nombre:str,email:str,publicaciones: list[Publicacion]):
        self.ultimo_id += 1
        self.id_usuario = self.ultimo_id
        self.nombre = nombre
        self.email = email
        self.publicaciones = publicaciones
    
    def crear_publicacion(self,contenido):
        self.publicaciones.append(Publicacion(contenido,[]))
    def ver_publicaciones(self):
        return self.publicaciones
    '''
    Clase RedSocial:
La clase RedSocial será la encargada de manejar todas las interacciones y operaciones dentro de la red social:
registrar_usuario: Permite agregar un nuevo usuario a la red social.
crear_publicacion: Permite a los usuarios crear nuevas publicaciones.
listar_usuarios: Muestra todos los usuarios registrados.
listar_publicaciones: Muestra todas las publicaciones en la red social.
ver_publicacion: Muestra una publicación y sus comentarios.'''
class RedSocial:
    lista_usuarios = []
    lista_publicaciones = []
    def __init__(self):
        pass
    def registrar_usuario(self,nombre:str,email:str,publicaciones: list[Publicacion]):
        self.lista_usuarios.append(Usuario(nombre,email,publicaciones))
    def crear_publicacion(self,id_usuario:int,contenido:str):
        usuario= list(filter(lambda usuario: usuario.ultimo_id == id_usuario,self.lista_usuarios))[0]
        usuario.crear_publicacion(contenido)
    def listar_usuarios(self):
        print(self.lista_usuarios)
    def listar_publicaciones(self):
        print(self.lista_publicaciones)
    def ver_publicacion(self,id_publicacion:int):
        publicacion= list(filter(lambda publicacion: publicacion.ultimo_id == id_publicacion,self.lista_publicaciones))[0]
        return publicacion.ver_detalles()
    def ver_comentarios(self,id_publicacion:int):
        publicacion= list(filter(lambda publicacion: publicacion.ultimo_id == id_publicacion,self.lista_publicaciones))[0]
        publicacion.ver_comentarios()
        #asd
    def annadir_comentario(self,id_publicacion:int,comentario:str):
        publicacion= list(filter(lambda publicacion: publicacion.ultimo_id == id_publicacion,self.lista_publicaciones))[0]
        publicacion.comentarios.append(comentario)

opcion = ''
red_social = RedSocial()
while opcion != '8':
    mostrar_menu()
    opcion = input()
    if opcion == '1':
        print('Introduce un nombre')
        nombre = input()
        print('Introduce un email')
        email = input()
        red_social.registrar_usuario(nombre,email,[])
    
    elif opcion == '2':
        print('Introduce el id de usuario que quiere crear una publicacion')
        id_usuario = int(input())
        print('Introduce el contenido que quieres que tenga la publicacion')
        contenido = input()
        red_social.crear_publicacion(id_usuario,contenido)
   
    elif opcion == '3':
        print('Introduce el id de la publicacion a la que se quiere añadir un comentario')
        id_publicacion = int(input())
        print('Introduce el comentario que quieres que tenga la publicacion')
        comentario = input()
        red_social.annadir_comentario(id_publicacion,comentario)
    
    elif opcion == '4':
        print('Introduce el id de la publicacion a la que se quiere ver los detalles')
        id_publicacion = int(input())
        red_social.ver_publicacion(id_publicacion)
    
    elif opcion == '5':
        red_social.listar_usuarios()

    elif opcion == '6':
        red_social.listar_publicaciones()
    
    elif opcion == '7':
        print('Introduce el id de la publicacion a la que se quiere ver los comentarios')
        id_publicacion = int(input())
        red_social.ver_comentarios(id_publicacion)
    
    elif opcion == '8':
        print('Se va a salir del programa...')
    
    else:
        print('Elige una opción del 1-8')