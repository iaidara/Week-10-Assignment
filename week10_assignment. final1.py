import os

directory_list = (os.listdir())
#Print current directory
print(os.listdir())
# promt user to enter a directory name
select_directory = input("Please choose a directory name: ")
# Prompt user to enter a file name
file_name = input("Enter the file name: ")
os.makedirs(select_directory)
completeName = os.path.join(select_directory, file_name+".txt") 

#User attrivutes
name = input("Please enter your name: ") 
phone_number = input("Please enter your phone number: ") 
adress = input("Please enter your adress: ") 

file_name = f"{file_name}.txt"
while input != 'quit':
    with open (completeName, 'a') as file_object:
        file_object.write(f"Name: {name}.\n")
        file_object.write(f"Phone number: {phone_number}.\n")
        file_object.write(f"Adress: {adress}.\n")
    prompt = input("\nWould you like to enter more information (Yes or NO): ").title() 
    if prompt == 'No':
        break
    else:
        name = input("\nPlease enter your name: ") 
        phone_number = input("Please enter your phone number: ") 
        adress = input("Please enter your adress: ")
   

    #prompt = input("Why do you like programming: ") 
  
