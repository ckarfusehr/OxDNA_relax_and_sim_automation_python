# OxDNA_relax_and_sim_automation_python
A Python script using OxPy to run OxDNA relaxations and simulations of DNA-Origami or other large objects on a GPU. Also containing the required OxDNA input files.
Author: Christoph Karfusehr, input files provided by Elija Feigl


This folder can be stored at your local script repository or anywhere else. The following aliase are convenient to quickly start a oxdna simulation in a folder, where the required files are present (min: topology, conformation, opt: forces)
Note that the automatic file detection in the python script is poorly done and that it simply looks for specific file endings.


alias get_oxdna="cp /path/to/this/folder/* ./"
alias start_oxdna="conda activate your_conda_env && python relaxation_and_prod.oxdna.py "
alias do_oxdna="get_oxdna && start_oxdna"
