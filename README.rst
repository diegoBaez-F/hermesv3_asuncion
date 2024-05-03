HERMESv3_BU - High-Elective Resolution Modelling Emission System version 3 – Bottom-Up
===========================================================================================

The High-Elective Resolution Modelling Emission System version 3 for Bottom-Up approaches (HERMESv3_BU) is a Python-based, open source, parallel and stand-alone emission model that estimates high-resolution anthropogenic emissions for air quality modelling.

Description
-----------

HERMESv3_BU is an emission model that estimates anthropogenic emissions at the source (e.g. road link, industrial facility) and hourly level combining state-of-the-art estimation methods with local activity and emission factors along with meteorological data.

The model covers the estimation of bottom-up emissions from point sources, road transport, residential and commercial combustion, other mobile sources and agricultural activities. The computed pollutants include main criteria pollutants (i.e. NOx; CO; NMVOC; SOx; NH3; PM10 and PM2.5).

Specific emission estimation methodologies are provided for each source, and are mostly based on (but not limited to) the calculation methodologies reported by the European EMEP/EEA air pollutant emission inventory guidebook. Meteorological-dependent functions are also included to take into account the dynamical component of the emission processes.

The model also provides several functionalities for automatically manipulating and performing spatial operations on georeferenced objects (shapefiles and raster files). The model is designed so that it can be applicable to any European country/region where the required input data is available.

Emissions can be estimated on several user-defined grids, mapped to multiple chemical mechanisms and adapted to the input requirements of different atmospheric chemistry models (CMAQ, WRF-Chem and MONARCH) as well as a street-level dispersion model (R-LINE).

Availability
------------

HERMESv3_BU is distributed free of charge under the licence `GNU GPL v3.0 <https://www.gnu.org/licenses/quick-guide-gplv3.html>`__.

Disclaimer
----------

Despite intensive work on the development and testing of HERMESv3_BU, some issues may arise when external users start to execute it for different frameworks. We welcome your feedback and will try to provide maximum support within our limited time resources.

How to cite
-----------

* Guevara, M., Tena, C., Porquet, M., Jorba, O., and Pérez García-Pando, C.: HERMESv3, a stand-alone multi-scale atmospheric emission modelling framework – Part 2: The bottom–up module, Geosci. Model Dev., 13, 873–903, https://doi.org/10.5194/gmd-13-873-2020, 2020.

Contact persons
---------------

Code developed by `Barcelona Supercomputing Centre <https://www.bsc.es/>`__ (BSC-CNS).

Developers:
* `marc.guevara@bsc.es <https://www.bsc.es/guevara-marc>`
* `carles.tena@bsc.es <https://www.bsc.es/tena-carles>`

Support
------------

Due to our limited time and resources, the developing team cannot guarantee regular support. Nevertheless, we will be happy to provide advice for new users.
Questions should be sent to the HERMESv3 mailing list:
* <hermesv3@bsc.es>

To join the mailing list, send an email to hermesv3-join@bsc.es (also include marc.guevara@bsc.es) with the following information:
* Name
* Organization
* Country.