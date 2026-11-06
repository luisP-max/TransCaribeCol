import os

def guardar_reporte_txt(nombre, cargo, horas_t, horas_e, resultados):
    #formateo de la moneda de colombia $
    def f_moneda(valor):
        return f"${valor:,.0f}".replace(",", ".")

    #aqui lo que hace python asegura que la carpeta "data" exista

    os.makedirs("data", exist_ok=True)

    #creo un nombre de archivo limpio basado en el nombre del empleado

    nombre_limpio = nombre.replace(" ", "_").lower()
    ruta_archivo = f"data/nomina_{nombre_limpio}.txt"

    #genera el bloque de texto con el mismo formato que aparece en la consola

    total_ingreso = resultados['salario_bruto'] + resultados['total_horas_extras']
    
    contenido = (
        f"{'='*50}\n"
        f"         TRANSCARIBECOL S.A.S. - COMPROBANTE DE NÓMINA         \n"
        f"{'='*50}\n"
        f"Empleado: {nombre.ljust(25)} Cargo: {cargo}\n"
        f"Horas Trab.: {str(horas_t).ljust(22)} Horas Extras: {horas_e}\n"
        f"{'-'*50}\n"
        f" CONCEPTO                        | INGRESOS    | DESCUENTOS \n"
        f"{'-'*50}\n"
        f" Salario Básico (Horas Norm.)    | {f_moneda(resultados['salario_bruto']).ljust(11)} | {'-'.center(10)}\n"
        f" Pago Horas Extras               | {f_moneda(resultados['total_horas_extras']).ljust(11)} | {'-'.center(10)}\n"
        f" Deducción Salud (4%)            | {'-'.center(11)} | {f_moneda(resultados['descuento_salud']).ljust(10)}\n"
        f" Deducción Pensión (4%)          | {'-'.center(11)} | {f_moneda(resultados['descuento_pension']).ljust(10)}\n"
        f" Deducción ARL Riesgo I (0.522%) | {'-'.center(11)} | {f_moneda(resultados['descuento_arl']).ljust(10)}\n"
        f"{'-'*50}\n"
        f" TOTALES                         | {f_moneda(total_ingreso).ljust(11)} | {f_moneda(resultados['total_descuentos']).ljust(10)}\n"
        f"{'='*50}\n"
        f" NETO A PAGAR EN CUENTA:           {f_moneda(resultados['total_a_pagar'])}\n"
        f"{'='*50}\n"
    )

    #escribe el archivo
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print(f" Reporte guardado con exito en: {ruta_archivo}")
    