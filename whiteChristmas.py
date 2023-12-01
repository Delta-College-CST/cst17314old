# This program reads a large file of weather data observed at your
# instructor's home.  From the data, determine the percentage of years
# with a white Christmas (determined if snow on ground 12/24 for a given year).
# File format:
# {year} {mon} {day} {loTemp} {hiTemp} {precip} {snow} {snowGrnd} {tStorm}

totalDays = 0.0
snowDays  = 0.0

wxfile = open("tkHomeWeather.txt", "r") # Open file for reading

for inputdataline in wxfile:

    # Read, clean, and spit input line into list elements
    inputdataline = inputdataline.strip()      
    datalinelist  = inputdataline.split(",")

    # Extract data tokens from line
    month  = int(datalinelist[1])
    day    = int(datalinelist[2])
    snow   = float(datalinelist[7])

    # For Christmas Eve, determine if snow on ground
    if day == 24 and month == 12:
        totalDays = totalDays + 1

        if snow > 0.0:
            snowDays = snowDays + 1

# Summarize:  Determine percentage - White Christmas
whiteChristmasPct = float(snowDays) / float(totalDays) * 100.0;

# Output
print()
        
print("White Christmas at Home: %5.1f pct" % (whiteChristmasPct))
