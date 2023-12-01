# This program reads a basic HTML page

import urllib.request

url = "http://websites.delta.edu/teklingl/cst173/simple.html"

# Capture web page content in file of string lines
file = urllib.request.urlopen(url)   

# Iterate through lines, clean up, and write
for line in file:
    decodedLine = line.decode("utf-8")  # Extract special characters
    print(decodedLine)
