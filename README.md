# Chromatin Network Retards Nucleoli Coalescence
 [![bioRxiv shield](https://img.shields.io/badge/bioRxiv-2021.03.02-green.svg?style=flat)](https://www.biorxiv.org/content/10.1101/2021.03.02.433564v1) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This is the repository of core scripts to set up Molecular Dynamics (MD) simulations detailed in the manuscript "Chromatin Network Retards Droplet Coalescence" [(bioRxiv)](https://www.biorxiv.org/content/10.1101/2021.03.02.433564v1).

* The first step is to set up the MD simulator Large-scale Atomic/Molecular Massively Parallel Simulator ([LAMMPS](https://lammps.sandia.gov/)), which is an open-source computational package for MD simulation. The standard LAMMPS package (tarball) can be downloaded [here](https://lammps.sandia.gov/tars/) and following the doc of LAMMPS [instructions](https://lammps.sandia.gov/doc/Install_tarball.html) to build the LAMMPS directory. We have been using the version [lammps-17Nov16](https://lammps.sandia.gov/tars/lammps-17Nov16.tar.gz), on which our custom modifications were built.

* After downloading the standard LAMMPS package, copy our custom modifications in [./src/lammps/](./src/lammps/) to the directory /LAMMPS/src/ of the downloaded package and compile.
  * Note that the [GCC](https://gcc.gnu.org/) compiler needs to be installed beforehand and an environment of [OpenMPI](https://www.open-mpi.org/) is needed to compile the parallel version of LAMMPS. 
  * On a "normal" desktop computer, the typical install time including download and compile steps is ~ 5 to 10 minutes.
* After the compilation of LAMMPS, direct the binary file in [run.py](run.py) (line 11) and execute [run.py](./run.py) to simulate the trajectory in [./sim/run00/](./sim/run00/). Additional independent simulations can be performed by changing the run index in  [run.py](run.py) (line 17) and re-execute the code. 
* An example simulated trajectory is provided [here](https://drive.google.com/file/d/1VGSmczlQUNC2zCUxzTgqdPl8vqJzOPDH/view?usp=sharing).

