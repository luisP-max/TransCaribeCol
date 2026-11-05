def mostrar_volante(nombre, cargo, horas_t, horas_e, resultados):
    # aqui ingreso la moneda colombiana ($ XX.XXX) lo digo por si las moscas no saben que es $.
    # ahora lo que hare es que python reconozca que estoy formateando la moneda colombiana

    def f_moneda(valor):
        return f"${valor:,.0f}".replace(",", ".")

    print("\n" + "="*50)
    print("         TRANSCARIBECOL S.A.S. - COMPROBANTE DE NÓMINA         ")
    print("="*50)
    print(f"Empleado: {nombre.ljust(25)} cargo: {cargo}")
    print(f"Horas Trab.: {str(horas_t).ljust(22)} Horas Extras: {horas_e}")
    print("="*50)
    print(" CONCEPTO                        | INGRESOS    | DESCUENTOS ")
    print("="*50)

    #filas de ingresos

    print(f" Salario Basico (Horas Norm.)   | {f_moneda(resultados['salario_bruto']).ljust(11)} | {'-'.center(10)}")
    print(f" Pago Horas Extras              | {f_moneda(resultados['total_horas_extras']).ljust(11)} | {'-'.center(10)}")

    #filas de descuentos

    print(f" Deduccion Salud (4%)           | {'-'.center(11)} | {f_moneda(resultados['descuento_salud']).ljust(10)}")
    print(f" Deduccion pension (4%)         | {'-'.center(11)} | {f_moneda(resultados['descuento_pension']).ljust(10)}")
    print(f" Deduccion ARL Riesgo I (0.522%)| {'-'.center(11)} | {f_moneda(resultados['descuento_arl']).ljust(10)}")

    print("-"*50)
    #totales
    totales_ingresos = resultados['salario_bruto'] + resultados['total_horas_extras']
    print(f" TOTALES                        | {f_moneda(totales_ingresos).ljust(11)} | {f_moneda(resultados['total_descuentos']).ljust(10)}")
    print("="*50)
    print(f" NETO A PAGAR EN CUENTA:        | {f_moneda(resultados['total_a_pagar'])}")
    print("="*50 + "\n")