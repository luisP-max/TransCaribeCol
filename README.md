# TransCaribeCol S.A.S. - Sistema Integral de Nómina

Este repositorio contiene la aplicación de consola para la gestión, liquidación y almacenamiento de nómina de **TransCaribeCol S.A.S.** El proyecto está desarrollado en **Python** bajo una arquitectura modular que permite gestionar tanto al personal administrativo como a los trabajadores operativos (prestación de servicios).

---

## Estado del Proyecto y Funcionalidades Implementadas

El sistema cuenta con dos flujos principales seleccionados desde el menú inicial de consola:

### 1. Módulo de Empleados Administrativos
*   **Captura de Datos:** Registro por consola del nombre, horas normales trabajadas y horas extras del mes.
*   **Liquidación Salarial:** Cálculo automático del salario básico (\$20.000/hora) y horas extras (\$25.000/hora).
*   **Deducciones de Ley:** Aplicación de descuentos de Salud (4%), Pensión (4%) y ARL Riesgo I (0.522%) sobre el total devengado.
*   **Volante y Persistencia:** Impresión del comprobante tabulado en consola y exportación automática en `data/nomina_<nombre>.txt`.

### 2. Módulo de Empleados Operativos (Trabajadores Oficiales)
*   **Gestión por Cargo:** Soporte para cargos operativos con horas mensuales fijas a \$40.000/hora: *Conductor* (160h), *Oficios Generales* (100h) y *Vigilancia* (336h).
*   **Seguridad Social e IBC:** Cálculo del Ingreso Base de Cotización (IBC al 40% del contrato) y deducciones de Salud (12.5%), Pensión (16%) y ARL según el nivel de riesgo del cargo (Riesgo I, II o IV).
*   **Registro Múltiple y Matriz Consolidada:** Bucle interactivo para liquidar múltiples trabajadores operativos en una misma sesión. Genera volantes individuales (`data/nomina_operativo_<nombre>.txt`) y consolida todos los registros en una tabla general exportada en `data/matriz_operativos.txt`.

---

## Estructura del Directorio

El proyecto separa las responsabilidades de cálculo, formato visual, estructuras de datos y guardado de archivos planos dentro del paquete `modulos/`:

```text
transcaribecol-nomina/
│
├── main.py                      # Punto de entrada, menú principal y control de flujo
├── modulos/                     # Paquete de submódulos del sistema
│   ├── __init__.py              # Inicializador del paquete
│   ├── calculos.py              # Fórmulas salariales para administrativos y operativos
│   ├── seguridad_social.py      # Tablas de riesgo ARL y cálculo de aportes IBC (Operativos)
│   ├── estructuras.py           # Gestión de matriz consolidada en memoria y formateo de tabla
│   ├── formateador.py           # Renderizado visual del comprobante administrativo
│   ├── persistencia.py          # Exportación de comprobantes administrativos a TXT
│   └── volante_operativo.py     # Flujo completo, volantes y exportación de matriz operativa
│
└── data/                        # Directorio autogenerado con todos los reportes .txt
```

---

## Instrucciones de Instalación y Ejecución

### Prerrequisitos
*   Tener instalado **Python 3.x** en el sistema. No requiere librerías externas (usa únicamente módulos nativos como `os`).

### Pasos para ejecutar
1. Abre una terminal y ubícate en la carpeta raíz del proyecto.
2. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```
3. Selecciona la opción deseada (`1` para Administrativo o `2` para Operativo) y sigue las instrucciones en pantalla.
4. Consulta los archivos generados dentro de la carpeta `data/`.

---