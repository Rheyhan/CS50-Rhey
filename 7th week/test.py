import sys
import os

if (counter:=len(sys.argv)) ==1:
    sys.exit("Too few command-line arguments")
elif counter>2:
    sys.exit("Too many command-line arguments")

path=sys.argv[1]
if not os.path.exists(path):
    sys.exit("File does not exist")
if not path.split(".")[-1]=="py":
    sys.exit("Not a Python file")

with open(path, "r") as fh:
    asu=fh.read()
    print(len([i for i in asu.replace(" ", "").split("\n") if len(i)>0 and not i.startswith("#")]))