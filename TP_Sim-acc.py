"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:
El proyecto consiste en crear un simulador donde los usuarios pueden comprar y vender acciones de 
diferentes empresas en un mercado simulado. Los precios de las acciones fluctuarán diariamente según una 
lógica de mercado sencilla o al azar.
Los usuarios podrán ver su portafolio, las ganancias o pérdidas, y el estado actual del mercado.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS

#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# LISTAS

#----------------------------------------------------------------------------------------------

empresas=["Apple", "Google", "Amazon", "Microsoft"]
precios=[150.00, 580.00, 440.00, 299.00]

#----------------------------------------------------------------------------------------------
# FUNCIONES

#----------------------------------------------------------------------------------------------
#OPCION 1
#----------------------------------------------------------------------------------------------
# Función para mostrar las empresas actuales en el mercado
def mostrar_empresas():
    print("\nEmpresas en el mercado:")
    for i in range(len(empresas)):
        print(f"{i+1}. {empresas[i]} - Precio de la acción: ${precios[i]:.2f}")

# Función para agregar una nueva empresa al mercado
def agregar_empresa():
    nombre = input("\nIngrese el nombre de la nueva empresa: ")
    precio_inicial = float(input("Ingrese el precio inicial de la acción: "))
    empresas.append(nombre.capitalize())
    precios.append(precio_inicial)
    print(f"Empresa '{nombre}' agregada con un precio inicial de ${precio_inicial:.2f}")

def menu_gestion_empresas():
    opcion = ""
    while opcion != "3":
        print("\n--- Menú de Gestión de Empresas ---")
        print("1. Mostrar empresas en el mercado")
        print("2. Agregar nueva empresa")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_empresas()
        elif opcion == "2":
            agregar_empresa()
        elif opcion == "3":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente de nuevo.")
#----------------------------------------------------------------------------------------------
#OPCION 2 
#----------------------------------------------------------------------------------------------

def comprar_accion(empresas, precios, saldo_usuario, portafolio):
    mostrar_empresas()
    seleccion = int(input("Seleccione la empresa para comprar acciones (número): ")) - 1
    
    if 0 <= seleccion < len(empresas):
        cantidad = int(input(f"Ingrese la cantidad de acciones de {empresas[seleccion]} a comprar: "))
        costo_total = cantidad * precios[seleccion]
        
        if saldo_usuario >= costo_total:
            saldo_usuario -= costo_total
            portafolio.append([empresas[seleccion], cantidad, precios[seleccion]])
            print(f"Has comprado {cantidad} acciones de {empresas[seleccion]} a ${precios[seleccion]:.2f} cada una.")
            print(f"Saldo restante: ${saldo_usuario:.2f}")
        else:
            print("Fondos insuficientes para realizar la compra.")
    else:
        print("Selección inválida.")
    
    return saldo_usuario, portafolio

def vender_accion(empresas, precios, saldo_usuario, portafolio):
    if not portafolio:
        print("No tienes acciones en tu portafolio para vender.")
        return saldo_usuario, portafolio

    print("\nPortafolio actual:")
    for i, accion in enumerate(portafolio):
        print(f"{i+1}. {accion[0]} - {accion[1]} acciones a un precio de compra de ${accion[2]:.2f}")

    seleccion = int(input("Seleccione la acción que desea vender (número): ")) - 1

    if 0 <= seleccion < len(portafolio):
        empresa, cantidad, precio_compra = portafolio.pop(seleccion)
        precio_actual = precios[empresas.index(empresa)]
        ganancia_perdida = (precio_actual - precio_compra) * cantidad
        saldo_usuario += precio_actual * cantidad
        print(f"Has vendido {cantidad} acciones de {empresa} a ${precio_actual:.2f} cada una.")
        print(f"Ganancia/Pérdida de la transacción: ${ganancia_perdida:.2f}")
        print(f"Saldo actual: ${saldo_usuario:.2f}")
    else:
        print("Selección inválida.")
    
    return saldo_usuario, portafolio

