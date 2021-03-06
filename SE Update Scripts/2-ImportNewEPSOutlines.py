#MenuTitle: 2. Import New EPS Outlines...
# -*- coding: utf-8 -*-
__doc__="""
Chooses EPS folder location.
Clear any leftover pictograms/ test paths in any glyphs
that have a matching EPS file. Find EPS files in designated
folder, move them to the Import folder, then open the
Import Outlines dialog to allow user to import outlines.

"""
import os, errno, shutil, GlyphsApp, subprocess, time
from subprocess import Popen, PIPE

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Ask for location of EPS folder
getEPSdir = GetFolder(message=None, allowsMultipleSelection = False)

# Change directory to location of EPS folder
os.chdir(getEPSdir)


currentDir = os.getcwd()

myLayers = Glyphs.font.selectedLayers
thisEPSnewPath = ""
ImportDir = '_Ready For Import'
importDirString = '\"' + currentDir + '/' + ImportDir + '/' + '\"'


# Creates new directory for the selected glyph, so Glyphs.app can find and grab it
def moveToImportDir():
	thisEPSoldPath = str(currentDir + '/' + thisEPSfile)
	thisEPSnewPathinImport = str(currentDir + '/' + ImportDir + '/' + thisEPSfile)
	if not os.path.exists(ImportDir):
		os.makedirs(ImportDir)
	shutil.move(thisEPSoldPath, thisEPSnewPathinImport)
	print "%s Moved into Import directory." % thisLayer.parent.name



# Removes paths in selected glyph
def removeGlyphPaths():
	Font = Glyphs.font
	selectedLayers = Font.selectedLayers
	def process( thisLayer ):
		thisLayer.parent.beginUndo()
		for i in range( len( thisLayer.paths ))[::-1]:
			del thisLayer.paths[i]
		thisLayer.parent.endUndo()
	Font.disableUpdateInterface()

	print "Clearing %s." % thisLayer.parent.name
	process( thisLayer )

	Font.enableUpdateInterface()

# Use AppleScript to interact with the Mac's GUI and go to the location of imported Glyphs.
def runascript():
	ascript = """
		tell application "System Events"
			keystroke "i" using {command down, shift down}
			delay 1
			keystroke "g" using {command down, shift down}
			delay 0.5
			keystroke """ + importDirString + """
			delay 2
			keystroke return

		end tell
		"""
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(ascript)
	print (p.returncode, stdout, stderr)

# Loop through selected glyphs, to check if there's a new glyph. If there is, it deletes
# the paths of the selected glyph, imports the new ones, resizes them to the UPM
for thisLayer in myLayers:
	thisEPSfile = "%s.eps" % (thisLayer.parent.name)
	if os.path.exists(thisEPSfile):
		removeGlyphPaths()
		moveToImportDir()
		thisLayer.parent.color = 7
#     	print (thisLayer.parent.name + ' was updated. \n')
	else:
		print (thisLayer.parent.name + ' was not affected. \n')

# Run import command
runascript()
