============
CHANGELOG
============

.. start-here

1.1.0b
============
* Release date: Unknown
* Changes and new features:
  * Porting to MareNostrum5 (`#97 <https://earth.bsc.es/gitlab/es/hermesv3_bu/-/issues/97>`_)

1.1.0
============
* Release date: 2023/08/22
* Changes and new features:
  * Fugitive fossil fuel sector added

1.0.8
============
* Release date: 2023/06/02
* Changes and new features:
  * Shipping port emissions hardcoded to 2nd layer (layer = 1)

1.0.7
============
* Release date: 2022/03/09
* Changes and new features:
  * Point Source plume rise output as CSV added

1.0.6
============
* Release date: 2022/02/18
* Changes and new features:
  * Add traffic scenario shapefile

1.0.5
============
* Release date: 2020/12/09
* Changes and new features:
  * Added Climatic meteorology

1.0.4
============
* Release date: 2020/07/17
* Changes and new features:
  * Fixed bug on WRF-Chem writer

1.0.3
============
* Release date: 2020/07/06
* Changes and new features:
  * NetCDF read: Added capability to try to read 'lat' instead of 'latitude' and 'lon' instead of 'longitude'
  * Corrected bug on NetCDF compression
  * Corrected bug on emission summary
  * Added CHUNK capability on writer.py
  * R-LINE output bug solved

1.0.2
============
* Release date: 2020/05/04
* Changes and new features:
  * Point source height increment from 1.2 to 1.8
  * MONARCH writer from 64 bits to 32
  * Corrected bug on rotated nested domains

1.0.1
============
* Release date: 2020/04/09
* Changes and new features:
  * Solved bug on road traffic cold emissions
  * Improved memory usage on hot & cold emission calculation
  * Added (option inside the traffic_sector.py script) to downcast from 64 bits to 32 bits

1.0.0
============
* Release date: 2020/03/12
* Changes and new features:
  * First beta version:
    * Grid options:
      1. Regular Lat-Lon
      2. Rotated
      3. Mercator
      4. Lambert conformal conic
    * Clip options:
      1. Shapefile clip: path to a shapefile
      2. Custom clip: list of lat-lon points
      3. Default clip: unary union of the desired output grid

    * Sector Manager:
      1. Aviation sector
      2. Shipping port sector
      3. Livestock sector
      4. Crop operations sector
      5. Crop fertilizers sector
      6. Agricultural machinery sector
      7. Residential combustion sector
      8. Recreational boats sector
      9. Point sources sector
      10. Road traffic sector
      11. Traffic area (evaporative & small cities) sector
      12. Solvents sector

    * Writing options:
      A. Return emissions on memory

      1. Default writer
      2. CMAQ writer
      3. MONARCH writer
      4. WRF-Chem writer
