#MenuTitle: 1. Add New Glyphs From Pictogram CSV...
# -*- coding: utf-8 -*-
__doc__="""
References CSV to match unicode values to Glyphs app. If missing from Glyphs, new glyph objects are added with missing unicode values.

QUICK START: Double check the path to the CSV file (line 15) and the name of the CSV file (line 33). No need to select any glyphs when runnign this script.
"""
# Import modules needed to run script
import os, csv, GlyphsApp

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory to location of CSV file
os.chdir("~/Downloads/SE-Pictogram-Maintenance-0.1/CSV/")

# List all files and directories in current directory
os.listdir('.')

# Create a dictionary to store the new names
newNames = {}

# Assign each unicode as the key and the new name as the value
def GetUpdatedNames():
    for line in csv_reader:
        if line[-2]:
            newNames[line[0]] = line[-2]
            print(line[1] + ' has been renamed to ' + line[-2])
        else:
            print(line[0] + ' was not changed.')

# Open Pictogram CSV file and check for new entries
with open('SE-Pictogram-Maintenance-0.1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip header information
    next(csv_reader)
    GetUpdatedNames()

# Create list of Unicode values already present in Glyphs App
unicodeChecker = []
for glyph in Glyphs.font.glyphs:
	unicodeChecker.append(str(glyph.unicode))


# Compare the unicode values in the CSV file to the Glyphs file, if there's
# a new unicode value then add it to the Glyphs file.
for key, val in newNames.items():
	if key in unicodeChecker:
		print(key + ' exists already')
	else:
		newGlyph = Glyphs.font.glyphs['E700'].copy()
		newGlyph.name = val
		newGlyph.unicode = key
		Font.glyphs.append(newGlyph)
		print(key + " doesn't exist already, new glyph made")
