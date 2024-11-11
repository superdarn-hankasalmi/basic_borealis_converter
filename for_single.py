#!/usr/local/bin/python3
# V0.1 Convert single .site data files to both RAWACF and FITACF3
# By Cassie Lakin
# 07/11/2024
import pydarnio
import subprocess
import shutil
from pathlib import Path
import os

INFILE = input("Please Specify the full path of the .site file.\n")
print("thank you kindly.")
OUTFILE = os.path.join(INFILE + ".rawacf")
FITACF = os.path.join(INFILE + ".fitacf3")
pydarnio.BorealisConvert(INFILE, "rawacf", OUTFILE, borealis_file_structure="site")
print("done")
args = "make_fit" " " "-fitacf3" " " "{}" " " ">" " " "{}" .format(OUTFILE, FITACF)
subprocess.call(args, shell=True)
