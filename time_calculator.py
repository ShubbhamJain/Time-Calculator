def add_time(start, duration, startDay=""):
    new_time = ""

    numOfDay = 0
    listOfDays = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    if startDay:
        dayParam = str(startDay).lower()
        if dayParam in listOfDays:
            numOfDay = listOfDays.index(dayParam)

    startTime = start.split(" ")
    startTimeHours, startTimeMins = startTime[0].split(":")
    timeType = startTime[1]
    durationHours, durationMins = duration.split(":")

    timeTypeInitial = True
    listOfTimeType = ["AM", "PM"]

    if listOfTimeType[0] == timeType:
        timeTypeInitial = True
    elif listOfTimeType[1] == timeType:
        timeTypeInitial = False

    newHours = int(startTimeHours) + int(durationHours)
    newMins = int(startTimeMins) + int(durationMins)

    if timeType == listOfTimeType[1]:
        newHours += 12

    if newMins >= 60:
        newHours = newHours + int(newMins / 60)
        newMins = newMins - 60

    daysCount = 0
    daysStr = ""

    if newHours % 24 == 12:
        timeTypeInitial = False
    elif newHours % 24 >= 12:
        timeTypeInitial = False
    else:
        timeTypeInitial = True

    # it shows that we are in the same day
    if newHours > 12 and newHours <= 24:
        newHours -= 12

    # it shows that we are not in the same day, we are past that day
    elif newHours > 24:
        daysCount = int(newHours / 24)

        newHours = newHours - daysCount * 24

        if newHours == 0:
            newHours = 12

        if daysCount == 1:
            daysStr = f"(next day)"
            numOfDay += 1
        else:
            daysStr = f"({daysCount} days later)"

            for i in range(daysCount):
                numOfDay += 1
                if numOfDay == len(listOfDays) and i <= daysCount:
                    numOfDay = 0

    if len(str(newMins)) == 1:
        newMins = "0" + str(newMins)

    if timeTypeInitial:
        timeType = listOfTimeType[0]
    else:
        timeType = listOfTimeType[1]

    if startDay:
        new_time = (
            f"{newHours}:{newMins} {timeType}, {listOfDays[numOfDay].capitalize()}"
        )
    else:
        new_time = f"{newHours}:{newMins} {timeType}"

    if daysStr:
        new_time += f" {daysStr}"

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
