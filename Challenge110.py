# ----------*CHALLENGE 110*----------* 
# Using the Names.txt file you created earlier, display the list of names in Python. Ask the user to 
# type in one of the names and then save all the names except the one they entered into a new file called Names2.txt.


file = open("Names.txt", "r")
print(file.read())
file.close()

removeItem = input("Enter the subjetc that  you want to remove: ")
removeItem = removeItem + "\n"

# *********** The solution I found **************:
with open('Names.txt','r') as firstfile, open('Names2.txt','w') as secondfile:
      
    # read content from first file
    for line in firstfile:
        if removeItem != line:       
             # write content to second file
             secondfile.write(line)

# "with" statement in Python is used in exception handling to make the code cleaner and much more readable.
# Notice that unlike the first two implementations, there is no need to call file.close() when using with statement. 
# [resource: GeeksforGeeks]

# *********** The solution of the book *************:
# file = open("Names.txt","r")
# for row in file:
#     if row != removeItem:
#         file = open("Names2.txt","a")
#         newrecord = row
#         file.write(newrecord)
#         file.close()
#     file.close()