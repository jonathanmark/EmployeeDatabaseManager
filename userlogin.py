from datetime import datetime

name = input('Hello dear employee. What is your name?: ')
timeToday = datetime.today().isoformat()

with open('user_database.txt', mode='r+') as database:
    database.write("Employee: " + name + "Login: " + timeToday)

print('Hello ' + name + ' you are now logged in')    