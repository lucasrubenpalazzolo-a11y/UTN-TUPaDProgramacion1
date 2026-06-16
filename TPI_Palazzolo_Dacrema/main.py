import funciones as fn #importa las diferentes funciones de forma más seguro bajo el alias de "fn"

paises = fn.cargar_paises()
print(f"Se cargaron {len(paises)} países")

def inicio_programa(paises):
    while True:
        print("\n=== Menú de biblioteca de países ===")
        print("Bienvenido a la biblioteca de países. Aquí puedes gestionar información sobre diferentes países del mundo. Por favor, elige una opción del menú para comenzar.")
        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Ordenar por población")
        print("6. Estadísticas de población")
        print("7. Guardar los cambios")
        print("0. Salir del programa")
        
        opcion = input("La elección es: ")
        
        try:
            if opcion == "1":
                fn.mostrar_paises(paises)
            
            elif opcion == "2":
                paises = fn.agregar_pais(paises)
            
            elif opcion == "3":
                fn.buscar_pais(paises)
            
            elif opcion == "4":
                fn.filtrar_por_continente(paises)
            
            elif opcion == "5":
                fn.ordenar_por_poblacion(paises)
            
            elif opcion == "6":
                fn.estadisticas(paises)
            
            elif opcion == "7":
                fn.guardar_paises(paises)
            
            elif opcion == "0":
                fn.guardar_paises(paises)
                print("Hasta luego. Gracias por utilizar esta biblioteca de países.")
                break
            
            else:
                print("Opción inválida. Por favor, elige una opción del menú. Recuerda que las opciones válidas son del 0 al 7.")
                
        except Exception as e:
            # Aquí está tu mensaje personalizado para cualquier error inesperado
            print("\nAlgo salió mal al intentar realizar esta acción.")
            print(f"El sistema reportó este error: {e}")
            print("Por favor, verifica los datos que ingresaste e intenta nuevamente.\n")

if __name__ == "__main__":
    inicio_programa(paises)