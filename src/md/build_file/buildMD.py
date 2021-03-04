#!/usr/bin/env python
from numpy import * 
from subprocess import *
import os
import fileinput

#   ----    create new folder     ----
def create_folder(cdir):
    if ( os.path.exists(cdir) is not True ):
        os.makedirs(cdir)

#   ----    prepare simulation scripts      ----
def prepare_simulation(lmp_bin_path,workDir,runId,dataFolder,paramsFolder,simFolder,nfac=1.0):

    # create folder
    rundir = workDir + '/run%02d/'%runId
    create_folder(rundir)

    # create run script
    runFile = rundir + 'run.sh'
    with open(runFile, 'w') as pf:
        cmd = '''#!/bin/bash

%s/lmp_openmpi < in.chromosome
''' %lmp_bin_path
        pf.write(cmd)
    cmd = 'chmod 744 %s'%runFile
    os.system(cmd)

    # prepare softcore include file
    ntype = 7
    with open(paramsFolder+'soft_core_p_include.txt','w') as fw:
        for i in xrange(1,ntype+1):
            for j in xrange(i,ntype+1):
                fw.write('pair_coeff         %d    %d table %s/soft_core_lj_4kT.table soft_core_lj 1.12\n'%(i,j,paramsFolder))

    # lammps input file with custom random seed
    inFile = rundir + 'in.chromosome'
    in_tmp = fileinput.input(simFolder+'lammps_template.in')
    with open(inFile, 'w') as pf:
        pf.write('variable        rseed equal   %d\n'%(4928459+runId))
        for line in in_tmp:
            if line[0:9] == 'read_data':
                pf.write('read_data\t%s/data.genome\n'%dataFolder)
            elif line[0:10] == 'pair_style':
                pf.write('pair_style\thybrid/overlay table linear 10000 \
tanhlr/cut/ideals 6.0 %s/ideal_potential_autosome.txt %s/ideal_potential_Xi.txt %.3f \
tanhlr/cut/domainab 6.0 3 46 %s/bead_index.txt %s/specific_ab_index.txt %s/specific_AB_potential.txt lj/cut 1.12\n'\
%(paramsFolder,paramsFolder,nfac,simFolder,simFolder,paramsFolder))
            elif line[0:7] == 'include':
                pf.write('include\t\t%s/soft_core_p_include.txt\n'%paramsFolder)
                pf.write('include\t\t%s/intra_AB_and_homolog.txt\n'%paramsFolder)
            else:
                pf.write(line)

#   ----    run simulation     ----
def run_simulation(workDir,runId):

    # run simulation
    rundir = workDir + '/run%02d/'%runId
    os.system('cd %s; ./run.sh'%rundir)

