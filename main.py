from modulos.calculos import calcular_nomina
from modulos.formateador import mostrar_volante

def capturar_datos_del_empleado():
    print("--- REGISTRO DE EMPLEADOS ADMINISTRATIVOS ---")

    #aqui capturamos los datos del texto
    nombre = input("ingrese el nombre del completo del empleado: ")
    cargo = "Auxiliar Administrativo" 

    #validamos que ingresen numeros enteros validos 
    try:
        horas_trabajadas = int(input("Ingrese las horas trabajadas en el mes: "))
        horas_extras = int(input("Ingrese las horas extras trabajas: "))
    except ValueError:
        print("Error: Por favor ingrese valores numericos validos.")
        return None

    return nombre, cargo, horas_trabajadas, horas_extras

if __name__ == "__main__":
    datos = capturar_datos_del_empleado()

    if datos:
        nombre, cargo, horas_trabajadas, horas_extras = datos

        #calculos matematicos
        resultados_calculados = calcular_nomina(horas_trabajadas, horas_extras)

        #formato en consola
        mostrar_volante(nombre, cargo, horas_trabajadas, horas_extras, resultados_calculados)