# %% [markdown]
# Programación 1
# 
# Trabajo Práctico N°3
# 
# Alumno: Lucas Rubén Palazzolo López
# 

# %% [markdown]
# Ejercicio 1: "Caja del kiosco"

# %% [markdown]
# Pseudocódigo: 
# 
# INICIO
# 
# MOSTRAR encabezado del sistema
# 
# // VALIDAR NOMBRE
# REPETIR
#     PEDIR nombre
#     SI nombre está vacío ENTONCES
#         MOSTRAR error
#     SINO SI nombre contiene solo letras ENTONCES
#         GUARDAR nombre formateado
#         MOSTRAR bienvenida
#     SINO
#         MOSTRAR error de formato
# HASTA que el nombre sea válido
# 
# // VALIDAR CANTIDAD DE PRODUCTOS
# REPETIR
#     PEDIR cantidad
#     SI cantidad está vacía ENTONCES
#         MOSTRAR error
#     SINO SI cantidad no es numérica ENTONCES
#         MOSTRAR error
#     SINO
#         CONVERTIR cantidad a entero
#         SI cantidad > 0 ENTONCES
#             CONTINUAR
#         SINO
#             MOSTRAR error
# HASTA que la cantidad sea válida
# 
# INICIALIZAR total_sin_desc = 0
# INICIALIZAR total_con_desc = 0
# INICIALIZAR lista_productos vacía
# 
# MOSTRAR inicio de carga de productos
# 
# // RECORRER PRODUCTOS
# PARA i DESDE 1 HASTA cantidad HACER
# 
#     MOSTRAR número de producto
# 
#     // VALIDAR PRECIO
#     REPETIR
#         PEDIR precio
#         SI precio no es numérico ENTONCES
#             MOSTRAR error
#         SINO
#             CONVERTIR precio a entero
#             SI precio > 0 ENTONCES
#                 CONTINUAR
#             SINO
#                 MOSTRAR error
#     HASTA que el precio sea válido
# 
#     // VALIDAR DESCUENTO
#     REPETIR
#         PEDIR descuento (S/N)
#         CONVERTIR a minúscula
#         SI descuento es "s" o "n" ENTONCES
#             CONTINUAR
#         SINO
#             MOSTRAR error
#     HASTA que el descuento sea válido
# 
#     // CÁLCULOS
#     SUMAR precio a total_sin_desc
# 
#     SI descuento es "s" ENTONCES
#         precio_final = precio * 0.90
#     SINO
#         precio_final = precio
# 
#     SUMAR precio_final a total_con_desc
# 
#     GUARDAR (número, precio, descuento) en lista_productos
# 
#     MOSTRAR detalle del producto cargado
# 
# FIN PARA
# 
# // RESULTADOS FINALES
# ahorro = total_sin_desc - total_con_desc
# promedio = total_con_desc / cantidad
# 
# MOSTRAR cliente
# MOSTRAR cantidad de productos
# 
# PARA cada producto EN lista_productos HACER
#     MOSTRAR detalle del producto
# FIN PARA
# 
# MOSTRAR total sin descuentos
# MOSTRAR total con descuentos (2 decimales)
# MOSTRAR ahorro total
# MOSTRAR promedio por producto (2 decimales)
# 
# MOSTRAR mensaje de cierre
# 
# FIN

# %%
print("===================================================================")
print("   Sistema de Gestión de Ventas - Kiosco de la Esquina 💰")
print("===================================================================\n")


while True:
    nombre_input = input("Por favor, ingrese el nombre del cliente para iniciar la operación: ").strip()

    if nombre_input == "":
        print("Error crítico: El campo de nombre no puede quedar vacío. Por favor ingrese un nombre válido. 🤔")
    elif nombre_input.isalpha():
        nombre_cliente = nombre_input.title()
        print("-" * 50)
        print(f"✅ ¡Validación exitosa! Hola {nombre_cliente}, es un gusto saludarte. 👋")
        print(f"Bienvenido al sistema de caja del kiosco de la esquina, {nombre_cliente}!")
        print("-" * 50)
        break
    else:
        print("Error de formato: El nombre solo puede contener letras (sin números ni símbolos). 🤔")


