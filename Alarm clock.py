# Running pip install command to download datetime & playsound modules
# Importing required these modules 
from datetime import datetime
from playsound import playsound
# Saving the alarm_time variable by using a standard time format for hour, minute, second and period
alarm_time = input("Enter the alarm time in 'HH:MM:SS AM/PM' format: ")
# Using a slicing operator to access the first two characters of user input
# The input is not more than 12 hours then the execution will move forward to the next conditional statement. 
# If the input is more than 12 hours, then it will return a statement asking the user to re-enter the time.
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time [3:5]
alarm_second = alarm_time [6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm!")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
# Using if statement to compare current time and user time
# When the user and current period(AM/PM) matches, the next if statement will be excuted 
# Finally, when the last if statement is matched and "It's time for waking up!" will be printed and the alarm tone will be played
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_second:
                    print("It's time for waking up!")
                    playsound('C:\\Users\\Engineer_2022\\Desktop\\Project-2022\\Day-projects\\repos\\100Python_projects\\Drum.wav')
                    break