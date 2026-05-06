def cargar_paises():
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []
    try: 
        archivo = open("datos/paises.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        
        # Saltar encabezado (primera línea)
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
    except:
        print("Error al guardar")


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
    try:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío")
            return paises
        
        poblacion = input("Población: ").strip()
        if poblacion == "":
            print("Error: la población no puede estar vacía")
            return paises
        poblacion = int(poblacion)
        
        superficie = input("Superficie: ").strip()
        if superficie == "":
            print("Error: la superficie no puede estar vacía")
            return paises
        superficie = int(superficie)
        
        continente = input("Continente: ").strip()
        if continente == "":
            print("Error: el continente no puede estar vacío")
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
        print("Error: debes ingresar números en población y superficie")
    
    return paises


def buscar_pais(paises):
    """Busca un país por nombre."""
    nombre = input("Ingresa el nombre: ")
    encontrado = False
    
    for p in paises:
        if nombre.lower() in p["nombre"].lower():
            print(f"Encontrado: {p}")
            encontrado = True
    
    if not encontrado:
        print("No encontrado")


def filtrar_por_continente(paises):
    """Filtra por continente."""
    continente = input("Continente: ")
    
    print("\n=== RESULTADOS ===")
    for p in paises:
        if p["continente"].lower() == continente.lower():
            print(f"{p['nombre']} - {p['poblacion']} - {p['continente']}")


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
    """Muestra estadísticas básicas."""
    if len(paises) == 0:
        print("Sin datos")
        return
    
    mayor = paises[0]
    menor = paises[0]
    suma = 0
    
    for p in paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p
        suma += p["poblacion"]
    
    promedio = suma / len(paises)
    
    print("\n=== ESTADÍSTICAS ===")
    print(f"Mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio: {promedio:.0f}")
