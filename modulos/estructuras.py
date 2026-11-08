# Encabezados: cada uno es una COLUMNA de la matriz
ENCABEZADOS = ["Empleado", "Cargo", "Riesgo", "Horas", "Salario", "IBC (40%)",
               "Salud", "Pensión", "ARL", "Total Aportes", "Neto a Pagar"]

# Matriz: lista de filas. Cada fila (otra lista) es un empleado.
matriz_operativos = []


def agregar_fila(nombre, horas, ss):
    """Agrega un empleado a la matriz. `ss` es el resultado de calcular_seguridad_social()."""
    fila = [nombre, ss["cargo"], ss["riesgo"], horas, ss["salario_bruto"], ss["ibc"],
            ss["salud"], ss["pension"], ss["arl"], ss["total_aportes"], ss["total_a_pagar"]]
    matriz_operativos.append(fila)
    return fila


def _m(valor):
    return f"${valor:,.0f}".replace(",", ".")


def matriz_a_texto(matriz=None):
    """Convierte la matriz en una tabla de texto alineada."""
    matriz = matriz_operativos if matriz is None else matriz
    filas = [ENCABEZADOS]
    for f in matriz:
        filas.append([f[0], f[1], f[2], str(f[3])] + [_m(v) for v in f[4:]])
    anchos = [max(len(fila[i]) for fila in filas) for i in range(len(ENCABEZADOS))]
    lineas = []
    for n, fila in enumerate(filas):
        lineas.append(" | ".join(c.ljust(anchos[i]) for i, c in enumerate(fila)))
        if n == 0:
            lineas.append("-+-".join("-" * a for a in anchos))
    return "\n".join(lineas)


def mostrar_matriz(matriz=None):
    print("\n--- MATRIZ DE EMPLEADOS OPERATIVOS ---")
    print(matriz_a_texto(matriz))