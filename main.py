from time import sleep
from Auto import Auto
from Cliente import Cliente

autosRegistrados = []

def Menu():
    
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
    opcion = int(input('Ingrese una opción: '))
    return opcion

def RegistrarAuto():
    print ('Ingrese los datos del auto:')
    placa = input('Placa: ')
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    descripcion = input('Descripción: ')
    precio = float(input('Precio Unitario: '))

    objAuto = Auto(placa, marca, modelo, descripcion, precio)

    autosRegistrados.append(objAuto)

    print()
    print('Registrando auto...')
    sleep(1)
    print()
    print('Auto registrado con éxito')
    sleep(1)
    print()

    for a in autosRegistrados:
        
        print(f'Placa: {a.placa}')
        print(f'Marca: {a.marca}')
        print(f'Modelo: {a.modelo}')
        print(f'Descripción: {a.descripcion}')
        print(f'Precio: {a.precio}')
        print ()

def RegistrarCliente():
    print ('Ingrese los datos del cliente:')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    email = input('Email: ')
    nit = input('NIT: ')

    objCliente = Cliente(nombre, apellido, email, nit)

    print()
    print('Registrando cliente...')
    sleep(1)
    print()
    print('Cliente registrado con éxito')
    sleep(1)
    print()

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
            print('Registrar Cliente')
        elif opcion == 3:
            print('Realizar Compra')
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