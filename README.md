# HERMESv3_BU Asunción

HERMESv3_BU Asunción es una distribución del modelo de emisiones bottom-up HERMESv3_BU, un sistema desarrollado por el Barcelona Supercomputing Center (BSC) para generar inventarios horarios y espacialmente distribuidos de emisiones atmosféricas. El repositorio contiene el código fuente del motor de cálculo, utilidades para el preprocesado de datos y ejemplos de configuración para ejecutar simulaciones personalizadas.

## Características principales

- Motor de cálculo paralelizado mediante **MPI** para ejecutar simulaciones de emisiones a gran escala.
- Soporte para distintos tipos de rejillas (Lambert Conformal Conic, Mercator, Regular, Rotated y Rotated Nested).
- Integración con múltiples sectores emisores (tráfico, residencial, ganadería, solventes, etc.) mediante un gestor modular de sectores (`SectorManager`).
- Escritura de resultados en distintos formatos (MONARCH, CMAQ, WRF-Chem o un formato genérico) gracias al sistema de `writer` extensible.
- Herramientas auxiliares para el recorte de dominios, descarga de benchmarks y manipulación de datos auxiliares.

## Requisitos previos

- **Python 3.11** o superior.
- Compilación del intérprete con soporte para MPI y la librería `mpi4py` funcional.
- Dependencias científicas y geoespaciales descritas en `requirements.txt` o `environment.yml` (NumPy, pandas, netCDF4, GeoPandas, Fiona, Rtree, Shapely, Rasterio, etc.).
- Acceso a los datos auxiliares de HERMESv3_BU (shapefiles, perfiles temporales y verticales, mapas de población, etc.). Consulte la documentación interna del proyecto para la obtención de estos recursos.

## Instalación

### 1. Crear y activar un entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

También puede reproducir el entorno de Conda/Mamba incluido:

```bash
mamba env create -f environment.yml
mamba activate hermesv3_bu
```

### 2. Instalar el paquete

Instale el proyecto en modo editable para facilitar el desarrollo:

```bash
pip install -e .
```

Esto instalará las dependencias listadas en `setup.py` y expondrá los comandos `hermesv3_bu` y `hermesv3_bu_download_benchmark` en su entorno.

## Configuración

El archivo `conf/hermes.conf` contiene un ejemplo completo de configuración. Los parámetros más relevantes son:

- **[GENERAL]**: rutas de datos (`input_dir`, `data_path`, `auxiliary_files_path`), fechas de simulación (`start_date`, `end_date`), frecuencia de salida (`output_timestep_num`) y opciones de registro.
- **[DOMAIN]**: definición de la rejilla objetivo (tipo de dominio, dimensiones, proyección y atributos de salida).
- **[CLIPPING]**: geometrías o shapefiles utilizados para recortar el dominio.
- **[SECTOR MANAGEMENT]**: asignación de procesadores a cada sector emisor cuando se ejecuta en paralelo.
- **[SHAPEFILES] / [SPECIATION DATA]**: rutas a los ficheros auxiliares que se emplean durante el cálculo.

Puede generar nuevas configuraciones copiando este archivo y adaptando cada bloque a su dominio, inventario y disponibilidad de datos.

## Ejecución de una simulación

Una vez configurados los datos y parámetros:

```bash
mpirun -n <num_procesos> hermesv3_bu --config conf/hermes.conf
```

El comando anterior inicializa la clase `HermesBu` (`hermesv3_bu/hermes.py`), ejecuta el `SectorManager`, sincroniza los procesos MPI y escribe los ficheros de emisiones mediante el `writer` seleccionado. Si se establece `first_time = 1`, el modelo únicamente generará los archivos auxiliares necesarios.

## Estructura del repositorio

- `hermesv3_bu/`: código fuente del modelo y sus componentes principales.
  - `config/`: manejo de argumentos y lectura de archivos de configuración.
  - `grids/`, `clipping/`, `writer/`: definición de rejillas, recortes espaciales y salida de resultados.
  - `sectors/`: lógica específica para cada sector emisor.
  - `tools/`: utilidades (descarga de benchmarks, scripts de ayuda, etc.).
  - `hermes.py`: punto de entrada principal del modelo.
- `conf/`: ejemplos de archivos de configuración.
- `tests/`: batería de pruebas automatizadas y utilidades para medir cobertura.
- `run_test.py`: script auxiliar para ejecutar pytest con informes de cobertura.
- `requirements.txt` / `environment.yml`: definición de dependencias para pip o Conda/Mamba.
- `CHANGELOG`, `LICENSE`: documentación legal e historial de cambios.

## Pruebas automatizadas

Para validar los cambios durante el desarrollo se recomienda ejecutar:

```bash
python run_test.py
```

El script genera reportes HTML y XML en `tests/report/python<versión>/` con los resultados de cobertura de código.

## Contribuir

1. Cree un fork del repositorio y genere una rama descriptiva.
2. Aplique los cambios necesarios y añada pruebas cuando corresponda.
3. Ejecute `python run_test.py` para asegurarse de que la batería de pruebas pasa correctamente.
4. Abra un _merge request_ describiendo el contexto, los cambios realizados y los pasos de validación.

## Licencia

Este proyecto se distribuye bajo la Licencia Pública General de GNU versión 3 (GPLv3). Consulte el archivo `LICENSE` para más detalles.

## Contacto y soporte

Para cuestiones técnicas, contribuciones o solicitudes de nuevos datos, póngase en contacto con el equipo responsable en el BSC (por ejemplo, `carles.tena@bsc.es`) o consulte la documentación oficial disponible en el portal interno del proyecto.
