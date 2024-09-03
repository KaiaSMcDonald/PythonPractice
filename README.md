#Create a script that counts the number of items in a specific directory
#Script should display the number of items present in the directory 

import os #The operating system organizes all the files into directory and therefore house existing directories

current_directory = os.getcwd()
print (current_directory) #prints out the absolute path of the current directory 

count = 0 
dir_path = 'C:/home/ubuntu/pythonpractice'

for elements in os.listdir(dir_path)
