import json
import moduloTPF as m


file1 = open("usuarios.json","r")
usuarios = json.load(file1) # [{},{}]
file1.close()

file2 = open("productos.json","r")
productos = json.load(file2) # [{},{}]
file2.close()


while True:
    m.decorar("Ingreso al sistema")
    print('''
    1-Ingreso por primera vez
    2-Login
    ''')
    opcionIngreso=int(input("Seleccione 1 si es su primer ingreso o 2 para loguearse: "))
    if opcionIngreso==1:
        m.altaUsuario(usuarios)
    elif opcionIngreso==2:
        dni = int(input("Ingresa tu DNI: "))
        clave = int(input("Ingresa su clave de 4 digitos: "))
        for usuario in usuarios:            
            if (usuario["Usuario"]==dni and usuario["Clave"]==clave):
                print("Bienvenido al sistema")
                while True:
                    m.decorar("Gestion de stock")
                    print("""
                    1-Gestion de productos
                    2-Reportes
                    0-Salir
                    """)
                    opcion = input("Ingrese opcion: ")
                    if opcion == "0":
                        print("Usted ha salido del sistema, muchas gracias!")
                        break
                    elif opcion == "1":
                        while True:
                            m.decorar("Gestion de productos")
                            print("""
                            1-Ingresar nuevo producto
                            2-Listado de productos
                            3-Modificar un producto
                            4-Eliminar un producto
                            0-Volver al menu principal
                            """)
                            opcionDos=input("Ingrese una opcion del Menu: ")
                            if opcionDos=="1":
                                m.altaProducto(productos)
                            elif opcionDos=="2":
                                m.decorar("Listado de productos actual")
                                for producto in productos:
                                    print(producto)
                            elif opcionDos=="3":
                                codigo = input("Ingrese el codigo del producto: ")
                                for prod in productos: # [{},{}]
                                    if codigo == prod["Codigo"]: # 44 == {}
                                        m.modificarProducto(productos,prod)
                                        break
                                else:
                                    print("El codigo no existe")
                                    continue
                            elif opcionDos=="4":
                                m.eliminarProducto(productos)
                            elif opcionDos=="0":
                                break
                    elif opcion == "2":
                        while True:
                            m.decorarDos("Reportes")
                            print("""
                            1-Mostrar productos nacionales
                            2-Mostrar productos importados
                            3-Mostrar stock de productos
                            4-Mostrar productos por categoria
                            0-Volver al Menu principal
                            """)
                            opcionTres=input("Ingrese una opcion del Menu: ")
                            if opcionTres=="0":
                                break
                            if opcionTres=="1":
                                cant=0
                                for producto in productos:
                                    pais="Argentina"
                                    if producto["Origen"].casefold() == pais.casefold():
                                        cant+=1
                                        print(f"Producto:{producto['Nombre'].upper()}-Origen {producto['Origen'].upper()}")
                                print(f"Hay {cant} tipo/s de producto/s de origen nacional en stock")
                            elif opcionTres=="2":
                                cant=0
                                for producto in productos:
                                    if producto["Origen"].casefold()!="Argentina".casefold():
                                        cant+=1
                                        print(f"Producto:{producto['Nombre'].upper()}-Origen {producto['Origen'].upper()}")
                                print(f"Hay {cant} tipo/s de producto/s de origen importado en stock")
                            elif opcionTres=="3":
                                for producto in productos:
                                    print(f"Hay {producto['Stock']} unidades en stock de {producto['Nombre'].upper()}")
                            elif opcionTres=="4":
                                categ=input("Ingrese la categoria a filtrar: ")
                                for producto in productos:
                                    print("")
                                    if producto["Categoria"].upper()==categ.upper():
                                        print(f"-{producto['Nombre'].upper():8} pertenece a la categoria {producto['Categoria'].upper()}")
        else:
            print("      :(           ")
            print("El usuario ingresado no esta en la base")
            continue





