# This program reads a large file of weather data observed at your
# instructor's home.  Given a valid date defined by the user, it determines
# the average high and low temperature for that date.
# File format:
# {year} {mon} {day} {loTemp} {hiTemp} {precip} {snow} {snowGrnd} {tStorm}

wxfile = open("tkHomeWeather.txt", "r") # Open file for reading

# Get user date request
targetMon = int(input("Enter month: "))
targetDay = int(input("Enter day: "))

totDays = 0
loTotal = 0
hiTotal = 0

# Read and capture input file
for inputdataline in wxfile:

    # Read, clean, and spit input line into list elements
    inputdataline = inputdataline.strip()        
    datalinelist  = inputdataline.split(",")

    # Extract data tokens from line
    year   = int(datalinelist[0])
    month  = int(datalinelist[1])
    day    = int(datalinelist[2])
    hiTemp = float(datalinelist[3])
    loTemp = float(datalinelist[4])

    # If date matches user target, accumulate & count for averaing
    if month == targetMon and day == targetDay:
        loTotal += loTemp
        hiTotal += hiTemp
        totDays += 1    # Count number of days for averaging
        
# Calcualate averages and summarize
aveLo = loTotal / totDays
aveHi = hiTotal / totDays

print()
print("For ",targetMon,"/",targetDay,": ")
print("  Average high temperature: %5.1f deg F" % (aveHi))
print("  Average low temperature: %5.1f deg F" % (aveLo))

