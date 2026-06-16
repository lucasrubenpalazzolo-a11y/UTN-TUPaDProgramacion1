def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []
    try: 
        archivo = open("datos/paises.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            
            if linea == "":
                continue
            
            partes = linea.split(",")
            
            if len(partes) >= 4:
                try:
                    pais = {
                        "nombre": partes[0].strip(),
                        "poblacion": int(partes[1].strip()),
                        "superficie": int(partes[2].strip()),
                        "continente": partes[3].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error en línea {i+1}: valores numéricos inválidos")
    
    except FileNotFoundError:
        print("ADVERTENCIA: El archivo 'datos/paises.csv' no existe")
        print("Verifica que el archivo esté en la carpeta 'datos'")
    except Exception as e:
        print(f"Error al cargar: {e}")
    
    return paises

def guardar_paises(paises):
    """Guarda la lista en el CSV."""
    try:
        archivo = open("datos/paises.csv", "w")
        archivo.write("nombre,poblacion,superficie,continente\n")
        
        for p in paises:
            linea = p["nombre"] + "," + str(p["poblacion"]) + "," + str(p["superficie"]) + "," + p["continente"] + "\n"
            archivo.write(linea)
        
        archivo.close()
        print("Datos guardados correctamente")
    except Exception as e:
        print(f"Error al guardar, {e}")

def mostrar_paises(paises):
    """Muestra todos los países."""
    if len(paises) == 0:
        print("No hay países")
    else:
        print("\n=== PAÍSES ===")
        for p in paises:
            print(f"{p['nombre']} - {p['poblacion']} hab - {p['superficie']} km² - {p['continente']}")

def agregar_pais(paises):
    """Agrega un nuevo país."""
    continentes_validos = ["america", "asia", "europa", "africa", "oceania", "antartida"]
    try:
        nombre = input("Nombre: ").strip().title()
        print(nombre)
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            return paises

        for p in paises:
            if p["nombre"] == nombre:
                print(f"Error: el país '{nombre}' ya existe en el registro.")
                return paises    
        
        poblacion = input("Población: ").strip()
        if poblacion == "":
            print("Error: la población no puede estar vacía.")
            return paises
        poblacion = int(poblacion)
        
        superficie = input("Superficie: ").strip()
        if superficie == "":
            print("Error: la superficie no puede estar vacía.")
            return paises
        superficie = int(superficie)
        
        continente = input("Continente: ").strip()
        if continente == "":
            print("Error: el continente no puede estar vacío.")
            return paises
        elif continente not in continentes_validos:
            print("Error: el continente escrito no es valido.")
            return paises
        
        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        
        paises.append(pais)
        print("País agregado correctamente")
    except ValueError:
        print("Error: debes ingresar números en población y superficie.")
    
    return paises

def buscar_pais(paises):
    """Busca un país por nombre y ofrece la opción de actualizarlo."""
    nombre = input("Ingresa el nombre del país que deseas buscar: ").strip()
    encontrado = False
    
    for p in paises:

        if nombre.lower() in p["nombre"].lower():
            print(f"\nEncontrado: {p['nombre']} - Población: {p['poblacion']} - Superficie: {p['superficie']} - Continente: {p['continente']}")
            encontrado = True
            
            opcion = input(f"¿Deseas actualizar los datos de {p['nombre']}? (s/n): ").strip().lower()
            
            if opcion == 's':
                try:
                    nueva_pob = input("Nueva población (deja en blanco para mantener la actual): ").strip()
                    if nueva_pob != "":
                        p["poblacion"] = int(nueva_pob)

                    nueva_sup = input("Nueva superficie (deja en blanco para mantener la actual): ").strip()
                    if nueva_sup != "":
                        p["superficie"] = int(nueva_sup)

                    print(f"Datos de {p['nombre']} actualizados correctamente.")
                except ValueError:
                    print("Error: debes ingresar números válidos para la población y la superficie.")

    if not encontrado:
        print("\nError: País no encontrado.")

    return paises

def filtrar_por_continente(paises):
    """Filtra por continente."""
    continentes_validos = ["america", "asia", "europa", "africa", "oceania", "antartida"]
    continente = input("Ingresa el continente que deseas filtrar: ").lower()
    if continente in continentes_validos: 
        print("\n=== RESULTADOS ===")
        for p in paises:
            if p["continente"].lower() == continente:
                print(f"{p['nombre']} - {p['poblacion']} - {p['continente']}")
    else:
        print(f"El continente {continente} no existe.")

def ordenar_por_poblacion(paises):
    """Ordena por población (burbuja)."""
    lista = paises.copy()
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["poblacion"] > lista[j + 1]["poblacion"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    print("\n=== ORDENADO POR POBLACIÓN ===")
    for p in lista:
        print(f"{p['nombre']} - {p['poblacion']}")

def estadisticas(paises):
    """Muestra estadísticas completas."""
    if len(paises) == 0:
        print("Sin datos")
        return
    
    mayor = paises[0]
    menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    conteo_continentes = {}
    
    for p in paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p
        
        suma_poblacion += p["poblacion"]
        suma_superficie += p["superficie"]
        
        cont = p["continente"]
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1
    
    promedio_pob = suma_poblacion / len(paises)
    promedio_sup = suma_superficie / len(paises)
    
    print("\nESTADÍSTICAS")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']} hab)")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']} hab)")
    print(f"Promedio de población global: {promedio_pob:.2f} hab")
    print(f"Promedio de superficie global: {promedio_sup:.2f} km²")
    print("\nCantidad de países por continente:")
    for cont, cantidad in conteo_continentes.items():
        print(f" - {cont}: {cantidad} países")