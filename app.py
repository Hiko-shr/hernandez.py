import funcion

lista = [] 

while True:
    print('\tmenu')
    print('1. Registrar consumo')
    print('2. Listar los todos los consumos')
    print('3. Imprimir hoja consumo')
    print('4. Buscar un consumo por ID')
    print('5. Salir del programa')
    opcion = input('opcion: ')
    if opcion == '1':
        funcion.registrar_consumo()
    elif opcion == '2':
        funcion.listar_consumo(lista)
    elif opcion == '3':
        funcion.imprimir_consumo(lista)
    elif opcion == '4':
        funcion.buscar_consumo_id(lista)
    elif opcion == '5':
        print('saliendo...')
        break
    else:
        print(f'la {opcion} no valida, estimado.')


