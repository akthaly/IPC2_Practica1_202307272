from cliente import Cliente
from auto import Auto
from compra import Compra

listaCLientes = []
listaAutos = []
listaCompras = []
listaSegurosCompleta = []

def Menu():
    print('--------Menú Principal-----------')
    print('1. Registrar Auto')
    print('2. Registrar Cliente')
    print('3. Realizar Comprar')
    print('4. Reporte de Compras')
    print('5. Datos del Estudiante')
    print('6. Salir')
    print('-----------------------------------')

    opcion = int(input('Ingrese una opción: '))
    return opcion
         

def RegistrarAuto():
    placa = input('Ingresa numero de placa: ')
    marca = input('Ingresa la marca: ')
    modelo = input('Ingresa el modelo: ')
    descripcion = input('Ingresa la descripción: ')
    precioUni = float(input('Ingresa el costo: '))

    objAuto = Auto(placa, marca, modelo, descripcion, precioUni)
    listaAutos.append(objAuto)
    print('¡Auto registrado exitósamente!')
    return objAuto

def RegistrarCliente():
    
    nit = input('Ingrese el NIT: ')

    for cliente in listaCLientes:
        if nit == cliente.nit:
            print('El cliente ya está registrado')
            break
    else:
        nombre = input('Ingresa el nombre del cliente: ')
        correo = input('Ingresa el correo electrónico: ')
        cliente = Cliente(nombre, correo, nit)
        listaCLientes.append(cliente)
        print('¡Cliente registrado exitósamente!')
        return cliente

def EncontrarCliente():
    nitIngresado = input('Ingrese el NIT del cliente: ')
    clienteEncontrado = None

    for cliente in listaCLientes:
        if nitIngresado == cliente.nit:
            print('¡Se encontro un cliente exitosamente!')
            clienteEncontrado = cliente
            return clienteEncontrado
    else:
        print('No se encontro ningún cliente :(')
        return clienteEncontrado

def subMenu(cliente):

    if cliente != None:
        print('------------Menú Compra----------------')
        print('1. Agregar Auto')
        print('2. Terminar Comprar y Generar Factura')
        print('---------------------------------------')

        opcion1 = input('Ingrese una opcion: ')
        return opcion1
    
def EncontrarAuto():
        placaIngresada = input('Ingrese la placa del auto que se desea comprar: ')
        autoEncontrado = None

        for auto in listaAutos:
            if placaIngresada == auto.placa:
                print('¡Auto Encontrado Exitosamente!')
                autoEncontrado = auto
                return autoEncontrado
        else:
            print('No se ha encontrado ningun auto')
            return autoEncontrado


def Comprar():

    clienteEncontrado = EncontrarCliente()

    if clienteEncontrado != None:
        id = 0
        id = id + 1
        costoTotal = 0
        costoSeguro = 0
        compra = Compra([], clienteEncontrado, id, [], costoTotal)
        
        opcion = 0

        while opcion != 3:

            opcion = int(subMenu(clienteEncontrado))
            
            if opcion == 1:
                autoEncontrado = EncontrarAuto()
                if autoEncontrado != None:
                    compra.autos.append(autoEncontrado)
                    print('El auto se ha agregado a su compra')
                elif autoEncontrado == None:
                    break
                
            elif opcion == 2:
                print('¿Desea agregar seguro de autos? (Agrega un 15 prociento del costo original a cada auto)')
                print('1. Si')
                print('2. No')

                opcionSeguro = int(input('Ingrese el número: '))

                if opcionSeguro == 1:
                    totalSeguro = compra.CostoSeguroCliente()
                    compra.costoSeguro.append(totalSeguro)
                    listaCompras.append(compra)
                    listaSegurosCompleta.append(totalSeguro)
                    print('El costo total de su compra es: '+ str(totalSeguro))
                    

                elif opcionSeguro == 2:
                    total = compra.CostoTotalCliente()
                    compra.costoSeguro.append(total)
                    listaCompras.append(compra)
                    listaSegurosCompleta.append(total)
                    print('El costo total de su compra es: '+ str(total))
                else: 
                    print('Opción no válida')
                break

            else:
                print('Opción no válida')

def MostrarReporte():
    for reporte in listaCompras:
        print(reporte)

def sumarTotales():
    print(sum([elem for sublista in range(listaSegurosCompleta) for elem in sublista]))

if __name__ == '__main__':
        
    opcion = 0

    while opcion != 6:

        opcion = Menu()

        if opcion == 1:
            auto = RegistrarAuto()
        elif opcion == 2:
            cliente = RegistrarCliente()
        elif opcion == 3:
            Comprar()
        elif opcion == 4:
            MostrarReporte()
            costoTotal = sumarTotales()
            print('Total = '+ str(costoTotal))
        elif opcion == 5:
            print('----------Datos del Estudiante----------')
            print('Mariana Abigail Mejía Garcia')
            print('202300370')
        elif opcion == 6:
            print('Gracias por comprar en autos GT')
        else:
            print('Opción no válida')
