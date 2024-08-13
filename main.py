from time import sleep
from Auto import Auto
from Cliente import Cliente
from Compra import Compras

autosRegistrados = []
clientesRegistrados = []
listaCompras = []
autosID = 0

def Menu():
    # Limpiar la pantalla
    print('====================')
    print('Super Autos GT')
    print('====================')
    print('Menú Principal')
    print('')
    print('1. Registrar Auto')
    print('2. Registrar Cliente')
    print('3. Realizar Compra')
    print('4. Reporte de Compras')
    print('5. Datos del Estudiante')
    print('6. Salir')
    print('')
    opcion = int(input('Ingrese una opción: ')) # Convertir a entero la opción ingresada por el usuario
    return opcion # Retornar la opción

def MenuCompra():
    print('========= Menú Compra =========')
    print('1. Agregar auto al carrito')
    print('2. Terminar Compra y Facturar')
    opcion = int(input('Ingrese una opción: '))
    print('===============================')
    return opcion


def RegistrarAuto():

    
    print ('Ingrese los datos del auto:')
    placa = input('Placa: ')
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    descripcion = input('Descripción: ')
    precio = float(input('Precio Unitario: '))

    # Crear un objeto de tipo Auto con los datos ingresados 

    objAuto = Auto(placa, marca, modelo, descripcion, precio)

    autosRegistrados.append(objAuto) # Agregar el objeto a la lista de autos registrados

    print()
    print('Registrando auto...')
    sleep(1)
    print()
    print('Auto registrado con éxito')
    sleep(1)
    print()

    for a in autosRegistrados: # Recorrer la lista de autos registrados
        print(a) # Imprimir los datos del auto

def RegistrarCliente():
    print ('Ingrese los datos del cliente:')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    email = input('Email: ')
    nit = int(input('NIT: '))

    # Crear un objeto de tipo Cliente con los datos ingresados
    objCliente = Cliente(nombre, apellido, email, nit)

    # Agregar el objeto a la lista de clientes registrados
    clientesRegistrados.append(objCliente)

    print()
    print('Registrando cliente...')
    sleep(1)
    print()
    print('Cliente registrado con éxito')
    sleep(1)
    print()

    for c in clientesRegistrados:
        print(c)

def RealizarCompra():
    nitComprador = int(input('Ingrese su número de NIT: '))

    cliente_Encontrado = None

    for cliente in clientesRegistrados:
        if nitComprador == cliente.nit:
            cliente_Encontrado = cliente
            break

    if cliente_Encontrado:
        compraActual = Compras([], cliente_Encontrado, autosID)
        opcion = MenuCompra()
        while opcion != 3:
            if opcion == 1:
                # CarritoCompras()
                print('Autos Disponibles:')
                print()
                for a in autosRegistrados:
                    print(a)
                print()
                placa = input('Ingrese el número de placa para agregar el auto a la compra: ')    

                auto_encontrado = False

                for auto in autosRegistrados:
                    if placa == auto.placa:
                        compraActual.autos.append(auto)
                        autosRegistrados.remove(auto)
                        print('Auto agregado al carrito')
                        auto_encontrado = True
                        break
                
                if not auto_encontrado:
                    print('Placas no encontradas, ingrese una placa válida')
                
                opcion = MenuCompra()
        
                listaCompras.append(compraActual)
                print('Compra finalizada')
                #print(autosComprados)

            elif opcion == 2:
                print('Desea Agregar Seguro a la compra?')
                print('1. Si')
                print('2. No')
                seguro = int(input('Ingrese una opción: '))
                while seguro != 3:
                    if seguro == 1:
                        print('----------Reporte de Compras----------')
                        print('======================================')
                        print(compraActual)
                        print('TOTAL:', compraActual.totalCompraSeguro())
                        break
                    elif seguro == 2:
                        print('----------Reporte de Compras----------')
                        print('======================================')
                        print(compraActual)
                        print('TOTAL:', compraActual.totalCompra())
                        break

                    else:
                        print('Opción no válida')
                        seguro = int(input('Ingrese una opción: '))
                break
                
            
    else:
        print('Usuario no encontrado, por favor verifique su NIT o registrese como cliente')



def DatosEstudiante():
    print('====================')
    print('Datos del Estudiante')
    print('====================')
    print('Nombre: Bryan Alejandro Anona Paredes')
    print('Carnet: 202307272')



if __name__ == '__main__':
    opcion = Menu()

    while opcion != 6:
        if opcion == 1:
            print()
            print('====================')
            print('Registrar Auto')
            print('====================')
            print()
            RegistrarAuto()
        elif opcion == 2:
            print()
            print('====================')
            print('Registrar Cliente')
            print('====================')
            print()
            RegistrarCliente()
        elif opcion == 3:
            print('Realizar Compra')
            RealizarCompra()
        elif opcion == 4:
            print('Reporte de Compras')
        elif opcion == 5:
            print('')
            sleep(1)
            DatosEstudiante()
            sleep(1)
            print('')
        else:
            print('Opción no válida')
        
        opcion = Menu()