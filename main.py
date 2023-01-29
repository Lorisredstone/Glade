import sys

import src.py_to_i.py_to_intermediate as pyTi
import src.i_to_py.intermediate_to_py as iTpy

import mod.inter.interlib as Ilib
import mod.colorprint as colorprint

# get extentions
iext, oext = map(lambda x: x.split(".")[-1], sys.argv[1:])

intermediate_repr:Ilib.Programme|None = Ilib.Programme()
output:str = ""

match iext:
    case "py":
        pyTiconvertor = pyTi.Pytointermediate(sys.argv[1])
        intermediate_repr = pyTiconvertor.py_to_intermediate()
    case _:
        colorprint.colorprint("Error : Input file extention not recognised", color = "red")
        exit(1)
        
match oext:
    case "py":
        iTpyconvertor = iTpy.Intermediatetopy(intermediate_repr)
        output = iTpyconvertor.intermediate_to_py()
    case _:
        colorprint.colorprint("Error : Output file extention not recognised", color = "red")
        exit(1)

with open(sys.argv[2], "w") as f:
    f.write(output)