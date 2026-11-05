# TransCaribeCol S.A.S. - Módulo de Nómina Administrativa

Este repositorio contiene el sistema automatizado de procesamiento y liquidación de nómina en consola para el personal de **TransCaribeCol S.A.S.** El proyecto está diseñado de forma modular bajo el lenguaje **Python**, permitiendo una fácil escalabilidad para futuras integraciones del equipo de desarrollo.

---

## Estado del Proyecto y Funcionalidades Implementadas

Actualmente, se encuentra completado el **Módulo Base de Liquidación y Persistencia**. Las características implementadas hasta el momento son:

*   **Captura de Datos Dinámica:** Entrada por consola del nombre del empleado, horas normales y horas extras.
*   **Motor de Cálculos:** Procesamiento automático del salario básico, horas extras con recargo y deducciones de ley estrictas bajo la normativa nacional colombiana (Salud 4%, Pensión 4%, ARL Riesgo I 0.522%).
*   **Generador Visual de Volantes:** Impresión simétrica y tabulada del comprobante de pago con formato de moneda local.
*   **Persistencia Local:** Almacenamiento automático de cada volante generado en formato `.txt` dentro del directorio `data/`.

---

## Estructura del Directorio

El proyecto sigue una arquitectura modular separando las responsabilidades de entrada, procesamiento lógico, renderizado visual y almacenamiento de datos:

```text
transcaribecol-nomina/
│
├── main.py                 # Punto de entrada de la aplicación (Menú y Flujo)
├── modulos/                # Paquete de submódulos del sistema
│   ├── __init__.py         # Inicializador del paquete
│   ├── calculos.py         # Motor de fórmulas matemáticas y deducciones
│   ├── formateador.py      # Estructura visual y renderizado del comprobante
│   └── persistencia.py     # Manejo del sistema de archivos y guardado TXT
│
└── data/                   # Directorio de persistencia física (Archivos .txt generados)
```

---

## Instrucciones de Instalación y Ejecución

### Prerrequisitos
*   Python 3.x instalado en el sistema.

### Ejecución
1. Clona este repositorio o navega hasta la carpeta del proyecto.
2. Abre tu terminal y ejecuta el script principal:
   ```bash
   python main.py
   ```
3. Ingresa los datos solicitados en la consola para generar el volante de pago en pantalla y el archivo físico.

---

## Historial de Commits Desarrollados

Para mantener la trazabilidad del código, la construcción de este módulo se estructuró bajo los siguientes commits consecutivos:

1.  `feat: crear estructura inicial y captura de datos del empleado por consola`
2.  `feat: estructurar carpetas del proyecto y crear módulo de cálculos de nómina`
3.  `feat: crear módulo de formateo visual e importar lógica en el main.py`
4.  `fix: corregir formula de deducción ARL y resolver neto negativo en nomina`
5.  `feat: agregar módulo de persistencia para guardar volantes de pago en archivos TXT`

---

## Instrucciones para el Equipo de Desarrollo (Siguientes Pasos)

Para los compañeros encargados de las siguientes funcionalidades, por favor sigan los lineamientos establecidos para mantener la consistencia del proyecto:

1.  **¿Dónde agregar nuevas funcionalidades?**
    *   Creen su propio archivo descriptivo dentro de la carpeta `modulos/` (ej. `modulos/busqueda.py`, `modulos/reportes_generales.py`).
    *   Importen sus funciones en el flujo del archivo `main.py` según corresponda.
2.  **Documentación de Avances:**
    *   Una vez que su funcionalidad esté completamente testeada y confirmada en consola, agreguen un bloque en este `README.md` bajo la sección *"Funcionalidades Implementadas"* detallando su nombre y el objetivo del módulo.
    *   Mantengan la convención de commits (`feat:`, `fix:`, `refactor:`) utilizada hasta ahora.
