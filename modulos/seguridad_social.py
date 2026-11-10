PCT_IBC = 0.40     # IBC = 40% del valor del centro 
PCT_SALUD = 0.125  # 12.5%
PCT_PENSION = 0.16  # 16%


# Nivel del riesgo y % de ARL por cargo 

Riesgo_ARL = {
    "oficios generales": {"cargo": "Oficios Generales", "riesgo": "I",  "pct_arl": 0.00522},
    "conductor":         {"cargo": "Conductor",         "riesgo": "II", "pct_arl": 0.01044},
    "vigilancia":        {"cargo": "Vigilancia",        "riesgo": "IV", "pct_arl": 0.04350},
}
ALIAS_CARGOS = {"vigilante": "vigilancia"}

def normalizar_cargo(cargo):
    limpio = cargo.strip().lower()
    return "vigilante" if limpio == "vigilante" else limpio


def obtener_info_riesgo(cargo):
    limpio = cargo.strip().lower()
    limpio = ALIAS_CARGOS.get(limpio, limpio)
    return Riesgo_ARL.get(limpio)

def calcular_seguridad_social(salario_bruto, cargo):
    info = obtener_info_riesgo(cargo)
    if info is None:
        return {"error": f"Cargo '{cargo}' sin nivel de riesgo definido."}
    ibc = int(salario_bruto * PCT_IBC)
    salud = int(ibc * PCT_SALUD)
    pension = int(ibc * PCT_PENSION)
    arl = int(ibc * info["pct_arl"])
    total_aportes = salud + pension + arl

    return {
        "cargo": info["cargo"], "riesgo": info["riesgo"], "pct_arl": info["pct_arl"],
        "salario_bruto": salario_bruto, "ibc": ibc,
        "salud": salud, "pension": pension, "arl": arl,
        "total_aportes": total_aportes,
        "total_a_pagar": salario_bruto - total_aportes,
    }