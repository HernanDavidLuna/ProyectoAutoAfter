from auto.motor import Motor
from auto.auto import Auto

print('***************************************************')
print('***************Consecionaria CoderHouse************')
print('***************************************************')

print('Opciones (1: Construir Motor, 2: Fabricar Auto, 3: Comprar Auto)')
opcion = int(input('opcion: '))

if opcion == 1:
    codigoMotor = input("Codigo de motor: ")
    nombreMotor = input("Nombre de motor: ")
    
    tipoCombustible = input("Tipo de combustible: ")
    cilindrada = input("Cilindrada: ")
    potencia = input("Potencia: ")
    torque = input("Torque: ")

    newMotor = Motor(tipoCombustible, cilindrada,potencia,torque)
    newMotor.setfabricarMotor(codigoMotor,nombreMotor)

elif opcion == 2:

    newAuto = Auto()
    codigoAuto = input("Codigo Auto: ")
    nombreAuto = input("Nombre Auto: ")

    ruedas = input("Cantidad ruedas: ")
    puertas = input("Cantidad puertas: ")
    tipo = input("Tipo de auto: ")

    newAuto = Auto(ruedas, puertas, tipo)
    newAuto.getlistaMotores()
    codigoMotor = input("Codigo Motor: ")
    newAuto.setfabricarAuto(codigoAuto,nombreAuto,codigoMotor)

elif opcion == 3:

    newAuto = Auto()
    newAuto.getlistarAutos()

    codigoAuto = input("Codigo de Auto: ")

    print(newAuto.getcomprarAuto(codigoAuto))
