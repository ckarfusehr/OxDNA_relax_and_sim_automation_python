from itertools import product
## Print simple energy vs timesteps for all energy files.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

for file in ["relax1.nrg", "relax2.nrg", "relax3.nrg", "production_run.nrg"]:
    energy = pd.read_csv(file, delimiter="\s+",names=['time', "X",'U','P',"cuda",'K'])
    fig, ax = plt.subplots(4, figsize=(5,20))
    sns.lineplot(data=energy, ax=ax[0], x="time", y="X")
    sns.lineplot(data=energy, ax=ax[1], x="time", y="U")
    sns.lineplot(data=energy, ax=ax[2], x="time", y="P")
    sns.lineplot(data=energy, ax=ax[3], x="time", y="K")
    fig.savefig(f"{file[:-4]}_energy_plot.jpg")
