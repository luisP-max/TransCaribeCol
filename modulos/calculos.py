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
    descuento_arl = int(total_devengado + PCT_ARL)

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