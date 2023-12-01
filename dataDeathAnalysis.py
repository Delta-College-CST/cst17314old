# This program analyzes raw spreadsheet data to determine
# patterns in mortality data.  Dataset includes monthly death counts
# due to various factors for 2014-2019.

# Specific questions to answer include:
#     1) How many people died each year by auto accident?
#     2) What was the overall percentage of deaths by heart disease and cancer combined?

# Relevant position numbers (as zero-based indexes)
#  [1] year    [2] month

# Utilize parallel lists for data extraction and storage
yearList   = []
monthList  = []
totalList  = []
cancerList = []
heartList  = []
autoList   = []
totalMonths = 0

# Load data from file
datafile = open("MonthlyDeathCauses1419.csv", "r")

firstLine = datafile.readline()   # Discard first header line

for inputStrItem in datafile:
    inputLineArr = inputStrItem.split(",")

    # Extract data tokens from current line and add to end lists.  Convert
    # all data to integers.
    yearList.append(int(inputLineArr[1]))
    monthList.append(int(inputLineArr[2]))
    totalList.append(int(inputLineArr[3]))
    cancerList.append(int(inputLineArr[6]))
    heartList.append(int(inputLineArr[14]))
    autoList.append(int(inputLineArr[17]))

    totalMonths += 1   # Add to counter for number of months

# ------------------------------------------------------------------------------ #
# Analysis 1:  How many people died each year by auto accident?

totals = {2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0 }  # Dictionary for counting

print()
print("Deaths By Auto Accident")
for year in range(2014, 2020):   # Loop year 2014 - 2016
    for i in range(totalMonths):    # For each month, loop through dataset
        if yearList[i] == year:
            totals[year] += autoList[i]
    print(year,"-->",totals[year])


# ------------------------------------------------------------------------------ #
# Analysis 2:  What was the overall percentage of deaths by heart disease and cancer combined?

totalCancerHeart = 0
totalDeaths = 0


print()
print("Percentage of Deaths by Cancer and Heart Disease Combined")

for i in range(totalMonths):    # Loop through dataset; perform summations
    totalDeaths += totalList[i]
    totalCancerHeart += (cancerList[i] + heartList[i])

# Calculate target pewrcentages
targetPct = float(totalCancerHeart) / float(totalDeaths) * 100
print("Pct of cancer and heart disease deaths: %5.1f pct" % (targetPct))

