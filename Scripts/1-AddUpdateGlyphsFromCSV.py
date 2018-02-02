#MenuTitle: 1. Add/Update Glyphs From Pictogram CSV...
# -*- coding: utf-8 -*-
__doc__="""
References CSV to match unicode values to Glyphs app. If missing from Glyphs, new glyph objects are added with missing unicode values. If names differ from CSV list, names are updated.

QUICK START: Double check the path to the CSV file (line 18) and the name of the CSV file (line 30). No need to select any glyphs when running this script.
"""
# Import modules needed to run script
import os, csv, GlyphsApp

# Clears Macro panel printout. Comment this out to keep each iteration of script run.
Glyphs.clearLog()

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory to location of CSV file
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.4/CSV/"))

# Create a dictionary to store the new names
newNames = {}

# Assign each unicode as the key and the new name as the value
def GetUpdatedNames():
    for line in csv_reader:
        if line[-2]:
            newNames[line[0]] = line[-2]

# Open Pictogram CSV file and check for new entries
with open('SE-Pictogram-Maintenance-0.4.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip header information
    next(csv_reader)
    GetUpdatedNames()

# Create list of Unicode values already present in Glyphs App
unicodeChecker = []
for glyph in Glyphs.font.glyphs:
	unicodeChecker.append(str(glyph.unicode))

# Compare the unicode values in the CSV file to the Glyphs file, if there's
# a new unicode value then add it to the Glyphs file. Sets the
# newPictograms checker variable to true.
def createNewPictograms():
	newPictograms = False
	for key, val in newNames.items():
		if key in unicodeChecker:
			pass
		else:
			newGlyph = Glyphs.font.glyphs['E700'].copy()
			newGlyph.name = val
			newGlyph.setUnicode_(key)
			Font.glyphs.append(newGlyph)
			newPictograms = True
			print(key + " doesn't exist already, new glyph made.")
	# Prints to inform you that nothing changed.
	if newPictograms == False:
		print("No new pictograms were added.")



# Compare the unicode values in the CSV file to the Glyphs file, if there's
# an updated name, change glyphs name. Sets the nameChanged
# checker variable to true.
def renameExistingPictograms():
	nameChanged = False
	for key, val in newNames.items():
		for glyph in Glyphs.font.glyphs:
			if glyph.unicode == key:
				if glyph.name != val:
					glyph.name = val
					nameChanged = True
					print(str(glyph.unicode) + ' has become ' + str(glyph.name))

    # Prints to inform you that nothing changed.
	if nameChanged == False:
		print("No names were altered.")

createNewPictograms()
print("\n" + "------------------------------" + "\n")
renameExistingPictograms()
