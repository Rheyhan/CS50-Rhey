import os
import sys
import pandas as pd
import numpy as np

if (temp:= len(sys.argv)) <= 2:
    sys.exit("Too few command-line arguments")
elif temp >3:
    sys.exit("Too many command-line arguments")
path=sys.argv[1]
target=sys.argv[2]

try:
    df=pd.read_csv(path)
except:
    sys.exit(f'Could not read {path}')

pd.concat((pd.DataFrame([i.split(", ") for i in df["name"].to_numpy()], columns=["first", "last"]), df["house"]), axis=1).to_csv(target, index=False)