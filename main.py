from modulos.calculos import calcular_nomina, calcular_operativo 
from modulos.formateador import mostrar_volante
from modulos.persistencia import guardar_reporte_txt
from modulos.seguridad_social import normalizar_cargo
from modulos.volante_operativo import procesar_operativo, registrar_mas_operativos

def capturar_datos_del_empleado():
    print("--- SISTEMA DE NÓMINA ---")
    print("1. Empleado Administrativo")
    print("2. Empleado Operativo (Trabajador oficial)")
    
    opcion = input("Seleccione el tipo de empleado (1 o 2): ").strip() # Colocar strip() para eliminar espacios en blanco

    # Validación de la opción ingresada
    
    if opcion == "1":
        print("\n--- REGISTRO DE EMPLEADOS ADMINISTRATIVOS ---")
        nombre = input("Ingrese el nombre completo del empleado: ")
        cargo = "Auxiliar Administrativo" 

        try:
            horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: "))
            horas_extras = int(input("Ingrese las horas extras trabajadas: "))
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")
            return None, None # Devolver None para ambos valores en caso de error

        return "administrativo", (nombre, cargo, horas_trabajadas, horas_extras)

    elif opcion == "2":
        print("\n--- REGISTRO DE EMPLEADOS OPERATIVOS ---")
        nombre = input("Ingrese el nombre completo del empleado: ")
        print("Cargos disponibles: Conductor, Oficios Generales, Vigilancia")
        cargo = input("Ingrese el cargo operativo: ").strip()

        return "operativo", (nombre, cargo)
    
    else:
        print("Opción no válida.")
        return None, None

# Ajuste limpio para el bloque principal
if __name__ == "__main__":
    print("--- SISTEMA DE NÓMINA ---")
    print("1. Administrativo")
    print("2. Operativo")
    tipo = input("Elija una opción: ").strip()

    if tipo == "1":
        print("\n--- REGISTRO ADMINISTRATIVO ---")
        nombre = input("Ingrese el nombre completo del empleado: ")
        cargo = "Auxiliar Administrativo"
        try:
            horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: "))
            horas_extras = int(input("Ingrese las horas extras trabajadas: "))
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
            exit()

        # Cálculos, formato y persistencia para administrativos
        resultados_calculados = calcular_nomina(horas_trabajadas, horas_extras)
        mostrar_volante(nombre, cargo, horas_trabajadas, horas_extras, resultados_calculados)
        guardar_reporte_txt(nombre, cargo, horas_trabajadas, horas_extras, resultados_calculados)

    elif tipo == "2":
        print("\n--- REGISTRO OPERATIVO ---")
        nombre = input("Ingrese el nombre completo del empleado: ")
        print("Cargos: conductor, oficios generales, vigilancia")
        cargo = input("Ingrese el cargo: ").strip()

        # Cálculos para operativos
        cargo = normalizar_cargo(cargo)  # acepta "vigilancia" o "vigilante"
        resultados_operativo = calcular_operativo(cargo)

        if "error" in resultados_operativo:
            print(resultados_operativo["error"])
        else:
            # Mostramos en consola de manera sencilla
            print("\n--- VOLANTE DE PAGO OPERATIVO ---")
            print(f"Empleado: {nombre}")
            print(f"Cargo: {resultados_operativo['cargo']}")
            print(f"Horas mensuales: {resultados_operativo['hora_mensuales']}")
            print(f"Salario Bruto: ${resultados_operativo['salario_bruto']:,.0f}")
            print(f"Total a Pagar: ${resultados_operativo['total_a_pagar']:,.0f}")
            print(f"Nota: {resultados_operativo['mensaje_seguridad_social']}")
            
            # aportes, matriz, volante y TXT
            procesar_operativo(nombre, resultados_operativo)
            registrar_mas_operativos()
    else:
        print("Opción no válida.")