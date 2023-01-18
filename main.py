import src.convert

python_file = open("input.py", "r")
python_code = python_file.read() # Read the file
convertissor = src.convert.Convertiseur(python_code, True) # Convert the code
convertissor.run() # Get the converted code
c_code = convertissor.code_c # Get the converted code
with open("out\\output.c", "w") as c_file:
    c_file.write(c_code) # Write the converted code to a file
print("Done!")