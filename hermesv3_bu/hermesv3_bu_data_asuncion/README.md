## HERMESv3_BU input dataset

This project contains an input dataset to test the build of the [HERMESv3_BU model](https://earth.bsc.es/gitlab/es/hermesv3_bu).

# Archivos mínimos para correr la simulación del sector tráfico en HERMESv3_BU (Asunción)

A continuación se detalla la lista completa de archivos requeridos, su función, ubicación esperada y formato.

---

## 1. Archivos de configuración y salida

| Tipo                        | Ruta                                               | Descripción                                                              |
| --------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| **Configuración principal** | `conf/hermes_traffic_asuncion.conf`                | Define dominio, fechas, rutas a datos y sectores activos (solo tráfico). |
| **Salida NetCDF**           | `OUT_asuncion/HERMESv3_<date>_traffic_asuncion.nc` | Archivo resultante con emisiones horarias (NOx, CO, PM, etc.).           |

---

## 2. Estructura de datos (`hermesv3_bu_data_asuncion/`)

```

hermesv3_bu_data_asuncion/
├── common/
├── profiles/
│   ├── temporal/traffic/
│   │   ├── aadt_h_mn.csv
│   │   ├── aadt_h_sat.csv
│   │   ├── aadt_h_sun.csv
│   │   ├── aadt_h_wd.csv
│   │   ├── aadt_m_mn.csv
│   │   ├── aadt_week.csv
│   │   └── speed_hourly.csv
│   ├── speciation/
│   │   ├── map_base.csv
│   │   ├── MolecularWeights.csv
│   │   └── traffic/
│   │       ├── hot_cold_base.csv
│   │       ├── tyre_base.csv
│   │       ├── road_base.csv
│   │       ├── brake_base.csv
│   │       └── resuspension_base.csv
│   └── vertical/
│       └── DEFAULT_6layers_vertical_description.csv
└── traffic/
├── ef/
│   ├── hot_*.csv
│   ├── cold_*.csv
│   ├── road_pm.csv
│   ├── tyre_pm.csv
│   ├── brake_pm.csv
│   └── resuspension_pm.csv
├── fleet_compo/
│   └── fleet_compo_asuncion.csv
└── road_links/
└── road_links_asuncion.shp  (junto con .dbf, .shx, .prj)

````

---

## 3. Archivos específicos del sector tráfico

### a) Red vial — `traffic/road_links/road_links_asuncion.shp`

Obligatorio. Shapefile con geometría **LineString**.

Archivos requeridos: `.shp`, `.shx`, `.dbf`, `.prj`.

Campos mínimos:

| Campo      | Descripción                  | Ejemplo |
| ---------- | ---------------------------- | ------- |
| `link_ID`  | Identificador único          | 1023    |
| `length_m` | Longitud del tramo en metros | 350.0   |
| `aadt`     | Tráfico medio diario anual   | 12500   |
| `speed`    | Velocidad promedio (km/h)    | 45      |
| `geometry` | Geometría (LineString)       | —       |

CRS obligatorio: **EPSG:4326**

---

### b) Composición vehicular — `traffic/fleet_compo/fleet_compo_asuncion.csv`

Ejemplo mínimo:

```csv
Code,Class,F001,F002,F003
PCG_25,Passenger_Cars_Gasoline,0.45,0.0,0.0
PCD_13,Passenger_Cars_Diesel,0.45,0.0,0.0
LCV_15,Light_Commercial_Diesel,0.05,0.0,0.0
HDV_20,Heavy_Diesel,0.05,0.0,0.0
````

Los códigos deben coincidir con los de `ef/hot_*.csv`.

---

### c) Factores de emisión — `traffic/ef/*.csv`

Archivos requeridos (copiados del dataset base):

```
hot_nox_no2.csv
hot_nh3.csv
hot_co.csv
hot_so2.csv
hot_pm.csv
hot_voc.csv
hot_ch4.csv
cold_nox_no2.csv
cold_nh3.csv
cold_co.csv
cold_so2.csv
cold_pm.csv
cold_voc.csv
cold_ch4.csv
tyre_pm.csv
road_pm.csv
brake_pm.csv
resuspension_pm.csv
```

---

## 4. Archivos de perfiles

Todos se copian del dataset base.

* **Temporales**: `aadt_m_mn.csv`, `aadt_week.csv`, `aadt_h_mn.csv`, `aadt_h_wd.csv`, `aadt_h_sat.csv`, `aadt_h_sun.csv`, `speed_hourly.csv`
* **Especiación**: `map_base.csv`, `MolecularWeights.csv`, `traffic/hot_cold_base.csv`, `tyre_base.csv`, `road_base.csv`, `brake_base.csv`, `resuspension_base.csv`
* **Vertical**: `DEFAULT_6layers_vertical_description.csv`

---

## 5. Archivos internos (se regeneran automáticamente)

El modelo crea:

```
hermesv3_bu_aux/
  └── d03_1km/
      ├── grid/grid.nc
      ├── clip/clip.shp
      └── ...
```

Para regenerarlos basta con borrar la carpeta antes de ejecutar.

---

## 6. Resumen corto

| Tipo                              | Ruta                                | Fuente / Acción |
| --------------------------------- | ----------------------------------- | --------------- |
| `.conf`                           | `conf/hermes_traffic_asuncion.conf` | Adaptar dominio |
| `road_links_asuncion.shp`         | Crear desde OSM/QGIS                | Nuevo           |
| `fleet_compo_asuncion.csv`        | Ajustar proporciones locales        | Nuevo           |
| `ef/*.csv`                        | Copiar del dataset base             | Listo           |
| `profiles/temporal/traffic/*.csv` | Copiar del dataset base             | Listo           |
| `profiles/speciation/...`         | Copiar del dataset base             | Listo           |
| `profiles/vertical/...`           | Copiar del dataset base             | Listo           |



