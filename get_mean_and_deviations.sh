## conda environment OxDNA must be activated

oat mean -p 20 -o production_run_mean.trj.dat production_run.trj.dat
oat deviations -p 20 -o production_run_deviations.trj.dat production_run_mean.trj.dat production_run.trj.dat
oat align -p 20 -r production_run_mean.trj.dat production_run.trj.dat production_run_aligned_to_mean.trj.dat
python $tacoxdna/oxDNA_PDB.py *.top production_run_mean.trj.dat 53 -H false -u --rmsf-file production_run_deviations.trj.dat.json
