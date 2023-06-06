Author: Christoph Karfusehr, input files provided by Elija Feigl
Date: 14.10.22

This folder can be stored at your local script repository or anywhere else. The following aliase are convenient to quickly start a oxdna simulation in a folder, where the required files are present (min: topology, conformation, opt: forces)
Note that the automatic file detection in the python script is poorly done and that it simply looks for specific file endings.


alias get_oxdna="cp /path/to/this/folder/* ./"
alias start_oxdna="conda activate your_conda_env && python relaxation_and_prod.oxdna.py "
alias do_oxdna="get_oxdna && start_oxdna"
