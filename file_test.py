import os
import pydarnio
import pandas
folder_path = "/home/hankasalmi/radar_data/BOREALIS/"

for file in os.listdir(folder_path):
    if file.endswith(".site"):
        with open(os.path.join(folder_path, file)) as f:

            print(file)
