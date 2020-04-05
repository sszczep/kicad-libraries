# KiCad Libraries

Set of symbols/footprints/models that I've created for my projects.

###### I'm not taking responsibility for any mistakes that I could have made. Be sure to double check all the dimensions and wiring before using in projects. 

## How to use

Download footprints (***.pretty** directories) and symbols (***.lib** files) that you want to use and add them as global or project specific libraries. To use 3D Models, you must create **SSZCZEP_MODELS** environment variable pointing to **models** directory.

## Footprints

### CherryMX.pretty

Over 400 different footprints for Cherry MX switches generated using [this](https://github.com/sszczep/kicad-libraries/blob/master/footprints/CherryMX.pretty/generate.py) code. 

It includes variants such as:
* Plate/PCB mounted
* Stabilizer Plate/PCB mounted
* No LED/2 pin LED/LTST-A683CEGBW
* Normal switch mount/Kailh Socket for hot-swap compatibility

## 3D Models

### LTST-A683CEGBW.step

Reverse mounted RGB SMD LED that I use for underglowing Cherry MX switches.
Detailed datasheet can be found [here](https://optoelectronics.liteon.com/upload/download/DS35-2019-0032/LTST-A683CEGBW.PDF).

### KailhSocket.stp

This model was obtained from [*QMK*](https://github.com/qmk). All credits go to them. The exact file can be found [here](https://github.com/qmk/qmk_hardware/blob/master/components/kailh_socket_mx.stp). I'm keeping it here as it is easier to link and use in all of my projects. 
