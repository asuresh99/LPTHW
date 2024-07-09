from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

txt.close()

print ("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())

txt_again.close()

# Receives filename from user.
filename = input("Filename: ")
# Opens file within program.
txt = open(filename)
# Displays title of filename. 
print ("Here's your file %r:" % filename)
# Displays text inside file.
print (txt.read())