while True:
    cantidad_str = input(f"Muy bien {nombre_cliente}, ahora por favor dinos: ¿Qué cantidad de productos desea comprar hoy? 🛒 ").strip()

    if cantidad_str == "":
        print("Advertencia: La cantidad de productos no puede estar vacía, por favor ingrese un número válido. 🤔")
    elif not cantidad_str.isdigit():
        print("Error de dato: El sistema detectó que lo ingresado no es un número entero. Por favor, use solo números. ⚠️")
    else:
        cantidad_productos = int(cantidad_str)
        if cantidad_productos > 0:
            print(f"📦 ¡Perfecto! Vamos a procesar un total de {cantidad_productos} productos en esta operación.")
            break
        else:
            print("Cantidad inválida: La cantidad debe ser mayor a 0 para iniciar el proceso de carga. ❌")

total_sin_desc = 0
total_con_desc = 0


productos = []

print("\n--- 📝 Iniciando carga detallada de productos ---")


for i in range(cantidad_productos):
    print(f"\n>>>> 🔄 Procesando ahora: Producto número {i + 1} de {cantidad_productos}...")

    
    while True:
        p_str = input(f"Producto {i + 1} - Precio: ").strip()
        if p_str.isdigit():
            precio = int(p_str)
            if precio > 0:
                break
            else:
                print("Error: El precio debe ser mayor a 0. 💵")
        else:
            print("Error: El precio debe ser un número entero. Por favor, ingrese un monto válido. 💵")

  
    while True:
        desc_input = input(f"Producto {i + 1} - Descuento (S/N): ").strip().lower()
        if desc_input == 's' or desc_input == 'n':
            break
        print("Error: Responda únicamente con 'S' para confirmar el descuento o 'N' para indicar que no posee. 🏷️")

   
    total_sin_desc += precio

    if desc_input == 's':
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_desc += precio_final

  
    productos.append((i+1, precio, desc_input.upper()))

    print("--------------------------------------------------")
    print(f"📦 Producto {i+1} registrado correctamente:")
    print(f"💲 Precio ingresado: ${precio}")
    print(f"🏷️ Descuento aplicado: {desc_input.upper()}")
    print(f"💸 Precio final del producto: ${precio_final:.2f}")
    print("--------------------------------------------------")


ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad_productos


print("\n" + "-" * 35)
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")


for prod in productos:
    print(f"Producto {prod[0]} - Precio: {prod[1]} Descuento (S/N): {prod[2]}")

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("-" * 35)

print("¡Muchas gracias por su compra! Vuelva pronto. 😊")

# %% [markdown]
# Ejercicio 2: “Acceso al Campus y Menú Seguro”

# %% [markdown]
# Pseudocódigo: 
# INICIO
# 
# MOSTRAR encabezado del sistema
# 
# DEFINIR usuario_correcto = "alumno"
# DEFINIR clave_correcta = "python123"
# 
# intentos = 0
# max_intentos = 3
# 
# // LOGIN CON INTENTOS
# MIENTRAS intentos < max_intentos HACER
# 
#     MOSTRAR número de intento
# 
#     PEDIR usuario
#     PEDIR clave
# 
#     SI usuario está vacío O clave está vacía ENTONCES
#         MOSTRAR error de campos vacíos
#         CONTINUAR
#     FIN SI
# 
#     SI usuario es igual a usuario_correcto Y clave es igual a clave_correcta ENTONCES
#         MOSTRAR acceso concedido
#         SALIR DEL BUCLE
#     SINO
#         MOSTRAR error de credenciales
#         intentos = intentos + 1
#     FIN SI
# 
# FIN MIENTRAS
# 
# // BLOQUEO
# SI intentos = max_intentos ENTONCES
#     MOSTRAR "Cuenta bloqueada"
# SINO
# 
#     // MENÚ REPETITIVO
#     MIENTRAS VERDADERO HACER
# 
#         MOSTRAR opciones:
#             1) Estado
#             2) Cambiar clave
#             3) Mensaje
#             4) Salir
# 
#         PEDIR opción
# 
#         SI opción no es numérica ENTONCES
#             MOSTRAR error
#             CONTINUAR
#         FIN SI
# 
#         CONVERTIR opción a entero
# 
#         SI opción < 1 O opción > 4 ENTONCES
#             MOSTRAR error
#             CONTINUAR
#         FIN SI
# 
#         SEGÚN opción HACER
# 
#             CASO 1:
#                 MOSTRAR "Inscripto"
# 
#             CASO 2:
#                 PEDIR nueva_clave
#                 PEDIR confirmación
# 
#                 SI longitud de nueva_clave < 6 ENTONCES
#                     MOSTRAR error
#                 SINO SI nueva_clave ≠ confirmación ENTONCES
#                     MOSTRAR error
#                 SINO
#                     ACTUALIZAR clave_correcta
#                     MOSTRAR confirmación
#                 FIN SI
# 
#             CASO 3:
#                 MOSTRAR mensaje motivacional
# 
#             CASO 4:
#                 MOSTRAR salida
#                 SALIR DEL BUCLE
# 
#         FIN SEGÚN
# 
#     FIN MIENTRAS
# 
# FIN SI
# 
# FIN

