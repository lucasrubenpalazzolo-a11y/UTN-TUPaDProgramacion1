from funciones import *

paises = cargar_paises()
print(f"Se cargaron {len(paises)} países")

while True:
    print("\n=== Menú de biblioteca de países ===")
    print ("Bienvenido a la biblioteca de países. Aquí puedes gestionar información sobre diferentes países del mundo. Por favor, elige una opción del menú para comenzar.")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Buscar país")
    print("4. Filtrar por continente")
    print("5. Ordenar por población")
    print("6. Estadísticas de población")
    print("7. Guardar los cambios")
    print("0. Salir del programa")
    
    opcion = input("La elección es: ")
    
    if opcion == "1":
        mostrar_paises(paises)
    
    elif opcion == "2":
        paises = agregar_pais(paises)
    
    elif opcion == "3":
        buscar_pais(paises)
    
    elif opcion == "4":
        filtrar_por_continente(paises)
    
    elif opcion == "5":
        ordenar_por_poblacion(paises)
    
    elif opcion == "6":
        estadisticas(paises)
    
    elif opcion == "7":
        guardar_paises(paises)
    
    elif opcion == "0":
        guardar_paises(paises)
        print("Hasta luego. Gracias, por utilizar esta biblioteca de países.")
        break
    
    else:
        print("Opción inválida. Por favor, elige una opción del menú. Recuerda que las opciones válidas son del 0 al 7.")
