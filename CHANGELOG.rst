============
CHANGELOG
============

.. start-here

1.1.1b
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

      * Regular Lat-Lon
      * Rotated
      * Mercator
      * Lambert conformal conic

    * Clip options:

      * Shapefile clip: path to a shapefile
      * Custom clip: list of lat-lon points
      * Default clip: unary union of the desired output grid

    * Sector Manager:

      * Aviation sector
      * Shipping port sector
      * Livestock sector
      * Crop operations sector
      * Crop fertilizers sector
      * Agricultural machinery sector
      * Residential combustion sector
      * Recreational boats sector
      * Point sources sector
      * Road traffic sector
      * Traffic area (evaporative & small cities) sector
      * Solvents sector

    * Writing options:

      * Return emissions on memory

      * Default writer
      * CMAQ writer
      * MONARCH writer
      * WRF-Chem writer
