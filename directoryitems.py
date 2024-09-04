#Create a script that counts the number of items in a specific directory
#Script should display the number of items present in the directory 

import os #The operating system organizes all the files into directory and therefore house existing directories

#Defining the function, naming the function, and then specifying the parameter for the function
def count_items_in_directory(directory_path): 

#Count the number of items in the directory 
    return len(list(os.scandir(directory_path)))

#Take directoy path as a input 
directory = input("Enter the path of the directory:")

#Count the number of items in the directory and output the result 
print(f"Number of items in '{directory}': {count_items_in_directory(directory)}")

