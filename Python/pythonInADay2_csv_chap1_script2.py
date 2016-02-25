import os, csv

# The path to the script
currentPath = os.path.dirname(os.path.abspath("_file_"))

# Make the spreadsheet path
inputCsv = currentPath + '/spreadsheet.csv'

# Open file in read mode
csvFile = open(inputCsv, "rb")

# Create reader object
reader = csv.reader(csvFile, delimiter=',')

# Print out data in file
for row in reader:
    print row

# Add data to array
readerData = []
for row in reader:
    readerData.append(row)

print readerData 
