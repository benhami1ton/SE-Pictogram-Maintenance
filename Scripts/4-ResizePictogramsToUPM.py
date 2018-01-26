#MenuTitle: 3. Import New EPS Outlines...
# -*- coding: utf-8 -*-
__doc__="""
Clear any leftover pictograms/ test paths in any glyphs that have a matching EPS file. Find EPS files in designated folder, move them to the Import folder, then open the Import Outlines dialog to allow user to import outlines

QUICK START: Double check the path to the EPS files (line 11). Only select/resize glyphs with a unicode of E700 or higher.
"""
import os, GlyphsApp, shutil

# Change directory to location of Import folder
os.chdir("~/Downloads/SE-Pictogram-Maintenance-0.1/EPS/Import/")

currentDir = os.getcwd()
completedDir = "Completed"
thisEPSnewPath = ""

myLayers = Glyphs.font.selectedLayers # current layer

def scaleToUPM():
	for thisLayer in myLayers:
		print (thisLayer.parent.name + ' scaled by factor of ' + str(thisLayer.width / thisLayer.bounds.size.width))
		thisLayer.applyTransform([
                        		thisLayer.width / thisLayer.bounds.size.width, # x scale factor
                        		0.0, # x skew factor
                        		0.0, # y skew factor
                        		thisLayer.width / thisLayer.bounds.size.width, # y scale factor
                        		0.0, # x position
                        		0.0  # y position
                        	])

# Creates new directory for the selected glyph, so Glyphs.app can find and grab it
def moveToCompletedDir():
	thisImportEPSoldPath = str(currentDir + '/' + thisEPSfile)
	thisImportEPSnewPath = str(currentDir + '/' + completedDir + '/' + thisEPSfile)
	if not os.path.exists(completedDir):
		os.makedirs(completedDir)
	shutil.move(thisImportEPSoldPath, thisImportEPSnewPath)
	print "%s Moved into Completed directory." % thisLayer.parent.name


# Loop through selected glyphs, to check if there's a new glyph. If there is, it deletes
# the paths of the selected glyph, imports the new ones, resizes them to the UPM.
for thisLayer in myLayers:
    thisEPSfile = "%s.eps" % (thisLayer.parent.name)
    if os.path.exists(thisEPSfile):
    	moveToCompletedDir()
    	scaleToUPM()
#     	print (thisLayer.parent.name + ' was updated. \n')
    else:
    	print (thisLayer.parent.name + ' was not affected. \n')
