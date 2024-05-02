#!/bin/sh

tleap -f tleap.in # create initial system (water box)
export PLUMED_KERNEL=~/opt/lib/libplumedKernel.so # import plumed
pmemd.cuda -O -i 01_Min.in -o 01_Min.out -p parm7 -c rst7 -r 01_Min.ncrst # minimize
pmemd.cuda -O -i 02_Heat.in -o 02_Heat.out -p parm7 -c 01_Min.ncrst -r 02_Heat.ncrst -x 02_Heat.nc # heat
pmemd.cuda -O -i 03_Prod.in -o 03_Prod.out -p parm7 -c 02_Heat.ncrst -r 03_Prod.ncrst -x 03_Prod.nc # MD run
python3 indus_params.py # create plot of P(N) vs N and create ts.txt for WHAM
# create basic analysis files
mkdir Analysis
cd Analysis
$AMBERHOME/bin/process_mdout.perl ../03_Prod.out




