# %% [markdown]
# Programación 1
# 
# Trabajo Práctico N°2
# 
# Alumno: Lucas Rubén Palazzolo López

# %% [markdown]
#  Ejercicio1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# %% [markdown]
# Pseudocódigo:
# 
# Algoritmo MayoriaEdad
# 
#     Escribir "Calculadora de mayoría de edad 🔞"
#     Escribir "Por favor, ingrese su edad:"
#     Leer entrada
#     
#     // Validamos si la entrada es un número
# 
#     Si NO Es_Numerico(entrada) Entonces
#         Escribir "¡Epa! No sabía que cumplías años en abecedario. 🧐"
#         Escribir "Por favor, ingrese una edad válida."
#     Sino
#         // Convertimos el texto a número real para operar
#         edad <- ConvertirANumero(entrada)
#         
#         Si edad < 0 Entonces
#             Escribir "La edad no puede ser negativa. ❌"
#             
#         Sino Si edad >= 120 Entonces
#             Escribir "🤔 ¡Epa! Esa edad parece un récord mundial."
#             Escribir "¿Sos un cyborg o un vampiro?"
#             
#         Sino Si edad >= 18 Entonces
#             Escribir "Es mayor de edad. ✅"
#             
#         Sino
#             Escribir "No es mayor de edad. 🧒"
#         FinSi
#         
#     FinSi
#     
#     Escribir "Fin del programa. ¡Gracias! 👋"
# FinAlgoritmo

# %%
print("Calculadora de mayoría de edad 🔞")
entrada = input("Por favor, ingrese su edad: ").isdigit().strip()      

if not entrada.isdigit():
    print("¡Epa! No sabía que cumplías años en abecedario. 🧐. Por favor, ingrese una edad valida")
else:
    edad = int(entrada)
    if edad < 0:
        print("La edad no puede ser negativa. Por favor, ingrese una edad válida. ❌")
    elif edad >= 120:
        print("🤔 ¡Epa! Esa edad parece un récord mundial, verificala  ¿Sos un cyborg o un vampiro?")
    elif edad >= 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

print("Fin del programa ¡Gracias por usar la calculadora de mayoría de edad! 👋")

# %% [markdown]
# Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”. 

# %% [markdown]
# Algoritmo CalculadoraNotas
# 
#     Escribir "Calculadora de notas aprobatorias o desaprobatorias 📚"
#     Escribir "Por favor, ingrese su nota:"
#     Leer nota_entrada
#     
#     Si NO Es_Numerico(nota_entrada) Entonces
#         Escribir "¡Epa! No sabía que las notas se escribían en letras. 🧐"
#     Sino
#         nota <- ConvertirANumero(nota_entrada)
#         
#         Si nota < 0 O nota > 10 Entonces
#             Escribir "La nota debe estar entre 0 y 10. ❌"
#             
#         Sino Si nota >= 6 Entonces
#             Escribir "Aprobado. ✅"
#             
#         Sino
#             Escribir "Desaprobado. 📕"
#         FinSi
#         
#     FinSi
#     
#     Escribir "Fin del programa 👋"
# FinAlgoritmo

# %%
print("Calculadora de notas aprobatorias o desaprobatorias 📚")
nota_entrada = input("Por favor, ingrese su nota: ").strip()
if not nota_entrada.isdigit():
    print("¡Epa! No sabía que las notas se escribían en letras. 🧐. Por favor, ingrese una nota válida")
else:
    nota = int(nota_entrada)
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10. Por favor, ingrese una nota válida. ❌")
    elif nota >= 6:
        print("Aprobado.")
    else:
        print("Desaprobado.")

print("Fin del programa ¡Gracias por usar la calculadora de notas! 👋")

# %% [markdown]
# Ejercicio 3:  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje. "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

# %% [markdown]
# Algoritmo VerificadorPares
# 
#     Escribir "Verificador de números pares 🧮"
#     Escribir "Por favor, ingrese un número:"
#     Leer entrada
#     
#     Si NO Es_Numerico(entrada) Entonces
#         Escribir "¡Epa! No sabía que los números se escribían en letras. 🧐"
#     Sino
#         num <- ConvertirANumero(entrada)
#         
#         // Usamos MOD para saber el resto de la división
#         Si num MOD 2 = 0 Entonces
#             Escribir "✅ El número es PAR."
#         Sino
#             Escribir "❌ El número es IMPAR."
#         FinSi
#         
#     FinSi
#     
#     Escribir "Fin del programa. 👋"
# FinAlgoritmo

# %%
print (f"Verificador de números pares 🧮")
numero_entrada = input("Por favor, ingrese un número: ").strip()
if not numero_entrada.isdigit():
    print("¡Epa! No sabía que los números se escribían en letras. 🧐. Por favor, ingrese un número válido" )
