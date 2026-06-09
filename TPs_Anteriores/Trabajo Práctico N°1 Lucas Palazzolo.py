# %% [markdown]
# Programación 1
# 
# Trabajo Práctico N°1 
# 
# Tema: Estructuras secuenciales
# 
# Alumno: Lucas Rubén Palazzolo López
# 

# %% [markdown]
# Ejercicio N°1:  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
# 

# %% [markdown]
# Pseudocódigo:
# 
# Algoritmo HolaMundo
# 
#     Escribir "¡Hola Mundo!"
#     
# FinAlgoritmo

# %%
print ("¡Hola Mundo!👋🌎")

# %% [markdown]
# Ejercicio N°2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. 

# %% [markdown]
# Pseudocódigo:
# 
# Algoritmo SaludoNombre
# 
#     Escribir "Ingrese su nombre:"
#     Leer nombre
#     Escribir "¡Hola ", nombre, "!"
#     
# FinAlgoritmo

# %%
nombre = input ("Por favor, ingrese su nombre: ").strip().capitalize()
print (f"Hola, {nombre}!")

# %% [markdown]
# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. 

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo PresentacionDatos
# 
#     Escribir "Ingrese nombre:"
#     Leer nombre
#     Escribir "Ingrese apellido:"
#     Leer apellido
#     Escribir "Ingrese edad:"
#     Leer edad
#     Escribir "Ingrese lugar de residencia:"
#     Leer residencia
#     Escribir "Soy ", nombre, " ", apellido, ", tengo ", edad, " años y vivo en ", residencia
# 
# FinAlgoritmo

# %%
nombre = input ("Por favor, ingrese su nombre: ").strip().capitalize().title ()
apellido = input ("Por favor, ingrese su apellido: ").strip().capitalize().title ()
edad = int(input ("Por favor, ingrese su edad: ").strip())
residencia = input ("Por favor, ingrese su lugar de residencia: ").strip().capitalize().title ()
print (f"Hola, {nombre} {apellido}. Usted tiene {edad} años y vive en {residencia}.")

# %% [markdown]
# Ejercicio N°4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo Circulo
# 
#     Escribir "Ingrese el radio:"
#     Leer r
#     area <- 3.14159 * r * r
#     perimetro <- 2 * 3.14159 * r
#     Escribir "Área: ", area
#     Escribir "Perímetro: ", perimetro
#     
# FinAlgoritmo

# %%
import math

print (f"Calculadora de área y perímetro de un círculo 🔵")
radio = float(input ("Por favor, ingrese el radio del círculo: ").strip())  
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio 

print (f"El área del círculo es: {area:.2f} y el perímetro del círculo es: {perimetro:.2f}")     
print (f"Fin de programa ¡Gracias por usar la calculadora de círculos!👋🔵")

# %% [markdown]
#  Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivalen.
# 

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo Circulo
# 
#     Escribir "Ingrese el radio:"
#     Leer radio
#     area <- 3.14159 * radio * radio
#     perimetro <- 2 * 3.14159 * radio
#     Escribir "Área: ", area
#     Escribir "Perímetro: ", perimetro
#     
# FinAlgoritmo

# %%
print ("Convertidor de segundos a horas ⏱️")
segundos = int(input ("Por favor, ingrese una cantidad de segundos: ").strip())
horas = segundos / 3600
segundos_restantes = segundos % 3600 
minutos = segundos_restantes // 60      
segundos_finales = segundos_restantes % 60 
print (f"{segundos} segundos equivalen a {horas:.2f} horas  ⏱️")
print (f"{segundos} segundos equivalen a {horas:.0f} horas, {minutos:.0f} minutos y {segundos_finales:.0f} segundos ⏱️")
print (f"Fin de programa ¡Gracias por usar el convertidor de segundos a horas!👋⏱️")

# %% [markdown]
# Ejercicio 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

# %% [markdown]
# Pseudocódigo:
# 
# Algoritmo TablaMultiplicar
# 
#     Escribir "Ingrese número:"
#     Leer número
#     Para i <- 0 Hasta 10 Hacer
#         Escribir número, " x ", i, " = ", número x i
# 
#     FinPara
# FinAlgoritmo

# %%
print (f"Calculadora de numeros enteros a tabla de multiplicar ✖️")
numero_a_multiplicar = int(input ("Por favor, ingrese un número entero para mostrar su tabla de multiplicar: ").strip())
print (f"{numero_a_multiplicar} x 0 = {numero_a_multiplicar * 0}")
print (f"{numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}")
print (f"{numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}")
print (f"{numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3}")
print (f"{numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}")
print (f"{numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}")
print (f"{numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}")
print (f"{numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}")
print (f"{numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}")
print (f"{numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}")
print (f"{numero_a_multiplicar} x 10 = {numero_a_multiplicar * 10}")
print (f"Tabla de multiplicar del número {numero_a_multiplicar} ✖️")

# %% [markdown]
# Ejercicio N°7:  Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# %% [markdown]
# Pseudocódigo
# 
# Algoritmo Operaciones
# 
#     Escribir "Ingrese primer número (no 0):"
#     Leer n1
#     Escribir "Ingrese segundo número (no 0):"
#     Leer n2
#     Escribir "Suma: ", n1 + n2
#     Escribir "Resta: ", n1 - n2
#     Escribir "Multiplicación: ", n1 * n2
#     Escribir "División: ", n1 / n2
#     
# FinAlgoritmo