def menu_gestion_compra ():
    op = ""
    while op != "3":
        print("\n--- Menú de Compra y venta de aciones ---")
        print("1. Comprar acciones")
        print("2. Vender acciones")
        print("3. Volver al menú principal")
        op = input("Seleccione una opción: ")
        if op == "1":
            comprar_accion(empresas, precios, saldo_usuario, portafolio)
        elif op == "2":
            vender_accion(empresas, precios, saldo_usuario, portafolio)
        elif op == "3":
            print("Volviendo al menú principal...")
        else:
            print("Opción no válida. Intente de nuevo.")
#----------------------------------------------------------------------------------------------
#OPCION 3 
#----------------------------------------------------------------------------------------------

def simular_dia(empresas, precios):
    # Primera confirmación
    confirmacion1 = input("¿Desea avanzar un día en el mercado? (s/n): ").lower()
    if confirmacion1 != 's':
        print("Operación cancelada. Volviendo al menú principal...")
        return precios
    
    # Segunda confirmación
    confirmacion2 = input("¿Desea avanzar un día en el mercado? (s/n): ").lower()
    if confirmacion2 != 's':
        print("Operación cancelada. Volviendo al menú principal...")
        return precios
    
    print("\nSimulando un día de mercado...")
    
    # Fluctuación de precios
    cambios_dia = []
    for i in range(len(precios)):
        cambio = random.uniform(-0.05, 0.05)  # Cambios de -5% a +5% (random.uniform da valores decimales)
        nuevo_precio = precios[i] * (1 + cambio)
        cambios_dia.append((empresas[i], precios[i], nuevo_precio))
        precios[i] = nuevo_precio
     # Resumen del día
    print("\nResumen del día de mercado:")
    for empresa, precio_anterior, precio_actual in cambios_dia:
        print(f"{empresa}: Precio anterior ${precio_anterior:.2f} -> Precio actual ${precio_actual:.2f}")
    return precios

#----------------------------------------------------------------------------------------------
#OPCION 4
#----------------------------------------------------------------------------------------------

def mostrar_portafolio(portafolio, empresas, precios):
    if not portafolio:
        print("No tienes acciones en tu portafolio.")
        return

    print("\n--- Portafolio de Inversiones ---")

    for accion in portafolio:
        empresa = accion[0]
        cantidad = accion[1]
        precio_compra = accion[2]
        precio_actual = precios[empresas.index(empresa)]

        print(f"Empresa: {empresa}")
        print(f"Cantidad de acciones: {cantidad}")
        print(f"Precio de compra: ${precio_compra:.2f}")
        print(f"Precio actual: ${precio_actual:.2f}\n")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#----------------------------------------------------------------------------------------------
continuar = True
saldo_usuario= 1000.00
portafolio=[]


#-------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------
while continuar:
    print()
    print("---------------------------")
    print("MENÚ DEL SISTEMA           ")
    print("---------------------------")
    print("[1] Opción 1 (Ingresar empresa)")
    print("[2] Opción 2(Comprar/vender acciones)")
    print("[3] Opción 3(Simular un día de mercado)")
    print("[4] Opción 4(Mostrar portafolio)")
    print("[0] Salir del programa")
    print()
    opcion = int(input("Seleccione una opción: "))
    if opcion in range(0, 5):  # Verifica si la opción es válida
        if opcion == 0:  # Opción salir del programa
            continuar = False
        elif opcion == 1:  # Opción 1
            menu_gestion_empresas()
        elif opcion == 2:  # Opción 2
            menu_gestion_compra()
        elif opcion == 3:  # Opción 3
            simular_dia(empresas,precios)
        elif opcion == 4:  # Opción 4
            mostrar_portafolio(portafolio,empresas,precios)
    else:
        input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if continuar:
        print()
        input("Presione ENTER para volver al menú.")
