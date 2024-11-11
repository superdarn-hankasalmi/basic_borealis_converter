#!/usr/local/bin/python3
# V0.1 Convert .site data to both RAWACF and FITACF3
# By Cassie Lakin
# 07/11/2024
import pydarnio
import subprocess
import shutil
from pathlib import Path
import os

#INFILE = input("Please Specify the directory of the rawacf.site data?\n")
INFILE = ("/home/hankasalmi/radar_data/BOREALIS/")

for file in os.listdir(INFILE):
    if file.endswith(".site"):
        final = os.path.join(INFILE, file)
        P = Path(file)
        ALTERED = P.stem
        OUTFILE = os.path.join(INFILE, ALTERED + ".rawacf")
        pydarnio.BorealisConvert(final, "rawacf", OUTFILE, borealis_file_structure="site")
        shutil.move(OUTFILE, "/home/hankasalmi/radar_data/RAWACF")
        r = subprocess.call("/home/hankasalmi/data_env/python_scripts/convert.sh")

"""This file works for multiple files being converted, I deally this needs to be a scheduled event to batch convert 
all the files that will be coming from the radar in finland. The RAWACF to FITACF will convert all .RAWACF files"""



