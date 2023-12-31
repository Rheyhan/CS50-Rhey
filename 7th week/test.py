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
    
first=[]
last=[]
for i in df["name"].to_numpy():
    temp = i.split(", ")
    first.append(temp[1])
    last.append(temp[0])
    
pd.DataFrame(list(zip(first, last, df["house"].to_numpy())), columns=["first", "last", "house"]).to_csv(target, index=False)