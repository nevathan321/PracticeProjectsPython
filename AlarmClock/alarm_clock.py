from playsound import playsound
import time

#playsound("alarm.mp3")
#02d a cool formatting tool in python, make its in format 00:00 rather than 0:0 


CLEAR = "\033[2j"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0 


    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed 
        minutes_left = time_left // 60 
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN} Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") 

    playsound("alarm.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes*60+ seconds
alarm(total_seconds) 