# ----------*CHALLENGE 108*----------* 
# Open the Names.txt file. Ask the user to input a new name. 
# Add this to the end of the file and display the entire file.

file = open("Names.txt", "a")

newName = input("Enter a new name: ")

file.write("\n")
file.write(newName)
file.close()

file = open("Names.txt", "r")
print(file.read())
