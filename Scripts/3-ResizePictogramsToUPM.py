#MenuTitle: 3. Import New EPS Outlines...
# -*- coding: utf-8 -*-
__doc__="""
Clear any leftover pictograms/ test paths in any glyphs that have a matching EPS file. Find EPS files in designated folder, move them to the Import folder, then open the Import Outlines dialog to allow user to import outlines

QUICK START: Double check the path to the EPS files (line 11). Only select/resize glyphs with a unicode of E700 or higher.
"""
import os, GlyphsApp, shutil

# Change directory to location of Import folder
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.4/EPS/Import/"))

currentDir = os.getcwd()
completedDir = "Completed"
thisEPSnewPath = ""
PUAglyphs = []
xMax = []
yMax = []
sameMax = []

for myFont in Glyphs.fonts:
    for myGlyph in myFont.glyphs:
        if myGlyph.category == "Private Use":
        	PUAglyphs.append(myGlyph)
    print "PUAglyphs collected."

for eachGlyph in PUAglyphs:
	for layer in eachGlyph.layers:
		if layer.bounds.size.width > layer.bounds.size.height:
			xMax.append(eachGlyph)
			# print (eachGlyph.name + " is wide.")
		if layer.bounds.size.width < layer.bounds.size.height:
			yMax.append(eachGlyph)
			# print (eachGlyph.name + " is tall.")
		if layer.bounds.size.width == layer.bounds.size.height:
			sameMax.append(eachGlyph)
			# print (eachGlyph.name + " is square.")
		if eachGlyph.name in xMax or yMax or sameMax:
			pass
		else:
			print (eachGlyph.name + "-----ERROR-----")

def scaleToWidth():
	# These two lists can be combined to simplify the loop.
	widthPriority = xMax + sameMax

	for glyph in widthPriority:
		for layer in glyph.layers:
			print (layer.parent.name + " | " + layer.name + ' scaled by factor of ' + str((1024 * 0.75) / layer.bounds.size.width))
			xOrigin = layer.bounds.origin.x
			yOrigin = layer.bounds.origin.y
			layer.applyTransform([
                        			(1024 * 0.75) / layer.bounds.size.width, # x scale factor
                        			0.0, # x skew factor
                        			0.0, # y skew factor
                        			(1024 * 0.75) / layer.bounds.size.width, # y scale factor
                        			0, # x position
                        			0  # y position
                        		])
def scaleToHeight():
	for glyph in yMax:
		for layer in glyph.layers:
			print (layer.parent.name + " | " + layer.name + ' scaled by factor of ' + str((1024 * 0.75) / layer.bounds.size.height))
			xOrigin = layer.bounds.origin.x
			yOrigin = layer.bounds.origin.y
			layer.applyTransform([
                        			(1024 * 0.75) / layer.bounds.size.height, # x scale factor
                        			0.0, # x skew factor
                        			0.0, # y skew factor
                        			(1024 * 0.75) / layer.bounds.size.height, # y scale factor
                        			0, # x position
                        			0  # y position

                        		])


# Creates new directory for the selected glyph, so Glyphs.app can find and grab it
def moveToCompletedDir():
	thisImportEPSoldPath = str(currentDir + '/' + thisEPSfile)
	thisImportEPSnewPath = str(currentDir + '/' + completedDir + '/' + thisEPSfile)
	if not os.path.exists(completedDir):
		os.makedirs(completedDir)
	shutil.move(thisImportEPSoldPath, thisImportEPSnewPath)
	print "%s moved into Completed directory." % thisGlyph.name


# Loop through selected glyphs, to check if there's a new glyph. If there is, it deletes
# the paths of the selected glyph, imports the new ones, resizes them to the UPM.
for thisGlyph in PUAglyphs:
    thisEPSfile = "%s.eps" % (thisGlyph.name)
    if os.path.exists(thisEPSfile):
    	moveToCompletedDir()
    	print (thisGlyph.name + ' was updated. \n')

scaleToWidth()
scaleToHeight()
