#MenuTitle: 1. Add/Update Glyphs From Pictogram CSV...
# -*- coding: utf-8 -*-
__doc__="""
References the selected CSV to match unicode values to Glyphs app. If missing from Glyphs, new glyph objects are added with missing unicode values. If names differ from CSV list, names are updated.
"""
# Import modules needed to run script
import os, errno, shutil, GlyphsApp, time, csv

# Clears Macro panel printout. Comment this out to keep each iteration of script run.
Glyphs.clearLog()

chooseCSV = GetOpenFile(message=None, allowsMultipleSelection=False, filetypes=["csv"])

# Change directory to location of CSV file
# os.chdir(chooseCSV)

# Create a dictionary to store the new names
newNames = {}

# Assign each unicode as the key and the new name as the value
def GetUpdatedNames():
    for line in csv_reader:
        if line[-2]:
            newNames[line[0]] = line[-2]

    # This should catch duplicates.
    rev_newNames = {}
    for key, value in newNames.items():
    	rev_newNames.setdefault(value, set()).add(key)
    if [values for key, values in rev_newNames.items() if len(values) > 1]:
    	print ("The following unicode values have the same name:\n" + str([values for key, values in rev_newNames.items() if len(values) > 1]))

# Open Pictogram CSV file and check for new entries
with open(chooseCSV, 'r') as csv_file:
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
			newGlyph.color = 9
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
					glyph.color = 9
					nameChanged = True
					print(str(glyph.unicode) + ' has become ' + str(glyph.name))

    # Prints to inform you that nothing changed.
	if nameChanged == False:
		print("No names were altered.")

try:
	renameExistingPictograms()
	print("\n" + "------------------------------" + "\n")
	createNewPictograms()
except NameError as e:
	print ("\nImmediate reason script has stopped: " + str(e))
	time.sleep(2)
	Message(str(e) + " Two glyphs with different unicode values cannot share the same name. Check source files for duplicates and try running the script again. Duplicates need to be removed or renamed.", "Script unable to continue." , OKButton=None)