# %%
# ENTRADA DE DATOS: Se solicita al usuario ingresar dos números enteros distintos de 0.
print ("Calculadora de operaciones básicas entre dos números enteros distintos de 0 ➕➖✖️➗")
numero1 = int(input ("Por favor, ingrese el primer número entero distinto de 0: ").strip())
numero2 = int(input ("Por favor, ingrese el segundo número entero distinto de 0: ").strip())

# PROCESO DE DATOS: Se realizan las operaciones de suma, resta, multiplicación y división entre los dos números ingresados por el usuario.
suma = numero1 + numero2
resta = numero1 - numero2   
multiplicación = numero1 * numero2
división = round(numero1 / numero2, 2)

# SALIDA DE DATOS: Se muestra por pantalla el resultado de las operaciones realizadas entre los dos números ingresados por el usuario.
print (f"La suma de {numero1} y {numero2} es: {suma}")
print (f"La resta de {numero1} y {numero2} es: {resta}")        
print (f"La multiplicación de {numero1} y {numero2} es: {multiplicación}")  
print (f"La división de {numero1} y {numero2} es: {división:.2f}")
print (f"Fin de programa ¡Gracias por usar la calculadora de operaciones básicas entre dos números enteros distintos de 0!👋➕➖✖️➗")

# %% [markdown]
# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 

# %% [markdown]
# Algoritmo CalcularIMC
# 
#     Escribir "Ingrese peso (kg):"
#     Leer p
#     Escribir "Ingrese altura (m):"
#     Leer a
#     imc <- p / (a * a)
#     Escribir "Su IMC es: ", imc
#     
# FinAlgoritmo

# %%
#ENTRADA DE DATOS: Se solicita al usuario ingresar su peso en kilogramos y su altura en metros.
print (f"Calculadora de índice de masa corporal (IMC) ⚖️")
peso = float(input ("Por favor, ingrese su peso en kilogramos: ").strip())
altura = float(input ("Por favor, ingrese su altura en metros: ").strip())

#PROCESO DE DATOS: Se calcula el índice de masa corporal (IMC) utilizando la fórmula: IMC = peso / altura^2.
imc = round(peso / altura ** 2, 2)


#SALIDA DE DATOS: Se muestra por pantalla el resultado del cálculo del índice de masa corporal (IMC) con dos decimales.
print (f"Su índice de masa corporal (IMC) es: {imc:.2f} ⚖️")
print (f"Fin de programa ¡Gracias por usar la calculadora de índice de masa corporal (IMC)!👋⚖️")

# %% [markdown]
# Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# 

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo ConversionTemp
# 
#     Escribir "Ingrese grados Celsius:"
#     Leer c
#     f <- (c * 9/5) + 32
#     Escribir "Fahrenheit: ", f
#     
# FinAlgoritmo

# %%
print (f"Calculadora de conversión de grados Celsius a grados Fahrenheit 🌡️")

#ENTRADA DE DATOS: Se solicita al usuario ingresar una temperatura en grados Celsius.
celsius = float(input ("Por favor, ingrese una temperatura en grados Celsius: ").strip())

#PROCESO DE DATOS: Se calcula el equivalente de la temperatura ingresada en grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
fahrenheit = round((celsius * 9/5) + 32, 2)

#SALIDA DE DATOS: Se muestra por pantalla el resultado de la conversión de grados Celsius a grados Fahrenheit con dos decimales.
print (f"{celsius}°C grados Celsius equivalen a {fahrenheit:.2f}°F grados Fahrenheit 🌡️")
print (f"Fin de programa ¡Gracias por usar la calculadora de conversión de grados Celsius a grados Fahrenheit!👋🌡️  ")

# %% [markdown]
# Ejercicio 10:  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

# %% [markdown]
# Pseudocódigo: 
# 
# Algoritmo Promedio
# 
#     Escribir "Número 1:"
#     Leer a
#     Escribir "Número 2:"
#     Leer b
#     Escribir "Número 3:"
#     Leer c
#     prom <- (a + b + c) / 3
#     Escribir "El promedio es: ", promedio
# 
# FinAlgoritmo

# %%
print ("Calculadora de promedio de tres números 📊")

#ENTRADA DE DATOS: Se solicita al usuario ingresar tres números.
numero1 = float(input ("Por favor, ingrese el primer número: ").strip())
numero2 = float(input ("Por favor, ingrese el segundo número: ").strip())   
numero3 = float(input ("Por favor, ingrese el tercer número: ").strip()) 

#PROCESO DE DATOS: Se calcula el promedio de los tres números ingresados por el usuario utilizando la fórmula: Promedio = (Número1 + Número2 + Número3) / 3.
suma = numero1 + numero2 + numero3
promedio = round(suma / 3, 2)

#SALIDA DE DATOS: Se muestra por pantalla el resultado del promedio con dos decimales.
print (f"El promedio de {numero1}, {numero2} y {numero3} es: {promedio:.2f}")    
print (f"Fin de programa ¡Gracias por usar la calculadora de promedio de tres números!👋📊")


