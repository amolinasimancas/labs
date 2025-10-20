import time
import datetime

print("Current date and time:")
print(time.asctime(time.localtime()))

print("\nCurrent date and time:")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))