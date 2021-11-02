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
