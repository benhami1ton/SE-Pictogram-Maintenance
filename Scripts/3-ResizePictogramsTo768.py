#MenuTitle: 3. Resize to 75% of UPM...
# -*- coding: utf-8 -*-
__doc__="""
Sorts glyphs into portrait, landscape, and square categories. Final output has a 12.5 percent margin around icon, resulting in icons 768 units wide or high.

QUICK START: Double check the path to the EPS files (line 11). Paste into Macro window, run two times.
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
                        			-xOrigin, # x position
                        			-yOrigin  # y position
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
                        			-xOrigin, # x position
                        			-yOrigin  # y position

                        		])
def centerGlyph():
    for glyph in PUAglyphs:
        for layer in glyph:
            xOrigin = layer.bounds.origin.x
			yOrigin = layer.bounds.origin.y
            layer.applyTransform([
                        			1, # x scale factor
                        			0.0, # x skew factor
                        			0.0, # y skew factor
                        			1, # y scale factor
                        			(layer.width - layer.bounds.size.width) // 2, # x position
                        			(layer.width - layer.bounds.size.height) // 2  # y position

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
centerGlyph()
