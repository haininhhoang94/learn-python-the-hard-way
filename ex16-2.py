from sys import argv

# Set variable as argument define in the command line
script, filename = argv

# Filename will be the first argv (you will see what happened when you try to run the code

txt = open(filename)

# print the file
print(f"Read the test file to test if {filename} is working or not:")
print(txt.read())

txt.close()
