# All Assignments are in : https://elzero.org/python-assignments-lesson-from-79-to-80/

# -1
import datetime

oldDate = datetime.datetime(2021 , 6 , 25)
nowDate = datetime.datetime.now()

print(f"Days From {oldDate} To {nowDate} Is => {(nowDate - oldDate).days}")

# -2
print(oldDate.strftime("%Y-%m-%d"))
print(oldDate.strftime("%b %d, %Y"))
print(oldDate.strftime("%d - %b - %Y"))
print(oldDate.strftime("%d / %b / %y"))
print(oldDate.strftime("%d / %B / %Y"))
print(oldDate.strftime("%A, %d %B %Y"))