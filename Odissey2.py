import os
trabajadores = []

def agregar_trabajadores():
    while True:
        nombre = input("Ingrese su Nombre:")
        apellido = input("Ingrese su apellido:")
        
        while True:
            cedula = input("Ingrese su cedula:")
            if cedula.isdigit():
                # Verificar si la cédula ya existe
                if any(t['Cedula'] == cedula for t in trabajadores):
                    print("Error: Esta cédula ya está registrada")
                    continue
                break
            print("Error: La cedula solo debe tener numeros")

        while True:
            salario = input("Ingrese su salario:")
            try: 
                salario = float(salario)
                break
            except ValueError:
                print("Error: Debe ingresar un numero Valido para el salario")

        trabajador = {"Nombre": nombre, "Apellido": apellido, "Cedula": cedula, "Salario": salario}
        trabajadores.append(trabajador)
        print("Trabajador agregado correctamente.\n")
        
        with open("Datos_trabajadores.txt", "a") as archivo:
            archivo.write(f"{nombre},{apellido},{cedula},{salario}\n")

        continuar = input("¿Desea ingresar otro trabajador? (s/n)").lower()
        if continuar != "s":
            break

def crear_lista():
    if os.path.exists("Datos_trabajadores.txt"):
        print("Error: El archivo ya existe. No se puede crear uno nuevo.")
        return
    
    with open("Datos_trabajadores.txt", "w") as archivo:
        archivo.write("")
    trabajadores.clear()
    print("Archivo creado exitosamente")

def ver_archivo():
    try:
        with open("Datos_trabajadores.txt", "r") as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                print("\nNo hay trabajadores registrados")
                return
                
            print("\n--- Lista de Trabajadores ---")
            print(f"{'#':<3} {'Nombre':<15} {'Apellido':<15} {'Cédula':<12} {'Salario':>10}")
            print("-"*60)
            
            for i, linea in enumerate(lineas, 1):
                datos = linea.strip().split(',')
                if len(datos) == 4:
                    print(f"{i:<3} {datos[0]:<15} {datos[1]:<15} {datos[2]:<12} {datos[3]:>10}")
            
            print("-"*60)
            print(f"Total: {len(lineas)} trabajadores")
            
    except FileNotFoundError:
        print("El archivo no existe. Primero debe crearlo")

def modificar_trabajador():
    ver_archivo()
    
    if not trabajadores:
        return
        
    try:
        num = int(input("\nIngrese el número del trabajador a modificar (0 para cancelar): "))
        if num == 0:
            return
        if num < 1 or num > len(trabajadores):
            print("Número inválido")
            return
            
        trabajador = trabajadores[num-1]
        print(f"\nEditando trabajador: {trabajador['Nombre']} {trabajador['Apellido']}")
        
        print("\n1. Cambiar nombre")
        print("2. Cambiar apellido")
        print("3. Cambiar cédula")
        print("4. Cambiar salario")
        print("5. Eliminar trabajador")
        print("6. Cancelar")
        
        opcion = input("\nSeleccione opción: ")
        
        if opcion == "1":
            trabajador['Nombre'] = input("Nuevo nombre: ")
        elif opcion == "2":
            trabajador['Apellido'] = input("Nuevo apellido: ")
        elif opcion == "3":
            while True:
                nueva_cedula = input("Nueva cédula: ")
                if nueva_cedula.isdigit():
                    if any(t['Cedula'] == nueva_cedula for t in trabajadores if t != trabajador):
                        print("Error: Esta cédula ya está registrada")
                        continue
                    trabajador['Cedula'] = nueva_cedula
                    break
                print("Error: La cédula solo debe tener numeros")
        elif opcion == "4":
            while True:
                try:
                    trabajador['Salario'] = float(input("Nuevo salario: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un numero Valido")
        elif opcion == "5":
            confirmacion = input(f"¿Eliminar a {trabajador['Nombre']} {trabajador['Apellido']}? (s/n): ").lower()
            if confirmacion == 's':
                trabajadores.pop(num-1)
                print("Trabajador eliminado")
            else:
                print("Operación cancelada")
                return
        else:
            print("Operación cancelada")
            return
            
        # Actualizar archivo
        with open("Datos_trabajadores.txt", "w") as archivo:
            for t in trabajadores:
                archivo.write(f"{t['Nombre']},{t['Apellido']},{t['Cedula']},{t['Salario']}\n")
                
        print("Cambios guardados exitosamente")
        
    except ValueError:
        print("Debe ingresar un número válido")

def borrar_archivo():
    if os.path.exists("Datos_trabajadores.txt"):
        confirmacion = input("¿Borrar archivo permanentemente? (s/n): ").lower()
        if confirmacion == 's':
            os.remove("Datos_trabajadores.txt")
            trabajadores.clear()
            print("Archivo eliminado")
    else:
        print("El archivo no existe")

# Cargar datos existentes al iniciar
if os.path.exists("Datos_trabajadores.txt"):
    with open("Datos_trabajadores.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if len(datos) == 4:
                trabajadores.append({
                    "Nombre": datos[0],
                    "Apellido": datos[1],
                    "Cedula": datos[2],
                    "Salario": float(datos[3])
                })

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Crear Lista (Nuevo archivo)")
    print("2. Agregar Trabajador")
    print("3. Ver Lista de Trabajadores")
    print("4. Modificar/Eliminar Trabajador")
    print("5. Borrar Archivo")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion == "1":
        crear_lista()
    elif opcion == "2":
        agregar_trabajadores()
    elif opcion == "3":
        ver_archivo()
    elif opcion == "4":
        modificar_trabajador()
    elif opcion == "5":
        borrar_archivo()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente")