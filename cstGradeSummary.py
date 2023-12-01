# This program performs a summary of recent CST course grades

datafile = open("cstGrades.txt", "r") # Open file

totalStudents = 0
aCount        = 0  
successCount  = 0      

# Perform file processing loop until end
for gradeAveData in datafile:
    
    gradeAve = float(gradeAveData)    # Read average
    
    if gradeAve >= 0.90:              # Count A-level grades
        aCount += 1

    if gradeAve >= 0.73:              # Count successful students
        successCount += 1

    totalStudents += 1                # Counter for total students

# Calculate and display summary data.  Convert data to percentage.

aGradePct = float(aCount) / float(totalStudents) * 100
print("Percentage A-Level Grades:")
print("%5.0f" % (aGradePct),"percent")

successRate = float(successCount) / float(totalStudents) * 100
print("Success rate:")
print("%5.0f" % (successRate),"percent")
