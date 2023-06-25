import json

def decorar(titulo):  #decora con bolitas negras
    print("•"*30)
    print(titulo)
    print("•"*30)
def decorarDos(titulo):#decora con bolitas vacias
    print("o"*30)
    print(titulo)
    print("o"*30)

def altaProducto(listado): # [{},{}]
    decorar("Ingreso de nuevo producto")
    codigo = str(input("Ingresa el codigo del producto: "))
    nombre = input("Ingresa el nombre del producto: ")
    categoria = input("Ingresa la categoria del producto: ")
    origen = input("Ingrese pais de origen del producto: ").casefold()
    while True:
        try:
            stock = int(input("Ingrese stock del producto: "))
            break
        except:
            print("El stock debe ser un entero")
    producto = {
        "Codigo":codigo.casefold(),
        "Nombre":nombre.casefold(),
        "Categoria":categoria.casefold(),
        "Stock":stock, 
        "Origen":origen
    }
    listado.append(producto)
    arch = open("productos.json","w")
    json.dump(listado,arch,indent=2)
    arch.close()

def eliminarProducto(listado):# Se el producto entero{}
    decorar("Eliminando producto")
    codigoAEliminar = input("Ingrese el codigo del producto a eliminar: ")
    for producto in listado:
        if producto["Codigo"] == codigoAEliminar:
            listado.remove(producto)
            print("El producto fue eliminado con exito")
    arch = open("personas.json","w")
    json.dump(listado,arch,indent=2)
    arch.close()

def modificarProducto(listado, elemento): 
    decorar(f"Modificando {elemento}")
    while True:
        print('''Datos
        1-Nombre
        2-Categoria
        3-Origen
        4-Stock
        0-Salir
        ''')
        opcionDato=input("Ingrese el dato a modificar: ")
        if opcionDato=="1":            
            elemento['Nombre']=input(f"Ingrese el nuevo nombre del producto: ")
        elif opcionDato=="2":
            elemento['Categoria']== input(f"Ingrese nueva categoria: ")
        elif opcionDato=="3":
            elemento['Origen']=input("Ingrese origen del elemento: ")
        elif opcionDato=="4":
            while True:
                try:
                    elemento['Stock']= int(input("Ingrese el stock actual del producto: "))
                    break
                except:
                    print("El stock debe ser un entero")
        elif opcionDato=="0":
            break
        arch = open("productos.json","w")
        json.dump(listado,arch,indent=2)
        arch.close()

def altaUsuario(listado): # [{},{}]
    decorar("Primer ingreso")
    dniNuevo = int(input("Ingresa tu DNI como usuario: "))
    claveNueva = int(input("Ingresa una clave de 4 digitos: "))
    usuarioNuevo = {
        "Usuario":dniNuevo,
        "Clave":claveNueva,
    }
    
    listado.append(usuarioNuevo)
    arch = open("usuarios.json","w")
    json.dump(listado,arch,indent=2)
    arch.close()
