import os
from modulos.seguridad_social import calcular_seguridad_social, normalizar_cargo
from modulos.calculos import calcular_operativo      # función que ya existía, solo se reutiliza
from modulos import estructuras

ANCHO = 50   # ancho del volante (igual al del volante administrativo)


def _m(valor):
    """Formato de moneda colombiana: 1000000 -> $1.000.000"""
    return f"${valor:,.0f}".replace(",", ".")


def construir_volante(nombre, horas, ss):
    """
    Arma el texto del volante y lo devuelve como un string.
    Recibe: nombre, horas del mes y `ss` (resultado de calcular_seguridad_social).
    """
    # Muestra el % de ARL sin ceros sobrantes: 0.00522 -> "0.522", 0.0435 -> "4.35"
    pct_arl = f"{ss['pct_arl'] * 100:.3f}".rstrip("0").rstrip(".")

    def fila(concepto, ing="-", des="-"):
        # Una fila de la tabla: concepto | ingresos | descuentos (columnas alineadas)
        return f" {concepto.ljust(32)}| {ing.center(11)} | {des.center(10)}\n"

    return (
        # --- Encabezado ---
        f"{'=' * ANCHO}\n"
        f"    TRANSCARIBECOL S.A.S. - COMPROBANTE DE PAGO OPERATIVO\n"
        f"{'=' * ANCHO}\n"
        f"Empleado: {nombre.ljust(25)} Cargo: {ss['cargo']}\n"
        f"Horas Mes: {str(horas).ljust(24)} Riesgo ARL: {ss['riesgo']}\n"
        f"Contrato: Prestación de servicios (sin horas extras)\n"
        f"{'=' * ANCHO}\n"
        f" CONCEPTO                        | INGRESOS    | DESCUENTOS\n"
        f"{'=' * ANCHO}\n"
        # --- Ingresos: solo honorarios (no hay horas extras) ---
        + fila("Honorarios (Valor contrato)", _m(ss["salario_bruto"]))
        # --- Informativo: IBC, base sobre la que se calculan los aportes ---
        + fila("IBC (40% del contrato)", _m(ss["ibc"]), "(base)")
        # --- Descuentos: los tres aportes de seguridad social ---
        + fila("Aporte Salud (12.5% IBC)", "-", _m(ss["salud"]))
        + fila("Aporte Pensión (16% IBC)", "-", _m(ss["pension"]))
        + fila(f"Aporte ARL Riesgo {ss['riesgo']} ({pct_arl}%)", "-", _m(ss["arl"]))
        + f"{'-' * ANCHO}\n"
        # --- Totales y neto ---
        + fila("TOTALES", _m(ss["salario_bruto"]), _m(ss["total_aportes"]))
        + f"{'=' * ANCHO}\n"
        f" NETO A PAGAR EN CUENTA:           {_m(ss['total_a_pagar'])}\n"
        f"{'=' * ANCHO}\n"
    )


def guardar_volante_txt(nombre, texto_volante):
    #Guarda el volante de UN empleado en: data/nomina_operativo_<nombre>.txt
    os.makedirs("data", exist_ok=True)   # crea la carpeta data/ si no existe
    ruta = f"data/nomina_operativo_{nombre.replace(' ', '_').lower()}.txt"
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(texto_volante)
    print(f" Reporte guardado con exito en: {ruta}")
    return ruta


def guardar_matriz_txt(ruta="data/matriz_operativos.txt"):
    #Guarda la matriz completa (todos los operativos registrados) en un TXT.
    os.makedirs("data", exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(estructuras.matriz_a_texto() + "\n")
    print(f" Matriz guardada con exito en: {ruta}")
    return ruta


def procesar_operativo(nombre, resultados_operativo):
    #Procesa UN empleado operativo de principio a fin.

    # Paso 1: calcular los aportes de seguridad social
    ss = calcular_seguridad_social(resultados_operativo["salario_bruto"],
                                  resultados_operativo["cargo"])
    if "error" in ss:
        print(ss["error"])
        return

    horas = resultados_operativo["hora_mensuales"]

    # Paso 2: guardar al empleado como una fila nueva en la matriz
    estructuras.agregar_fila(nombre, horas, ss)

    # Paso 3: armar, mostrar y guardar el volante
    texto = construir_volante(nombre, horas, ss)
    print("\n" + texto)
    guardar_volante_txt(nombre, texto)


def registrar_mas_operativos():
    #Pregunta si se quieren registrar más operativos (bucle). Al terminar muestra la matriz en consola y la guarda en TXT.

    while input("\n¿Registrar otro empleado operativo? (s/n): ").strip().lower() == "s":
        nombre = input("Ingrese el nombre completo del empleado: ")
        cargo = input("Ingrese el cargo (conductor, oficios generales, vigilancia): ")
        res = calcular_operativo(normalizar_cargo(cargo))   # normaliza "vigilancia" -> "vigilante"
        if "error" in res:
            print(res["error"])
            continue                                         # vuelve a preguntar
        procesar_operativo(nombre, res)

    estructuras.mostrar_matriz()   # tabla final en consola
    guardar_matriz_txt()           # tabla final en TXT