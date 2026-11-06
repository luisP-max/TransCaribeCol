def calcular_nomina(horas_trabajadas, horas_extras):
    #valor por hora
    
    VALOR_HORA_NORMAL = 20000
    VALOR_HORA_EXTRA = 25000

    #porcentaje de descuento
    
    PCT_SALUD = 0.04
    PCT_PENSION = 0.04
    PCT_ARL = 0.00522

    #calculos de ingresos
    
    salario_bruto = horas_trabajadas * VALOR_HORA_NORMAL
    total_horas_extras = horas_extras * VALOR_HORA_EXTRA
    total_devengado = salario_bruto + total_horas_extras

    #calculos de descuentos de ley 

    descuento_salud = int(total_devengado * PCT_SALUD)
    descuento_pension = int(total_devengado * PCT_PENSION)
    descuento_arl = int(total_devengado * PCT_ARL)

    total_descuentos = descuento_salud + descuento_pension + descuento_arl

    #total neto a pagar
    
    total_a_pagar = total_devengado - total_descuentos

    #libreria
    return{
        "salario_bruto": salario_bruto,
        "total_horas_extras": total_horas_extras,
        "descuento_salud": descuento_salud,
        "descuento_pension": descuento_pension,
        "descuento_arl": descuento_arl,
        "total_descuentos": total_descuentos,
        "total_a_pagar": total_a_pagar
    }
    


def calcular_operativo(cargo):
    """
    Calcula la asignación para el empleado Operativo (Trabajador oficial) 
    según las horas fijas de su cargo.
    """
    
    VALOR_HORA_OPERATIVO = 40000
    
    cargos_horas = {
        "conductor": 160,
        "oficios generales": 100,
        "vigilante": 336
    }
    
    cargo_limpio = cargo.strip().lower()  # Limpiar el cargo para evitar errores de mayúsculas/minúsculas y espacios
    
    if  cargo_limpio not in cargos_horas:
        return {
            "error": f"Cargo Operativo '{cargo}' no válido."
        }
    
    ## Horas mensuales según el cargo
    
    hora_mensuales = cargos_horas[cargo_limpio]
    salario_bruto = hora_mensuales * VALOR_HORA_OPERATIVO
    
    return {
        "cargo": cargo,
        "hora_mensuales": hora_mensuales,
        "salario_bruto": salario_bruto,
        "total_a_pagar": salario_bruto,
        "mensaje_seguridad_social": "El empleado cancela de forma autónoma sus aportes."
        }   