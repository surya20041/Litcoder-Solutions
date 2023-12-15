def convert_to_military_time(time_str):
    # Split the input time into hours, minutes, and seconds
    time_components = time_str[:-2].split(':')
    
    # Extract hours, minutes, and seconds
    hours = int(time_components[0])
    minutes = int(time_components[1])
    seconds = int(time_components[2])
    
    # Check if it's PM and not 12:00:00 PM
    if "PM" in time_str and hours != 12:
        hours += 12
    
    # Check if it's AM and 12:00:00 AM
    if "AM" in time_str and hours == 12:
        hours = 0
    
    # Format the result in 24-hour time
    military_time = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    
    return military_time

# Take user input for the time
user_input = input()

# Call the function to convert the time
converted_time = convert_to_military_time(user_input)

# Print the converted time
print(converted_time)
