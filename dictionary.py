#Create a dictionary that includes information about three students 
# The information should include the students name, age, and grade
# Student's info should be in a readable format 

#Create dictionary 

student_dictionary = {
	"name":["Anna","Josh","Kayla"],
	"age": ["15", "15", "14"],
	"grade":["B", "B-","A-"]
}

for i in range(len(student_dictionary["name"])):
    print(f"Name: {student_dictionary['name'][i]}, Age: {student_dictionary['age'][i]}, Grade: {student_dictionary['grade'][i]}")
