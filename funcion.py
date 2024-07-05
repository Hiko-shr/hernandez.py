import csv
import random


def registrar_consumo():
    nombre = input('nombre: ')
    edad = int(input('edad: '))
    print('\n¿Que equipo?---')
    print('1. Los Genios de la garrafa')
    print('2. Compiladores Despiertos')
    print('3. Código Borracho')
    print('4. Los programadores perezosos')
    print('5. Ctrl+Alt+Derrota')
    equipos = int(input('opcion: '))
    if equipos == 1:
        print('listo')
    elif equipos == 2:
        print('listo')
    elif equipos == 3:
        print('listo')
    elif equipos == 4:
        print('listo')
    elif equipos == 5:
        print('listo')
    else:
        print(f'la opcion {equipos} no valida.') 

    viernes = int(input('viernes: '))
    sabado = int(input('sabado: '))
    domingo = int(input('domingo: '))
    listado = nombre,edad,equipos,viernes,sabado,domingo

def imprimir_consumo():
    with open('listado.csv','w') as archivo:
        escritor  = csv.writer(archivo)
        next (escritor)
        escritor.writerow = ['ID consumo','Jugador','Edad','Equipo','Viernes','Sábado','Domingo']
        escritor.writerows = ()


def listar_consumo(lista):
    for fila in lista:
        ID_especial = random.randint(100000,999999)
        print(ID_especial)
        fila (registrar_consumo)




def buscar_consumo_id():
    id = print()