else:
    numero = int(numero_entrada)
    if numero % 2 == 0:
        print("Ha ingresado un número par.")
    else:
        print("Ha ingresado un número impar, por favor, ingresar un número par.")

print("Fin del programa ¡Gracias por usar el verificador de números pares! 👋")   

# %% [markdown]
# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece: 

# %% [markdown]
# Algoritmo ClasificacionEtapasVida
# 
#     Escribir "Calculadora de etapas de vida 🧬"
#     Escribir "Por favor, ingrese su edad:"
#     Leer entrada
#     
#     Si NO Es_Numerico(entrada) Entonces
#         Escribir "¡Epa! No sabía que cumplías años en abecedario. 🧐"
#     Sino
#         edad <- ConvertirANumero(entrada)
#         
#         Si edad < 0 Entonces
#             Escribir "La edad no puede ser negativa. ❌"
#         Sino Si edad >= 120 Entonces
#             Escribir "¡Epa! Esa edad parece un récord mundial. 🧛‍♂️"
#             
#         // Aplicamos los rangos de la consigna
#         Sino Si edad < 12 Entonces
#             Escribir "Pertenece a la categoría: Niño/a."
#             
#         Sino Si edad >= 12 Y edad < 18 Entonces
#             Escribir "Pertenece a la categoría: Adolescente."
#             
#         Sino Si edad >= 18 Y edad < 30 Entonces
#             Escribir "Pertenece a la categoría: Adulto/a joven."
#             
#         Sino
#             Escribir "Pertenece a la categoría: Adulto/a."
#         FinSi
#         
#     FinSi
#     
#     Escribir "Fin del programa. 👋"
# FinAlgoritmo

# %%
print("Calculadora de etapas de vida 🧬")
edad_entrada = input("Por favor, ingrese su edad: ").strip()

if not edad_entrada.isdigit():
    print("¡Epa! No sabía que cumplías años en abecedario. 🧐")
else:
    edad = int(edad_entrada)
    
    if edad < 0:
        print("La edad no puede ser negativa. ❌")
    elif edad >= 120:
        print("🤔 ¡Récord mundial! ¿Sos un cyborg o un vampiro?")
    
    elif edad < 12:
        print("Pertenece a la categoría: Niño/a.")
    
    elif 12 <= edad < 18:
        print("Pertenece a la categoría: Adolescente.")
        
    elif 18 <= edad < 30:
        print("Pertenece a la categoría: Adulto/a joven.")
        
    else: 
        print("Pertenece a la categoría: Adulto/a.")

print("Fin del programa. ¡Gracias por participar de la calculadora de etapas de la vida! 👋")

# %% [markdown]
# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo VerificadorClave
# 
#     Escribir "Verificador de contraseñas de entre 8 y 14 caracteres 🔐"
#     Escribir "Por favor, ingrese una contraseña:"
#     Leer clave
#     
#     // Calculamos el largo de la cadena
#     largo <- Longitud(clave)
#     
#     Si largo >= 8 Y largo <= 14 Entonces
#         Escribir "Ha ingresado una contraseña correcta. ✅"
#     Sino
#         Escribir "Error: La contraseña debe tener entre 8 y 14 caracteres. ❌"
#     FinSi
#     
#     Escribir "Fin del programa. 👋"
# FinAlgoritmo

# %%
print("Verificador de contraseñas (8 a 14 caracteres) 🔐")
clave = input("Por favor, ingrese su nueva clave: ").strip()

# Guardamos el largo en una variable para no calcularlo dos veces
largo = len(clave)

if 8 <= largo <= 14:
    print(f"✅ Contraseña aceptada. (Tiene {largo} caracteres).")
elif largo < 8:
    print(f"❌ Error: La clave es muy corta. Falta(n) {8 - largo} caracteres.")
else:
    print(f"❌ Error: La clave es muy larga. Te pasaste por {largo - 14} caracteres.")

print("Fin del programa. ¡Gracias por usar el verificador de contraseñas! 👋")

# %% [markdown]
# Ejercicio 6: Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:

# %% [markdown]
# Algoritmo VerificadorConsumoElectrico
# 
#     Escribir "Ingrese su consumo mensual en kWh:"
#     Leer entrada
#     
#     Si NO Es_Numerico(entrada) Entonces
#         Escribir "Error: Debe ingresar números, no letras."
#     Sino
#         consumo <- ConvertirANumero(entrada)
#         
#         Si consumo <= 0 Entonces
#             Escribir "Error: El consumo debe ser mayor a cero."
#             
#         Sino Si consumo < 150 Entonces
#             Escribir "Consumo bajo. 🌿"
#             
#         Sino Si consumo >= 150 Y consumo < 300 Entonces
#             Escribir "Consumo medio. 🌎"
#             
#         Sino Si consumo >= 300 Y consumo < 500 Entonces
#             Escribir "Consumo alto. ⚠️"
#             
#         Sino
#             Escribir "Consumo nuclear. 🚨"
#         FinSi
#         
#     FinSi
# 
# FinAlgoritmo

