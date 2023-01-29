import src.py_to_i.py_to_intermediate as pyTi

pyTiconvertor = pyTi.Pytointermediate("input.py")
intermediate_repr = pyTiconvertor.py_to_intermediate()
print(intermediate_repr.dict())