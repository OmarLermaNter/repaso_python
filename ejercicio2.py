#Este será el método que mostrará el menú
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

#variables globales con las que se crearán id autoincrementale y únicos
id_usuario = 0
id_publicacion = 0
def comprobar_input(input:str):
    import re
    return re.match('^[0-9]+$',input)

#Clase Comentario  
class Comentario:
    def __init__(self,id_publicacion,nombre_usuario:str,texto_comentario:str):
        self.id_publicacion = id_publicacion
        self.nombre_usuario = nombre_usuario
        self.contenido = texto_comentario
    
    #Método que actúa como toString
    def __str__(self):
        return f"{self.nombre_usuario}: {self.contenido}"

#Clase Publicacion
class Publicacion:
    def __init__(self,contenido:str,comentarios: list[Comentario],id_usuario: int):
        global id_publicacion
        id_publicacion += 1
        self.id_usuario = id_usuario
        self.id_publicacion = id_publicacion
        self.contenido = contenido
        self.comentarios = comentarios

    #Métodos que permite ver todos los comentarios de una instancia de Publicacion
    def ver_comentarios(self):
        for comentario in self.comentarios:
            print(comentario)
    
    #Métodos que permite ver los detalles (contenido, comentarios) de una instancia de Publicacion
    def ver_detalles(self):
        comentarios = '['
        for comentario in self.comentarios:
            comentarios += str(comentario) + ','
        comentarios += ']'
        return f'contenido: {self.contenido},comentarios:{comentarios}'
    
    #Método que actúa como toString
    def __str__(self):
        return f'{self.id_publicacion}{self.contenido},{self.comentarios}'

#Clase Usuario
class Usuario:
    def __init__(self,nombre:str,email:str,publicaciones: list[Publicacion]):
        global id_usuario
        id_usuario += 1
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.publicaciones = publicaciones

    #Método que permite crear un usuario dentro una instancia de Usuario
    def crear_publicacion(self,publicacion: Publicacion):
        self.publicaciones.append(publicacion)
        print(publicacion)
        
    #Método que permite ver las publicaciones de una instancia de Usuario
    def ver_publicaciones(self):
        for publicacion in self.publicaciones:
            print(publicacion)
    
    #Método que actúa como toString
    def __str__(self):
        return f'{self.id_usuario},{self.nombre},{self.email}.{self.publicaciones}'
    
