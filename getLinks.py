# This program reads an HTML page containing multiple links
# It extracts the list, adds them to a list, and the writes them.
# Then, it seeks the links that are related to the U.S. Govt.

import urllib.request

url = "http://websites.delta.edu/teklingl/psc103w/climateResources.html"

urlList = []  # List of all URLs found

file = urllib.request.urlopen(url)

for aLine in file:
    aLine = aLine.decode("utf-8")

    # If the "href" HTML tag is in the line, it contains a link
    if "href" in aLine:
        
        # Mark beginning and end of link URL
        start = aLine.find("href") + 6
        end   = aLine.find("\">",start)

        # Extract link as substring
        link = aLine[start : end]   

        # Add link to web page list
        urlList.append(link)

# Write U.S. Govt links to output
for aLink in urlList:
    if ".gov" in aLink:
        print(aLink)
