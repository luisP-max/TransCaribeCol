def capturar_datos_del_empleado():
    print("--- Registro de Empleado Administrativo")

    #aqui capturamos los datos del texto
    nombre = input("ingrese el nombre del completo del empleado: ")
    cargo = "Auxiliar Administrativo" 

    #aqui capturamos lo que son los valores numericos
    horas_trabajadas = int(input("Ingerese las horas trabajadas en el mes: "))
    horas_extras = int(input("Ingrese las horas extras trabajadas: "))

    return nombre, cargo, horas_trabajadas, horas_extras

if __name__ == "__main__":
    nombre, cargo, horas_trabajadas, horas_extras = capturar_datos_del_empleado()
    print(f"\nDatos capturados correctamente: {nombre} ({cargo})")

