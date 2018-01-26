#MenuTitle: 2. Rename Glyphs from Pictogram CSV...
# -*- coding: utf-8 -*-
__doc__="""
References CSV to match unicode values to Glyphs app. If there's a match, update name to most recent name.

QUICK START: Double check the path to the CSV file (line 15) and the name of the CSV file (line 33). No need to select any glyphs when runnign this script.
"""
# Import modules needed to run script
import os, csv, GlyphsApp

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.3/CSV/"))

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
with open('SE-Pictogram-Maintenance-0.3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip header information
    next(csv_reader)
    GetUpdatedNames()

# Compare the unicode values in the CSV file to the Glyphs file, if the
# unicode values match, then make the names equal as well.
for key, val in newNames.items():
  for glyph in Glyphs.font.glyphs:
		if glyph.unicode == key:
			glyph.name = val
			print(str(glyph.unicode) + ' has become ' + str(glyph.name))
		else:
			print(str(glyph.unicode) + ' is unchanged')