# %%
print("Verificador de consumo responsable de energía eléctrica ⚡")
entrada = input("Por favor, ingrese su consumo mensual (kWh): ").strip()

if not entrada.isdigit():
    print("❌ ¡Epa! El consumo no se mide en letras. Poné un número.")
else:
   
    consumo = int(entrada)
    
    if consumo <= 0:
        print("❌ El consumo no puede ser cero o negativo.")
    
    elif consumo < 150:
        print("🌿 Consumo bajo. ¡Buen trabajo!")
        
    elif 150 <= consumo < 300:
   
        print("🌎 Consumo medio. Podrías reducirlo un poco.")
        
    elif 300 <= consumo < 500:
        print("⚠️ Consumo alto. Considerá ahorrar energía.")
        
    else:
    
        print("🚨 Consumo nuclear. ¡Apagá todo y salí a tomar aire!")

print("Fin del programa. Gracias por usar el verificador de consumo de energía eléctrica! 👋")

# %% [markdown]
# Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla. 

# %% [markdown]
# Algoritmo VerificadorVocales
# 
#     Escribir "Ingrese una palabra o frase:"
#     Leer texto
#     
#     // Validamos que el texto no esté vacío
#     Si Longitud(texto) > 0 Entonces
#         // Extraemos el último carácter
#         ultima <- Subcadena(texto, Longitud(texto), Longitud(texto))
#         
#         // Si es vocal, agregamos el signo
#         Si ultima="a" O ultima="e" O ultima="i" O ultima="o" O ultima="u" Entonces
#             Escribir texto + "!"
#         Sino
#             Escribir texto
#         FinSi
#     Sino
#         Escribir "Error: No se ingresó ninguna palabra."
#     FinSi
#     
# FinAlgoritmo

# %%
print("Verificador de Vocales Finales 🗣️")
texto = input("Por favor, ingrese una palabra o frase: ").strip()

if len(texto) == 0:
    print("⚠️ No ingresaste nada. Por favor, intentá de nuevo.")
else:
 
    ultima_letra = texto[-1].lower()

if ultima_letra in "AEIOUaeiouÁÉÍÓÚáéíóú":
        print(texto + "!")
else:
        print(texto)

print("Fin del programa 👋")

# %% [markdown]
# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee: 

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo ModificadorNombres
# 
#     Escribir "Modificador gramatical de nombres propios 🏷️"
#     Escribir "Por favor, ingrese su nombre:"
#     Leer nombre
#     
#     // 1. Validamos que el nombre no esté vacío
#     Si Longitud(nombre) = 0 Entonces
#         Escribir "⚠️ No ingresaste nada. Por favor, intentá de nuevo."
#     Sino
#         Escribir "Seleccione una opción:"
#         Escribir "1. Mayúscula"
#         Escribir "2. Minúscula"
#         Escribir "3. Formato Nombre Propio"
#         Leer opcion
#         
#         // 2. Procesamos la opción elegida
#         Segun opcion Hacer
#             "1":
#                 Escribir ConvertirAMayusculas(nombre)
#             "2":
#                 Escribir ConvertirAMinusculas(nombre)
#             "3":
#                 Escribir Capitalizar(nombre) // Primera letra en mayúscula
#             De Otro Modo:
#                 Escribir "⚠️ Opción no válida. Ingrese 1, 2 o 3."
#         FinSegun
#         
#     FinSi
#     
#     Escribir "Fin del programa 👋"
# FinAlgoritmo

# %%
print (f"Modificador gramatical de nombres propios 🏷️")
nombre = input("Por favor, ingrese su nombre: ").strip()
if len(nombre) == 0:
    print("⚠️ No ingresaste nada. Por favor, intentá de nuevo.")
else:
    opcion = input("Ingrese el número de la opción que desea:\n1. Mayúscula\n2. Minúscula\n3. Invertir mayúsculas y minúsculas\nOpción: ").strip()
    
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("⚠️ Opción no válida. Por favor, ingrese 1, 2 o 3.")

print("Fin del programa. ¡Gracias por usar el modificador gramatical de nombres propios! 👋")

# %% [markdown]
# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla: 

