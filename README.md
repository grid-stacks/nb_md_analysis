# Jupyter Notebook MD Analysis

This project illustrates the simulation protein in complex with a ligand with jupyter notebook. We will analyze T4 lysozyme L99A/M102Q protein (PDB code 3HTB), in complex with the 2-propylphenol small molecule (Code JZ4).

## Create New Environment

`conda env create -f .conda_env/nb_md_analysis.yml`

`conda activate nb_md_analysis`

`jupyter-nbextension enable --py --user widgetsnbextension`

`jupyter-nbextension enable --py --user nglview`

## Start Coding

`conda activate nb_md_analysis`

`jupyter-notebook project/notebooks/protein_ligand_complex_analysis.ipynb`

## Output files

Important Output files generated:

- 3HTB_JZ4_md.gro: Final structure (snapshot) of the MD setup protocol.
- 3HTB_JZ4_md.trr: Final trajectory of the MD setup protocol.
- 3HTB_JZ4_md.cpt: Final checkpoint file, with information about the state of the simulation. It can be used to restart or continue a MD simulation.
- 3HTB_JZ4_gppmd.tpr: Final tpr file, GROMACS portable binary run input file. This file contains the starting structure of the MD setup free MD simulation step, together with the molecular topology and all the simulation parameters. It can be used to extend the simulation.
- 3HTB_JZ4_genion_top.zip: Final topology of the MD system. It is a compressed zip file including a topology file (.top) and a set of auxiliar include topology files (.itp).

## Analysis (MD setup check) output files generated

- 3HTB_JZ4_rms_first.xvg: Root Mean Square deviation (RMSd) against minimized and equilibrated structure of the final free MD run step.
- 3HTB_JZ4_rms_exp.xvg: Root Mean Square deviation (RMSd) against experimental structure of the final free MD run step.
- 3HTB_JZ4_rgyr.xvg: Radius of Gyration of the final free MD run step of the setup pipeline.

## Amber update time-to-time

`conda update -c conda-forge ambertools`