# %%
print ("\n===================================================================")
print("   Acceso al menu de la UTN y Menú Seguro para estudiantes 🧑‍💻") 
print("===================================================================\n")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3

# LOGIN CON MÁXIMO 3 INTENTOS
while intentos < max_intentos:
    print(f"\n🔐 Intento {intentos+1}/{max_intentos}")

    # 🔧 FIX: inputs separados y claros
    usuario = input("👤 Usuario: ").strip().lower().capitalize().isalpha()
    clave = input("🔑 Clave: ").strip()

    if usuario == "" or clave == "":
        print("⚠️ Error: El usuario y la clave no pueden estar vacíos.")
        continue

    if usuario == usuario_correcto and clave == clave_correcta:
        print("✅ Acceso concedido.")
        print("🎉 ¡Bienvenido al sistema del campus virtual!")
        break
    else:
        print("❌ Error: credenciales inválidas.")
        print("🔄 Por favor, intente nuevamente.")
        intentos += 1

# BLOQUEO SI FALLA 3 VECES
if intentos == max_intentos:
    print("🚫 Cuenta bloqueada. Contacte con administración.")
else:
    # MENÚ REPETITIVO
    while True:
        print("\n📋 Menú principal")
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        opcion = input("👉 Opción: ").strip()

        # VALIDACIÓN DE OPCIÓN
        if not opcion.isdigit():
            print("⚠️ Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("⚠️ Error: opción fuera de rango.")
            continue

        # OPCIONES DEL MENÚ
        if opcion == 1:
            print("📄 Estado: Inscripto")

        elif opcion == 2:
            print("🔒 Cambio de clave")
            nueva = input("Ingrese nueva clave: ").strip()
            confirmar = input("Confirme la clave: ").strip()

            if len(nueva) < 6:
                print("❌ Error: la clave debe tener mínimo 6 caracteres.")
            elif nueva != confirmar:
                print("❌ Error: las claves no coinciden.")
            else:
                clave_correcta = nueva
                print("✅ Clave actualizada correctamente.")

        elif opcion == 3:
            print("💡 Mensaje motivacional:")
            print("Seguí adelante, el esfuerzo vale la pena.")

        elif opcion == 4:
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

# %% [markdown]
#  Ejercicio 3 (Alta) — “Agenda de Turnos con nombres ("sin listas") 
# 
# 

# %% [markdown]
# Pseudocódigo:
# 
# INICIO
# 
# MOSTRAR encabezado del sistema
# 
# // VALIDAR OPERADOR
# REPETIR
#     PEDIR nombre_operador
#     SI nombre_operador está vacío O no es solo letras ENTONCES
#         MOSTRAR error
#     SINO
#         MOSTRAR bienvenida
# HASTA que sea válido
# 
# // INICIALIZAR TURNOS
# lunes1 = ""
# lunes2 = ""
# lunes3 = ""
# lunes4 = ""
# 
# martes1 = ""
# martes2 = ""
# martes3 = ""
# 
# // MENÚ PRINCIPAL
# MIENTRAS VERDADERO HACER
# 
#     MOSTRAR:
#         1) Reservar turno
#         2) Cancelar turno
#         3) Ver agenda del día
#         4) Ver resumen general
#         5) Cerrar sistema
# 
#     PEDIR opción
# 
#     SI opción está vacía O no es numérica ENTONCES
#         MOSTRAR error
#         CONTINUAR
#     FIN SI
# 
#     CONVERTIR opción a entero
# 
#     SI opción < 1 O opción > 5 ENTONCES
#         MOSTRAR error
#         CONTINUAR
#     FIN SI
# 
#     SEGÚN opción HACER
# 
#         // ---------------- RESERVAR ----------------
#         CASO 1:
# 
#             PEDIR día (1=Lunes, 2=Martes)
# 
#             SI día no es numérico O fuera de rango ENTONCES
#                 MOSTRAR error
#                 CONTINUAR
#             FIN SI
# 
#             PEDIR nombre_paciente
# 
#             SI nombre inválido ENTONCES
#                 MOSTRAR error
#                 CONTINUAR
#             FIN SI
# 
#             SI día = 1 ENTONCES
#                 SI nombre = lunes1 O lunes2 O lunes3 O lunes4 ENTONCES
#                     MOSTRAR "Paciente repetido"
#                 SINO
#                     SI lunes1 está vacío ENTONCES guardar en lunes1
#                     SINO SI lunes2 está vacío ENTONCES guardar en lunes2
#                     SINO SI lunes3 está vacío ENTONCES guardar en lunes3
#                     SINO SI lunes4 está vacío ENTONCES guardar en lunes4
#                     SINO
#                         MOSTRAR "Sin cupos"
#                     FIN SI
#                 FIN SI
#             FIN SI
# 
#             SI día = 2 ENTONCES
#                 SI nombre = martes1 O martes2 O martes3 ENTONCES
#                     MOSTRAR "Paciente repetido"
#                 SINO
#                     SI martes1 vacío ENTONCES guardar en martes1
#                     SINO SI martes2 vacío ENTONCES guardar en martes2
#                     SINO SI martes3 vacío ENTONCES guardar en martes3
#                     SINO
#                         MOSTRAR "Sin cupos"
#                     FIN SI
#                 FIN SI
#             FIN SI
# 
#         // ---------------- CANCELAR ----------------
#         CASO 2:
# 
#             PEDIR día
#             PEDIR nombre_paciente
# 
#             encontrado = FALSO
# 
#             SI día = 1 ENTONCES
#                 SI nombre = lunes1 ENTONCES lunes1 = "" y encontrado = VERDADERO
#                 SINO SI nombre = lunes2 ENTONCES lunes2 = "" y encontrado = VERDADERO
#                 SINO SI nombre = lunes3 ENTONCES lunes3 = "" y encontrado = VERDADERO
#                 SINO SI nombre = lunes4 ENTONCES lunes4 = "" y encontrado = VERDADERO
#             FIN SI
# 
#             SI día = 2 ENTONCES
#                 SI nombre = martes1 ENTONCES martes1 = "" y encontrado = VERDADERO
#                 SINO SI nombre = martes2 ENTONCES martes2 = "" y encontrado = VERDADERO
#                 SINO SI nombre = martes3 ENTONCES martes3 = "" y encontrado = VERDADERO
#             FIN SI
# 
#             SI encontrado = VERDADERO ENTONCES
#                 MOSTRAR "Turno cancelado"
#             SINO
#                 MOSTRAR "No encontrado"
#             FIN SI
# 
#         // ---------------- VER AGENDA ----------------
#         CASO 3:
# 
#             PEDIR día
# 
#             SI día = 1 ENTONCES
#                 MOSTRAR Turno 1: lunes1 o "(libre)"
#                 MOSTRAR Turno 2: lunes2 o "(libre)"
#                 MOSTRAR Turno 3: lunes3 o "(libre)"
#                 MOSTRAR Turno 4: lunes4 o "(libre)"
#             SINO SI día = 2 ENTONCES
#                 MOSTRAR Turno 1: martes1 o "(libre)"
#                 MOSTRAR Turno 2: martes2 o "(libre)"
#                 MOSTRAR Turno 3: martes3 o "(libre)"
#             FIN SI
# 
#         // ---------------- RESUMEN ----------------
#         CASO 4:
# 
#             ocupados_lunes = 0
#             ocupados_martes = 0
# 
#             SI lunes1 ≠ "" ENTONCES sumar 1
#             SI lunes2 ≠ "" ENTONCES sumar 1
#             SI lunes3 ≠ "" ENTONCES sumar 1
#             SI lunes4 ≠ "" ENTONCES sumar 1
# 
#             SI martes1 ≠ "" ENTONCES sumar 1
#             SI martes2 ≠ "" ENTONCES sumar 1
#             SI martes3 ≠ "" ENTONCES sumar 1
# 
#             MOSTRAR ocupados y libres por día
# 
#             SI lunes > martes ENTONCES mostrar "Lunes"
#             SINO SI martes > lunes ENTONCES mostrar "Martes"
#             SINO
#                 MOSTRAR "Empate"
#             FIN SI
# 
#         // ---------------- SALIR ----------------
#         CASO 5:
#             MOSTRAR cierre
#             SALIR DEL BUCLE
# 
#     FIN SEGÚN
# 
# FIN MIENTRAS
# 
# FIN

# %%
print("====================================================")
print("   📅 Sistema de Agenda de Turnos - Atención Médica")
print("====================================================\n")

# 🔹 VALIDAR OPERADOR
while True:
    operador = input("👤Por favor, ingrese su nombre:").strip ()
    if operador == "" or not operador.isalpha():
        print("❌ Error: Ingrese solo letras, sin espacios ni números.")
    else:
        print(f"✅ Bienvenido/a {operador}! Sistema listo para operar 🚀")
        print("💡 Consejo: Use el menú para gestionar turnos fácilmente.")
        break

# 🔹 TURNOS
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# 🔹 MENÚ PRINCIPAL
while True:
    print("\n📋 Menú Principal")
    print("1) 📝 Reservar turno")
    print("2) ❌ Cancelar turno")
    print("3) 📅 Ver agenda del día")
    print("4) 📊 Ver resumen general")
    print("5) 🚪 Cerrar sistema")

    opcion = input("👉 Seleccione una opción: ").strip()

    if opcion == "":
        print("⚠️ Error: No puede dejar la opción vacía.")
        continue

    if not opcion.isdigit():
        print("⚠️ Error: Debe ingresar un número válido (1-5).")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("⚠️ Error: Opción fuera de rango. Intente nuevamente.")
        continue

    # ================= RESERVAR =================
    if opcion == 1:
        print("\n📝 Reserva de turno")

        dia = input("📅 Día (1=Lunes, 2=Martes): ").strip()

        if dia == "":
            print("⚠️ Error: Debe ingresar un día.")
            continue

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("❌ Error: Día inválido. Solo 1 o 2.")
            continue

        dia = int(dia)

        nombre = input("👤 Nombre del paciente: ").strip()

        if nombre == "" or not nombre.isalpha():
            print("❌ Error: Nombre inválido. Solo letras.")
            continue

        nombre = nombre.title()

        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("⚠️ Este paciente ya tiene un turno en Lunes.")
            elif lunes1 == "":
                lunes1 = nombre
                print("✅ Turno asignado en Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = nombre
                print("✅ Turno asignado en Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = nombre
                print("✅ Turno asignado en Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = nombre
                print("✅ Turno asignado en Lunes (Turno 4).")
            else:
                print("🚫 No hay cupos disponibles en Lunes.")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("⚠️ Este paciente ya tiene un turno en Martes.")
            elif martes1 == "":
                martes1 = nombre
                print("✅ Turno asignado en Martes (Turno 1).")
            elif martes2 == "":
                martes2 = nombre
                print("✅ Turno asignado en Martes (Turno 2).")
            elif martes3 == "":
                martes3 = nombre
                print("✅ Turno asignado en Martes (Turno 3).")
            else:
                print("🚫 No hay cupos disponibles en Martes.")

    # ================= CANCELAR =================
    elif opcion == 2:
        print("\n❌ Cancelación de turno")

        dia = input("📅 Día (1=Lunes, 2=Martes): ").strip()

        if dia == "":
            print("⚠️ Error: Debe ingresar un día.")
            continue

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("❌ Error: Día inválido.")
            continue

        dia = int(dia)

        nombre = input("👤 Nombre del paciente: ").strip()

        if nombre == "" or not nombre.isalpha():
            print("❌ Error: Nombre inválido.")
            continue

        nombre = nombre.title()

        encontrado = False

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("✅ Turno cancelado correctamente.")
        else:
            print("⚠️ No se encontró ese paciente en ese día.")

    # ================= VER AGENDA =================
    elif opcion == 3:
        print("\n📅 Consulta de agenda")

        dia = input("📌 Día (1=Lunes, 2=Martes): ").strip()

        if dia == "":
            print("⚠️ Error: Debe ingresar un día.")
            continue

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("❌ Error: Día inválido.")
            continue

        dia = int(dia)

        if dia == 1:
            print("\n📅 Agenda Lunes")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\n📅 Agenda Martes")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # ================= RESUMEN =================
    elif opcion == 4:
        print("\n📊 Resumen general del sistema")

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print(f"📅 Lunes: {ocupados_lunes} ocupados | {4 - ocupados_lunes} libres")
        print(f"📅 Martes: {ocupados_martes} ocupados | {3 - ocupados_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("🏆 Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("🏆 Día con más turnos: Martes")
        else:
            print("🤝 Empate entre ambos días")

    # ================= SALIR =================
    elif opcion == 5:
        print("\n👋 Cerrando sistema... ¡Gracias por usar la agenda!")
        print(f"🙌 Hasta luego {operador}, ¡buen trabajo hoy!")
        break

# %% [markdown]
# Ejercicio 4: “Escape Room: La Bóveda”

# %% [markdown]
# INICIO
# 
# MOSTRAR encabezado
# 
# // VARIABLES INICIALES
# energia = 100
# tiempo = 12
# cerraduras_abiertas = 0
# alarma = FALSO
# codigo_parcial = ""
# racha_forzar = 0
# 
# // VALIDAR NOMBRE
# REPETIR
#     PEDIR nombre_agente
#     SI está vacío O no es solo letras ENTONCES
#         MOSTRAR error
#     SINO
#         MOSTRAR bienvenida
# HASTA que sea válido
# 
# // BUCLE PRINCIPAL
# MIENTRAS energia > 0 Y tiempo > 0 Y cerraduras_abiertas < 3 HACER
# 
#     // BLOQUEO POR ALARMA
#     SI alarma = VERDADERO Y tiempo <= 3 Y cerraduras_abiertas < 3 ENTONCES
#         MOSTRAR "Sistema bloqueado"
#         SALIR DEL BUCLE
#     FIN SI
# 
#     MOSTRAR estado:
#         energia, tiempo, cerraduras_abiertas, alarma
# 
#     MOSTRAR menú:
#         1) Forzar cerradura
#         2) Hackear panel
#         3) Descansar
# 
#     PEDIR opción
# 
#     SI opción no es numérica ENTONCES
#         MOSTRAR error
#         CONTINUAR
#     FIN SI
# 
#     CONVERTIR opción a entero
# 
#     SI opción fuera de rango ENTONCES
#         MOSTRAR error
#         CONTINUAR
#     FIN SI
# 
#     SEGÚN opción HACER
# 
#         // ---------------- FORZAR ----------------
#         CASO 1:
# 
#             RESTAR 20 a energia
#             RESTAR 2 a tiempo
#             racha_forzar = racha_forzar + 1
# 
#             SI racha_forzar = 3 ENTONCES
#                 MOSTRAR "Alarma activada por abuso"
#                 alarma = VERDADERO
# 
#             SINO
# 
#                 SI energia < 40 ENTONCES
#                     PEDIR número entre 1 y 3
# 
#                     VALIDAR número
# 
#                     SI número = 3 ENTONCES
#                         alarma = VERDADERO
#                     FIN SI
#                 FIN SI
# 
#                 SI alarma = FALSO ENTONCES
#                     cerraduras_abiertas = cerraduras_abiertas + 1
#                     MOSTRAR "Cerradura abierta"
#                 SINO
#                     MOSTRAR "No se pudo abrir"
#                 FIN SI
# 
#             FIN SI
# 
#         // ---------------- HACKEAR ----------------
#         CASO 2:
# 
#             RESTAR 10 a energia
#             RESTAR 3 a tiempo
#             racha_forzar = 0
# 
#             PARA i DESDE 1 HASTA 4 HACER
#                 MOSTRAR progreso
#                 codigo_parcial = codigo_parcial + "A"
#             FIN PARA
# 
#             SI longitud(codigo_parcial) >= 8 Y cerraduras_abiertas < 3 ENTONCES
#                 cerraduras_abiertas = cerraduras_abiertas + 1
#                 MOSTRAR "Cerradura abierta automáticamente"
#             FIN SI
# 
#         // ---------------- DESCANSAR ----------------
#         CASO 3:
# 
#             SUMAR 15 a energia
#             SI energia > 100 ENTONCES
#                 energia = 100
#             FIN SI
# 
#             RESTAR 1 a tiempo
#             racha_forzar = 0
# 
#             SI alarma = VERDADERO ENTONCES
#                 RESTAR 10 a energia
#             FIN SI
# 
#             MOSTRAR "Energía recuperada"
# 
#     FIN SEGÚN
# 
# FIN MIENTRAS
# 
# // RESULTADO FINAL
# SI cerraduras_abiertas = 3 ENTONCES
#     MOSTRAR "VICTORIA"
# SINO SI energia <= 0 O tiempo <= 0 ENTONCES
#     MOSTRAR "DERROTA"
# SINO SI alarma = VERDADERO Y tiempo <= 3 ENTONCES
#     MOSTRAR "DERROTA POR BLOQUEO"
# SINO
#     MOSTRAR "Misión fallida"
# FIN SI
# 
# FIN

# %%
print("====================================================")
print("   🏦 ESCAPE ROOM: LA BÓVEDA")
print("====================================================\n")

# 🔹 VARIABLES
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

# 🔹 NOMBRE
while True:
    agente = input("🕵️ Por favor, ingrese su nombre de agente: ").strip()
    if agente == "" or not agente.isalpha():
        print("❌ Error: solo letras, sin espacios ni números.")
    else:
        print(f"✅ Bienvenido agente {agente}.")
        break

# 🔹 JUEGO
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # 🔒 BLOQUEO
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n🚨 SISTEMA BLOQUEADO POR ALARMA")
        break

    print("\n===================================")
    print(f"⚡ Energía: {energia}")
    print(f"⏳ Tiempo: {tiempo}")
    print(f"🔓 Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"🚨 Alarma: {'ACTIVA' if alarma else 'INACTIVA'}")
    print("===================================")

    print("\n1) 🔧 Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) 💻 Hackear panel (-10 energía, -3 tiempo)")
    print("3) 🛌 Descansar (+15 energía, -1 tiempo)")

    opcion = input("👉 Seleccione una opción: ").strip()

    if not opcion.isdigit():
        print("⚠️ Error: ingrese un número válido (1-3).")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("⚠️ Error: opción fuera de rango.")
        continue

    # ================= FORZAR =================
    if opcion == 1:
        print("\n🔧 Intentando forzar cerradura...")

        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # 🔥 ANTI-SPAM
        if racha_forzar == 3:
            print("🚨 ¡Forzaste 3 veces seguidas!")
            print("🔒 La cerradura se trabó.")
            print("🚨 Alarma activada automáticamente.")
            alarma = True

        else:
            # ⚠️ RIESGO
            if energia < 40:
                print("⚠️ Energía baja: riesgo de alarma.")

                while True:
                    riesgo = input("🎲 Elija un número (1-3): ").strip()
                    if not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
                        print("❌ Error: número inválido.")
                    else:
                        riesgo = int(riesgo)
                        break

                if riesgo == 3:
                    print("🚨 ¡Se activó la alarma!")
                    alarma = True

            # 🔓 ABRIR SOLO SI NO HAY ALARMA
            if not alarma:
                cerraduras_abiertas += 1
                print("✅ Cerradura abierta.")
            else:
                print("⚠️ No se pudo abrir por la alarma.")

    # ================= HACKEAR =================
    elif opcion == 2:
        print("\n💻 Iniciando hackeo...")

        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        for i in range(1, 5):
            print(f"🔄 Paso {i}/4...")
            codigo_parcial += "A"

        print(f"🔐 Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("✅ Hackeo exitoso: cerradura abierta.")

    # ================= DESCANSAR =================
    elif opcion == 3:
        print("\n🛌 Descansando...")

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10
            print("🚨 La alarma consume energía adicional.")

        print("💪 Energía recuperada.")

# 🔹 RESULTADO
print("\n===================================")

if cerraduras_abiertas == 3:
    print("🏆 VICTORIA: Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA: Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("🚫 DERROTA: Sistema bloqueado por alarma.")
else:
    print("❌ Misión fallida.")

# %% [markdown]
# Ejercicio 5: “Escape Room:"La Arena del Gladiador"
# 

# %% [markdown]
# INICIO
# 
# MOSTRAR "BIENVENIDO A LA ARENA"
# 
# // VALIDAR NOMBRE
# REPETIR
#     PEDIR nombre
#     SI nombre está vacío O no es solo letras ENTONCES
#         MOSTRAR "Error: Solo se permiten letras"
#     SINO
#         MOSTRAR bienvenida
# HASTA que sea válido
# 
# // VARIABLES INICIALES
# vida_jugador = 100
# vida_enemigo = 100
# pociones = 3
# danio_pesado = 15
# danio_enemigo = 12
# juego_activo = VERDADERO
# 
# MOSTRAR "INICIO DEL COMBATE"
# 
# // CICLO PRINCIPAL
# MIENTRAS juego_activo HACER
# 
#     MOSTRAR vida_jugador, vida_enemigo, pociones
# 
#     MOSTRAR menú:
#         1) Ataque Pesado
#         2) Ráfaga Veloz
#         3) Curar
# 
#     // VALIDAR OPCIÓN
#     REPETIR
#         PEDIR opción
#         SI opción no es numérica ENTONCES
#             MOSTRAR error
#         SINO SI opción < 1 O opción > 3 ENTONCES
#             MOSTRAR error
#         SINO
#             opción válida
#     HASTA que sea válida
# 
#     // ACCIONES
#     SEGÚN opción HACER
# 
#         CASO 1: ATAQUE PESADO
#             SI vida_enemigo < 20 ENTONCES
#                 danio = danio_pesado * 1.5
#                 MOSTRAR "Golpe crítico"
#             SINO
#                 danio = danio_pesado
#             FIN SI
# 
#             RESTAR danio a vida_enemigo
#             MOSTRAR daño realizado
# 
#         CASO 2: RÁFAGA VELOZ
#             MOSTRAR "Inicia ráfaga"
#             PARA i DESDE 1 HASTA 3 HACER
#                 RESTAR 5 a vida_enemigo
#                 MOSTRAR "Golpe de 5 daño"
#             FIN PARA
# 
#         CASO 3: CURAR
#             SI pociones > 0 ENTONCES
#                 SUMAR 30 a vida_jugador
#                 SI vida_jugador > 100 ENTONCES
#                     vida_jugador = 100
#                 FIN SI
#                 RESTAR 1 poción
#                 MOSTRAR "Curación realizada"
#             SINO
#                 MOSTRAR "No quedan pociones"
#             FIN SI
# 
#     FIN SEGÚN
# 
#     // TURNO DEL ENEMIGO
#     SI vida_enemigo > 0 ENTONCES
#         RESTAR 12 a vida_jugador
#         MOSTRAR "El enemigo atacó"
#     FIN SI
# 
#     // CONTROL DE FIN
#     SI vida_jugador <= 0 O vida_enemigo <= 0 ENTONCES
#         juego_activo = FALSO
#     FIN SI
# 
# FIN MIENTRAS
# 
# // RESULTADO FINAL
# SI vida_jugador > 0 ENTONCES
#     MOSTRAR "VICTORIA"
# SINO
#     MOSTRAR "DERROTA"
# FIN SI
# 
# FIN

# %%
print("===================================")
print("   🏟️ BIENVENIDO A LA ARENA")
print("===================================\n")

# 🔹 VALIDACIÓN NOMBRE
while True:
    nombre = input("🧑‍🦱 Por favor, ingrese el nombre del Gladiador: ").strip()
    if nombre == "" or not nombre.isalpha():
        print("❌ Error: Solo se permiten letras.")
    else:
        print(f"✅ Bienvenido {nombre}, prepárate para la batalla.")
        break

# 🔹 VARIABLES INICIALES
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
juego_activo = True   # boolean usado correctamente

print("\n⚔️ === INICIO DEL COMBATE === ⚔️")

# 🔹 CICLO PRINCIPAL
while juego_activo:

    print("\n===================================")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("===================================")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # 🔹 VALIDACIÓN MENÚ
    while True:
        opcion = input("👉 Opción: ").strip()
        if not opcion.isdigit():
            print("❌ Error: Ingrese un número válido.")
        else:
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                print("❌ Error: opción fuera de rango.")
            else:
                break

    # ================= ATAQUE PESADO =================
    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_pesado * 1.5   # float real
            print("🔥 ¡Golpe crítico!")
        else:
            danio = float(danio_pesado)

        vida_enemigo -= danio
        print(f"💥 ¡Atacaste al enemigo por {danio:.2f} puntos de daño!")

    # ================= RÁFAGA VELOZ =================
    elif opcion == 2:
        print("⚡ ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # ================= CURAR =================
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print("🧪 Te curaste 30 puntos de vida.")
        else:
            print("⚠️ ¡No quedan pociones! Pierdes el turno.")

    # 🔹 TURNO DEL ENEMIGO
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"👹 ¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    # 🔹 CONTROL FIN DEL JUEGO
    if vida_jugador <= 0 or vida_enemigo <= 0:
        juego_activo = False

# 🔹 RESULTADO FINAL
print("\n===================================")

if vida_jugador > 0:
    print(f"🏆 ¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("💀 DERROTA. Has caído en combate.")


