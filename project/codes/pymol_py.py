import pymolPy3
import pyrotein as pr
import os

pm = pymolPy3.pymolPy3()

drc = 'pdb'
pdb = '3HTB'
pdb_file = f"{pdb}.pdb"
pdb_path = os.path.join(drc, pdb_file)
print(pdb_path)
pm(f"load {pdb_path}")


atoms_pdb = pr.atom.read(pdb_path)
print(atoms_pdb)

input("Press Enter to exit...")
