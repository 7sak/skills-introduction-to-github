class Usuario:
    def __init__(self, nombre, clave, correo, rol):
        self.__nombre = nombre
        self.__clave = clave
        self.__correo = correo
        self.__rol = rol

    def get_nombre(self):
        return self.__nombre
    
    def __str__(self):
        print("------------------------------------------------")
        return f"Nombre: {self.__nombre}\nClave: {self.__clave}\nCorreo: {self.__correo}\nRol: {self.__rol}"

    def actualizar_datos (self, new_clave, new_correo, new_rol):
        self.__clave = new_clave
        self.__correo = new_correo
        self.__rol = new_rol

class Sistema_Usuarios:
    def __init__(self):
        self.Lista_Usuarios = []

    def agg_usuario(self, nombre, clave, correo, rol):
        nuevo_usuario = Usuario(nombre, clave, correo, rol)
        self.Lista_Usuarios.append(nuevo_usuario)
        print ("El usuario ha sido creado")
        return True
  
    def eliminar_usuario(self, del_user):
        for usuario in self.Lista_Usuarios:
            if usuario.get_nombre() == del_user:
                self.Lista_Usuarios.remove(usuario)
                print(f"El usuario {del_user} ha sido eliminado")
                return
        print(f"El usuario {del_user} no ha sido encontrado")
               
    def buscar_usuario(self, buscar_usuario):
        for usuario in self.Lista_Usuarios:
            if usuario.get_nombre() == buscar_usuario:
                print(usuario)
                print("El usuario se encuentra registrado")
                print("------------------------------------------------")
                return
        print("El usuario no fue encontrado")

#Crear el objeto sistema para el System User
sistema = Sistema_Usuarios()

while True:
    print("\nOpciones:")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Buscar usuario")
    print("4. Salir")
    opcion = input("Ingrese la opción que desee: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        clave = input("Ingrese la clave del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        rol = input("Ingrese el rol del usuario: ")
        sistema.agg_usuario(nombre, clave, correo, rol)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
        sistema.eliminar_usuario(nombre)

    elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema.buscar_usuario(nombre)
    
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
