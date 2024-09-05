# Write a Python function that calculates the uptime percentage of a service
# It must be based on the total number of hours and the number of hours the service was down.
# The function should take 2 parameters(total hours and down hours, inputted when the function is run)
# the function should return the uptime percentage rounded to two decimal places. 

# Define the function and add the two parameters 
def calculate_uptime(total_hours, down_hours):
    if total_hours <= 0 or down_hours > total_hours: #Total hours must be greater than 0, and down hours must be between 0 and total hours


# Create a variable for uptime_hours and uptime_percentage
uptime_hours = total_hours - down_hours
uptime_percentage = (uptime_hours/total_hours) * 100 
return round(uptime_percentage, 2) #This will round uptime percentage to two decimal places


total_hours= 5 
down_hours = 2
print(f"Uptime percentage: {uptime}%")
