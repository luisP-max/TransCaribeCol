PCT_IBC = 0.40     # IBC = 40% del valor del centro 
PCT_SALUD = 0.125  # 12.5%
PCT_PENSION = 0.6  # 16%


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