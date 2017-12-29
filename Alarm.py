import time
import os
import threading


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = init(hours)
        self.minutes = init(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW")
                    os.popen("voltage.mp3")
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False


username = input("Enter your name: ")
print("Hello, " + username)

alarm_hours = input("Enter the hours you want to wake up at: ")
alarm_minutes = input("Enter the minutes you want to wake up at: ")
print("Your alarm is set for: {0:02}:{1:02}").format(alarm_hours, alarm_minutes)


alarm = Alarm(alarm_hours, alarm_minutes)
alarm.start()

try:
    while True:
        text = str(raw_input())
        if text == "stop":
            alarm.just_die()
            break
except:
    print("Yikes lets get out of here")
    alarm.just_die()