#Clase RedSocial, encargada de gestionar todo lo que pasa en el programa
class RedSocial:
    lista_usuarios = []
    lista_publicaciones = []
    
    def __init__(self):
        pass
    
    #Método que permite registrar un usuario
    def registrar_usuario(self, nombre: str, email: str, publicaciones: list[Publicacion]):
        import os
        usuario = Usuario(nombre, email, publicaciones)
        self.lista_usuarios.append(usuario)
        self.guardar_usuarios_en_archivo()

    #Método que permite crear una publicación de un usuario en concreto
    def crear_publicacion(self, id_usuario: int, contenido: str):
        import os
        usuarios = list(filter(lambda usuario: usuario.id_usuario == id_usuario, self.lista_usuarios))
        if len(usuarios) > 0:
            usuario = usuarios[0]
            publicacion = Publicacion(contenido, [], usuario.id_usuario)
            self.lista_publicaciones.append(publicacion)
            usuario.crear_publicacion(publicacion)
            self.guardar_publicaciones_en_archivo()
        else:
            print('No existe un usuario con ese id')

    #Método que permite listar todos los usuarios registrados
    def listar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.lista_usuarios:
            print(f'ID: {usuario.id_usuario} - Nombre: {usuario.nombre} - Email: {usuario.email}')
            if usuario.publicaciones:
                print("  Publicaciones:")
                for publicacion in usuario.publicaciones:
                    print(f"    {publicacion.id_publicacion}: {publicacion.contenido}")
            else:
                print("  No tiene publicaciones.")

    #Método que permite listar todos las publicaciones creadas
    def listar_publicaciones(self):
        print("Publicaciones en la red social:")
        for publicacion in self.lista_publicaciones:
            print(f'ID: {publicacion.id_publicacion} - Usuario ID: {publicacion.id_usuario}')
            print(f'  Contenido: {publicacion.contenido}')
            if publicacion.comentarios:
                print(f'  Comentarios:')
                for comentario in publicacion.comentarios:
                    print(f'    {comentario.nombre_usuario}: {comentario.contenido}')
            else:
                print(f'  No hay comentarios.')

    #Método que permite ver los detalles de una publicación
    def ver_publicacion(self, id_publicacion: int):
        publicaciones = list(filter(lambda publicacion: publicacion.id_publicacion == id_publicacion, self.lista_publicaciones))
        if len(publicaciones) > 0:
            publicacion = publicaciones[0]
            print(f'Contenido: {publicacion.contenido}')
            if publicacion.comentarios:
                print("Comentarios:")
                for comentario in publicacion.comentarios:
                    print(f'{comentario.nombre_usuario}: {comentario.contenido}')
            else:
                print("No hay comentarios en esta publicación.")
        else:
            print("No existe una publicación con ese ID.")
   
    #Método que permite ver los comentarios de una publicación
    def ver_comentarios(self, id_publicacion: int):
        publicaciones = list(filter(lambda publicacion: publicacion.id_publicacion == id_publicacion, self.lista_publicaciones))
        if len(publicaciones) > 0:
            publicacion = publicaciones[0]
            if publicacion.comentarios:
                for comentario in publicacion.comentarios:
                    print(f'{comentario.nombre_usuario}: {comentario.contenido}')
            else:
                print("No hay comentarios en esta publicación.")
        else:
            print("No existe una publicación con ese ID.")
    
    #Método que permite añadir un comentario a una publicación, dando un usuario
    def annadir_comentario(self, id_publicacion: int, id_usuario: int, contenido_comentario: str):
        import os
        try:
            publicaciones = list(filter(lambda publicacion: publicacion.id_publicacion == id_publicacion, self.lista_publicaciones))
            if len(publicaciones) > 0:
                publicacion = publicaciones[0]
                usuarios = list(filter(lambda usuario: usuario.id_usuario == id_usuario, self.lista_usuarios))
                if len(usuarios) > 0:
                    usuario = usuarios[0]
                    comentario = Comentario(publicacion.id_publicacion, usuario.nombre, contenido_comentario)
                    publicacion.comentarios.append(comentario)
                    self.guardar_comentarios_en_archivo()
                else:
                    raise Exception('Usuario no encontrado')
                    
            else:
                raise Exception('Publicación no encontrada')
        except Exception as e:
            print(e)

    #Método que permite guardar los usuarios que se van creando en un archivo
    def guardar_usuarios_en_archivo(self):
        with open('./usuarios.txt', "w") as archivo:
            cabecera = 'id,nombre,email\n'
            archivo.write(cabecera)
            for usuario in self.lista_usuarios:
                datos = f'{usuario.id_usuario},{usuario.nombre},{usuario.email}\n'
                archivo.write(datos)

    #Método que permite guardar las publicaciones que se van creando en un archivo    
    def guardar_publicaciones_en_archivo(self):
        with open('./publicaciones.txt', "w") as archivo:
            cabecera = 'id,usuario_id,contenido\n'
            archivo.write(cabecera)
            for publicacion in self.lista_publicaciones:
                datos = f'{publicacion.id_publicacion},{publicacion.id_usuario},{publicacion.contenido}\n'
                archivo.write(datos)

    #Método que permite guardar los comentarios que se van creando en un archivo
    def guardar_comentarios_en_archivo(self):
        with open('./comentarios.txt', "w") as archivo:
            cabecera = 'publicacion_id,usuario_nombre,comentario\n'
            archivo.write(cabecera)
            for publicacion in self.lista_publicaciones:
                for comentario in publicacion.comentarios:
                    datos = f'{comentario.id_publicacion},{comentario.nombre_usuario},{comentario.contenido}\n'
                    archivo.write(datos)



opcion = ''
red_social = RedSocial()

#Se mostrará el menú siempre que la selección sea distinta a 8, 
# al insertar un id se comprobará que sea un digito numerico sin decimales, utilizando para ello comprobar_input()
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
        while True:
            print('Introduce el id de usuario que quiere crear una publicacion')
            input_introducido = input()
            if comprobar_input(input_introducido):
                break
            print('Introduce un numero sin decimales')
        id_usuario = int(input_introducido)
        print('Introduce el contenido que quieres que tenga la publicacion')
        contenido = input()
        red_social.crear_publicacion(id_usuario,contenido)
   
    elif opcion == '3':
        while True:
            print('Introduce el id de la publicacion a la que se quiere añadir un comentario')
            input_introducido = input()
            if comprobar_input(input_introducido):
                break
            print('Introduce un numero sin decimales')
        id_publicacion = int(input_introducido)
        while True:
            print('Introduce el id del usuario que quiere añadir un comentario')
            input_introducido2 = input()
            if comprobar_input(input_introducido2):
                break
            print('Introduce un numero sin decimales')
        id_usuario = int(input_introducido2)        
        print('Introduce el comentario que quieres que tenga la publicacion')
        comentario = input()
        red_social.annadir_comentario(id_publicacion,id_usuario,comentario)
   
    elif opcion == '4':
        while True:
            print('Introduce el id de la publicacion a la que se quiere conocer detalles')
            input_introducido = input()
            if comprobar_input(input_introducido):
                break
            print('Introduce un numero sin decimales')
        id_publicacion = int(input_introducido) 
        red_social.ver_publicacion(id_publicacion)
   
    elif opcion == '5':
        red_social.listar_usuarios()


    elif opcion == '6':
        red_social.listar_publicaciones()
   
    elif opcion == '7':
        while True:
            print('Introduce el id de la publicacion a la que se quiere añadir un comentario')
            input_introducido = input()
            if comprobar_input(input_introducido):
                break
            print('Introduce un numero sin decimales')
        id_publicacion = int(input_introducido) 
        red_social.ver_comentarios(id_publicacion)
   
    elif opcion == '8':
        print('Se va a salir del programa...')
   
    else:
        print('Elige una opción del 1-8')

