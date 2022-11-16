from sys import argv

# Set variable as argument define in command line
script, filename = argv

# Filename will be the first argv (you will see what happened when you try to
# run the code)
txt = open(filename)

# print the file
print(f"Here's your file {filename}:")
print(txt.read())

# txt = close(filename)

# reread the file to reread the input vs argv
reread = True
while reread == True:
    print("Type the filename again:")
    file_again = input("> ")

# TODO:
    try:
        txt_again = open(file_again)
        print(txt_again.read())
        reread = False
    except:
        reread = True