# %% [markdown]
# Algoritmo ClasificadorSismosOnda
# 
#     Escribir "🌍 Detector de Intensidad de Sismos 📈"
#     Escribir "Ingrese la magnitud del sismo:"
#     Leer entrada
#     
#     Si NO Es_Numerico(entrada) Entonces
#         Escribir "Error: Debe ingresar un número."
#     Sino
#         m <- ConvertirANumero(entrada)
#         
#         Si m < 3 Entonces
#             Escribir "'Apenas se sintió' (😴)"
#         Sino Si m >= 3 Y m < 4 Entonces
#             Escribir "'Leve' (🤔)"
#         Sino Si m >= 4 Y m < 5 Entonces
#             Escribir "'Moderado' (😮)"
#         Sino Si m >= 5 Y m < 6 Entonces
#             Escribir "'Fuerte' (😧)"
#         Sino Si m >= 6 Y m < 7 Entonces
#             Escribir "'Muy Fuerte' (😱)"
#         Sino
#             Escribir "'Extremo' (🚨💥)"
#         FinSi
#         
#     FinSi
#     
#     Escribir "Fin del programa 👋💤"
# FinAlgoritmo

# %%
print("🌍 Detector de Intensidad de Sismos - Escala Richter 📈")

entrada = input("¿De cuánto fue la magnitud?: ").strip()

if not entrada.replace('.', '', 1).isdigit():
    print("❌ ¡Epa! Poné un número válido. 🤓")
else:
    magnitud = float(entrada)
    
    if magnitud < 0:
        print("❌ La magnitud no puede ser negativa.")
    elif magnitud < 3:
        print("Clasificación: 'Apenas se sintió' (¿Fue un camión?) 😴")
    elif 3 <= magnitud < 4:
        print("Clasificación: 'Leve' (Algo se movió...) 🤔")
    elif 4 <= magnitud < 5:
        print("Clasificación: 'Moderado' (¡Se sintió fuerte!) 😮")
    elif 5 <= magnitud < 6:
        print("Clasificación: 'Fuerte' (¡Aferrate a la mesa!) 😧")
    elif 6 <= magnitud < 7:
        print("Clasificación: 'Muy Fuerte' (¡El suelo es lava!) 😱")
    else:
        print("Clasificación: 'Extremo' (¡Salí corriendo ya!) 🚨💥")

print("Fin del programa. ¡Gracias por usar el detector de intensidad de sismos! 👋")

# %% [markdown]
# Ejercicio 10: Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

# %% [markdown]
# Algoritmo DeterminarEstaciones
# 
#     Escribir "Ingrese hemisferio (N/S):"
#     Leer hemi
#     Escribir "Ingrese mes (1-12):"
#     Leer mes_texto
#     Escribir "Ingrese día (1-31):"
#     Leer dia_texto
#     
#     // Verificamos si son números (Validación)
#     Si Es_Numerico(mes_texto) Y Es_Numerico(dia_texto) Entonces
#         mes <- ConvertirANumero(mes_texto)
#         dia <- ConvertirANumero(dia_texto)
#         
#         Si (mes >= 1 Y mes <= 12) Y (dia >= 1 Y dia <= 31) Entonces
#             // Acá va toda la lógica de los Si / Sino Si que armamos antes
#             // (Hemisferio Sur y Norte)
#         Sino
#             Escribir "Error: Fecha fuera de rango."
#         FinSi
#     Sino
#         Escribir "Error: Debe ingresar valores numéricos."
#     FinSi
# FinAlgoritmo

# %%
print("✨ Verificador de Estaciones del Año ✨")

# 1. Pedimos los datos
hemi = input("¿En qué hemisferio estás? (N/S): ").strip().lower()
mes_input = input("Ingresá el mes (1-12): ").strip()
dia_input = input("Ingresá el día (1-31): ").strip()

# 2. Validamos que sean números antes de convertir
if not (mes_input.isdigit() and dia_input.isdigit()):
    print("❌ Error: Por favor, ingresá solo números para el mes y el día. 🤓")
else:
    mes = int(mes_input)
    dia = int(dia_input)

    # 3. Validamos que los números tengan sentido
    if not (1 <= mes <= 12 and 1 <= dia <= 31):
        print("❌ Error: Ese mes o día no existe. Revisá los datos. 🌎")
    else:
        # --- LÓGICA HEMISFERIO SUR ---
        if hemi == "s":
            if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
                print("Estación actual: ¡Verano! ☀️🥵")
            elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
                print("Estación actual: ¡Otoño! 🍂🍁")
            elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
                print("Estación actual: ¡Invierno! ❄️🏔️")
            else:
                print("Estación actual: ¡Primavera! 🌸🌷")

        # --- LÓGICA HEMISFERIO NORTE ---
        elif hemi == "n":
            if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
                print("Estación actual: ¡Invierno! ❄️🧥")
            elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
                print("Estación actual: ¡Primavera! 🌸🦋")
            elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
                print("Estación actual: ¡Verano! ☀️🏖️")
            else:
                print("Estación actual: ¡Otoño! 🍂🍎")
        else:
            print("⚠️ Error: El hemisferio debe ser 'N' o 'S'.")

print("\nFin del programa. ¡Gracias por usar el verificador de estaciones!")


