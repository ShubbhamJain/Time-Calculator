def add_time(start, duration, startDay = ''):
  new_time = ''

  startTime = start.split(' ')

  startTimeHours, startTimeMins = startTime[0].split(':')
  timeType = startTime[1]
  timeTypeInitial = True

  startTimeHours = int(startTimeHours)
  startTimeMins = int(startTimeMins)

#   print(13, startTimeHours, timeTypeInitial)
  if (timeType == 'PM'):
    startTimeHours = startTimeHours + 12
    timeTypeInitial = not timeTypeInitial
#   print(17, startTimeHours, timeTypeInitial)

  durationHours, durationMins = duration.split(':')

  newHours = startTimeHours + int(durationHours)
  newMins = startTimeMins + int(durationMins)

  if (newMins > 60 and newMins % 60 > 0):
    newHours = newHours + int(newMins / 60)
    newMins = newMins - 60
    timeTypeInitial = not timeTypeInitial

  daysCount = 0
  daysStr = ''

  if (newHours > 12 and newHours <= 24):
    newHours -= 12
  elif (newHours > 24):
    daysCount = int(newHours / 24)
    newHours = newHours - daysCount * 24

    if (newHours == 0): newHours = 12

    if (daysCount == 1):
        daysStr = f'(next day)'
    else:
        daysStr = f'({daysCount} days later)'

  if (len(str(newMins)) == 1):
    newMins = '0' + str(newMins)

  if (timeTypeInitial):
    timeType = 'AM'
  else:
    timeType = 'PM'

  if (startDay):
    new_time = f'{newHours}:{newMins} {timeType} {daysStr}'
  else:
    new_time = f'{newHours}:{newMins} {timeType}'
  return new_time

print(add_time("11:06 PM", "2:02"))
print(add_time("11:55 AM", "3:12"))
print(add_time("8:16 PM", "466:02"))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("9:15 PM", "5:30"))
print(add_time("5:01 AM", "0:00"))
print(add_time("11:40 AM", "0:25"))
print(add_time("3:30 PM", "2:12"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM ", "24:00"))
print(add_time("2:59 AM ", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
