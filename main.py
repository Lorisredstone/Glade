import src.py_to_intermediate as pyTi
import src.intermediate_to_c as iTc
import src.intermediate as inter

pyTiconvertor = pyTi.Pytointermediate("input.py")
intermediate_repr = pyTiconvertor.py_to_intermediate()
iTcconvertor = iTc.Intermediatetoc("output.c", intermediate_repr)
iTcconvertor.convert()