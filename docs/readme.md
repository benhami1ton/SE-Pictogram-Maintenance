Introduction
-------------
The goal of this documentation is to provide in-depth information on how to update the Pictogram font used by Schneider Electric in various design applications. By following this guide in order, the reader should have a full grasp on the steps needed to update the font, as well as some insight into how the automation process is working.


<a name="top"></a>Table of Contents
------------------

### **[0. Setup](#setup)**
- [0.1 Install Scripts](#install)
- [0.2 Quick Start](#quickstart)
- [0.3 Helpful Resources](#resources)

### **[1. Create Project Directory](#projectdirectory)**
### **[2. Export Pictograms from Adobe Illustrator](#illustrator)**
### **[3. Prepare Pictogram CSV File](#prepCSV)**
- [3.1 Convert Spreadsheet to CSV](#createCSV)

### **[4. Working With Glyphs](#glyphsapp)**
- [4.1 Create Working Glyphs Document](#saveAs)
- [4.2 Create new glyph slots and update names using the CSV file](#addglyphs)
- [4.3 Import the EPS outlines to their corresponding glyph](#importoutlines)
- [4.4 Resize the glyphs that are not 1024 units](#resize)
- [4.5 Generate OTF ligature code](#OT)
- [4.6 Export font files](#export)
- [4.7 Create HTML guide for reference](#htmlguide)

[Return to top](#top)

# <a name="setup"></a>0. Setup

<a name="install"></a>0.1 Install Scripts
----------
The bulk of the automation work is handled by Python scripts that are placed within Glyphs, and can be accessed from the menu bar when Glyphs is running. To install these, place the contents of the `Glyphs Scripts` folder into `~/Library/Application Support/Glyphs/Scripts`. The scripts can be kept in a deeper folder for cleaner organization, or each file can be placed in the Scripts folder individually.

After the files have been placed, open the Glyphs app and while holding the Option key, select the Scripts menu item and click "Reload Scripts". This will tell Glyphs to look in the Scripts folder and update it's list within the app. Currently they are not listing in alphabetical order, however this is a bug that the Glyphs developer is aware of.

[Return to top](#top)

<a name="quickstart"></a>0.2 Quick Start
----------
To quickly test these files, this GitHub repository has been set up to accomodate downloading the latest release and run directly from the `/Downloads` folder. The content of each script can be copied into and run via the Macro window of the Glyphs app and run without installing them to `~/Library/Application Support/Glyphs/Scripts`. This is not recommended as a long-term solution, however it can provide some initial testing of the project.

1. Download the [latest release](https://github.com/benhami1ton/SE-Pictogram-Maintenance/releases/).
2. Add EPS files to the `/EPS` folder.
3. Add CSV file to the `/CSV` folder, renaming it the same name as the latest release. (Example: GitHub Release = SE-Pictogram-Maintenance-0.1.zip, so CSV = SE-Pictogram-Maintenance-0.1.csv)
3. Open Glyphs file.
4. Copy each script into the Macro window and run, taking care to look for any "Quick Start Instructions" at the top of the code.

[Return to top](#top)

<a name="resources"></a>0.3 Helpful Resources
----------
While this guide should get you through this process, it's always best to have some resources in case specific problems happen.

[Glyphs Tutorials](https://glyphsapp.com/tutorials)
------------
The main tutorial source for Glyphs. This will get you up and running with Glyphs very quickly, and has a great primer for [scripting with the Glyphs API](https://glyphsapp.com/tutorials/scripting-glyphs-part-1), which becomes a core tool to quickly manipulate information in this icon font.

[Glyphs Forum](https://forum.glyphsapp.com)
------------
The main Forum for Glyphs is an incredible resource of designers and programmers who are working within the same GUI with similar goals. Few of these designers are working with icons, but they end goals are usually the same with letterforms as you may be seeking with icons.

[Type Drawers](http://typedrawers.com/)
------------
One of the primary forums for the type design community, Type Drawers has a lot of archived questions when it comes to the broader scope of programming and software in the type design world. This is not the first place to look for specific questions, but it's sometimes the one place where your unique question might be answered.

[Return to top](#top)

0.4 Prepare for using Python
-----------------------
### Dependencies Needed for Programming in Glyphs
There are a few packages that you will need to maximize the efficiency of using Python in Glyphs. As I am not a full fledged developer, I fully admit that some of these tools may not be needed in every instance, but it's what I have at my disposal to get these jobs completed.
#### Python
I've installed [Python 2.7.14](https://www.python.org/downloads/release/python-2714/) on my Mac OS X 10.13.2. At this point, Glyphs works with Python 2.7.
#### Vanilla
Go to Glyphs > Preferences > Addons > Modules and click the Install Modules button. This is often needed when interacting with the Glyphs GUI itself. Not required for all scripts, but some utilize Vanilla to manipulate Glyphs directly, so it's best to install it before starting.

[Return to top](#top)

<hr>

# <a name="projectdirectory"></a>1. Create Project Directory
The location of your stored files is crucial to the success of using these tools, because many of the scripts reference exact locations on your computer. Familiarize yourself with how your Mac files are stored, and choose a place to store the project files. This can be anywhere on your computer, but the folders within your project folder must resemble this outline:

```
Project Folder
├── SpreadsheetExport
├── EPS
│   └── Import
│       └── Completed
├── fonts
└── Glyphs
```
The `EPS > Import > Completed` tree is the most important in this step, because the scripts are looking for those folders to move EPS files as they are being processed.

[Return to top](#top)

# 2. <a name="illustrator"></a>Export Pictograms from Adobe Illustrator
The first major step will be to prepare all of the icons to be imported into a font design software. This includes working with each icon and manipulating it in Illustrator until it is ready for export as an EPS file to be brought into Glyphs. *It is important to note that the name of the exported file must match exactly to the names that will be listed in the CSV file used later.*

[Return to top](#top)

# 3. <a name="prepCSV"></a>Prepare Pictogram CSV File

An important tool that will be reference in the beginning is the spreadsheet and comma separated values (CSV) file that will hold the Unicode value, the old name, and new name of the pictogram. Currently this file also contains images of the pictograms, and while the images do not need to be placed in the cells, those columns need to remain. Otherwise the scripts will pull information from the wrong columns.

### <a name="createCSV"></a>Convert Spreadsheet to CSV
1. Remove any blank columns before the Unicode column, which must be the first column.
2. Remove any blank columns after the last Pictogram Image column, which must be the last column.
3. It is okay to have empty rows at the bottom or throughout the document.
4. Export the Pictograms sheet to a Comma Separated Values file and place it in the SpreadsheetExport folder.

[Return to top](#top)

<hr>

# 4. Working With Glyphs

In this Section, we will:
1. Make a copy of an existing Glyphs file
2. Create new glyph slots and pdate the names of all glyphs, using the CSV file
3. Import the EPS outlines to their corresponding glyph
4. Resize the glyphs that are not 1024 units
5. Generate OTF ligature code
6. Export Font files
7. Create HTML guide for reference

[Return to top](#top)


<a name="saveAs"></a>4.1 Create Working Glyphs Document
-----------------------
Save the most recent Glyphs app file as a new document for the purposes of this update. This can be saved for future updates, but it's important to save new versions of this file to prevent overwriting if mistakes occur.

[Return to top](#top)

<a name="addglyphs"></a>4.2 Create new glyph slots, using the CSV file
-----------------------
Using the first script in the Scripts menu bar, run `1. Add/Update Glyphs From Pictogram CSV...`. No Glyphs need to be selected to run this script.

### What does this script do?
This script uses the exported CSV file to check 1) if a pictogram exists and 2) what the new name should be. It first compares any existing unicode values to the ones in the CSV list and makes new glyph slots if they don't already exist. Then it checks all the names and if they differ from the CSV, the names are updated.

### What's in this script?
```python
Import modules needed to run script
import os, csv, GlyphsApp

# Clears Macro panel printout. Comment this out to keep each iteration of script run.
Glyphs.clearLog()

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory to location of CSV file
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.8/CSV/"))

# Create a dictionary to store the new names
newNames = {}

# Assign each unicode as the key and the new name as the value
def GetUpdatedNames():
   for line in csv_reader:
       if line[-2]:
           newNames[line[0]] = line[-2]

# Open Pictogram CSV file and check for new entries
with open('SE-Pictogram-Maintenance-0.8.csv', 'r') as csv_file:
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
```

### Important notes before running script:
You must update this line of code to match the location of the CSV file. Be careful to note backslashes and your Mac's username, and it may be necessary to begin the path with `~/`:
```python
# Change directory to location of CSV file
os.chdir("/Users/YourUsername/Location/Of/Folder/Containing/CSVfile/")
```
You must also input the name of the CSV file, including the `.csv` file extension into this snippet:
```python
# Open Pictogram CSV file and check for new entries
with open('CSV-FILE-NAME.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
```
Also, if the spreadsheet and CSV have columns added from subsequent updates for new versions, the script can handle additional columns by using a `-2` index value in the function `GetUpdatedNames()`, which searches for the "second-to-last" column in the CSV file. As long as the Pictogram spreadsheet and CSV include icon images/examples, use an index of `-2` to find the names, otherwise use an index of `-1` which is equivalent to the "last column".

This script uses the line of code `newGlyph = Glyphs.font.glyphs['E700'].copy()` to duplicate the `TestSquare` glyph as a template for all new glyphs. It will keep a 1024x1024 square until Step 4.3 when it is removed.

### Other notes:
There is a line in the script that clears the console before running the script, just to keep things clean and understandable. If you don't this, and instead want to keep all notes in the console, comment out the line `Glyphs.clearLog()`.

[Return to top](#top)

<a name="importoutlines"></a>4.3 Import the EPS outlines to their corresponding glyph
-----------------------
With all the glyphs in your Glyphs App file now containing the correct unicode and name values, we can import the EPS outlines of the pictograms.

With all the glyphs in the file selected run `Import New EPS Outlines...`.
### What does this script do?
This script checks the EPS folder to see if there are files that match the names of pictograms in the Glyphs App. If there are, it will remove any existing paths or objects in that glyph, in preparation for importing the new paths and objects. It will then move the EPS files that do match into an `Import` folder. Then it will open the `Import > Outlines...` menu item, go to the `Import` folder, and allow you to select all files and open them.
### What's in this script?
```Python
import os, errno, shutil, GlyphsApp, subprocess, time
from subprocess import Popen, PIPE

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory to location of EPS folder
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.8/EPS/"))


currentDir = os.getcwd()

myLayers = Glyphs.font.selectedLayers
thisEPSnewPath = ""
ImportDir = 'Import'


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
			delay 0.5
			keystroke "g" using {command down, shift down}
			delay 0.5
			keystroke "~/Downloads/SE-Pictogram-Maintenance-0.8/EPS/Import/"
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
#     	print (thisLayer.parent.name + ' was updated. \n')
    else:
    	print (thisLayer.parent.name + ' was not affected. \n')

# Run import command
runascript()
```
### Important notes before running script:
Similar to steps 4.2 and 4.3, this time you must update this line of code to match the location of the EPS files. Be careful to note backslashes and your Mac's username, and it may be necessary to begin the path with `~/`:
```python
# Change directory to location of EPS folder
os.chdir("/Users/YourUsername/Location/Of/Project/Folder/EPS/")
```

The `runascript()` function is a string of AppleScript code that will use the keyboard shortcut `Command + I` to open the Import Outlines... menu item. This must be assigned in System Preferences, under Keyboard Settings, and in the Shortcuts tab. The shortcut must be listed exactly as `File->Import->Outlines...` to access the menu item properly. Below is the settings for that shortcut::

![System Preferences > Keyboard > Shortcuts](https://i.imgur.com/Wa5HFvt.png "System Preferences > Keyboard > Shortcuts")

`runascript()` is a part of this script that is not crucial to its success. If there are any errors with running AppleScript within Python, this script should still remove the paths of each glyph and you can manually Import Outlines, choose all the EPS files, and Glyphs will bring them into their respective slots.

[Return to top](#top)

<a name="resize"></a>4.4 Resize the glyphs that are not 768 units
-----------------------
Now that the EPS files are imported into the Glyphs app, they need to be scaled from their small size to a usable height and width. Run `Resize Pictograms to 75% of UPM...`

### What does this script do?
This script calculates the size of each pictogram and scales it to the  width of 768 units, which is is 75% UPM of the font (1024). This will ensure that no matter the size of the original icon, it will match the others and allow for reliable placement of the icon in the center of the frame.

This script also moves the EPS files that are currently in the `Import` folder into the `Completed` folder. This will help you know which pictograms have been fully manipulated. In order to see which pictograms did not import, the script will move the successful ones out of sight, leaving only the potentially problematic files.
### What's in this script?
```Python
import os, GlyphsApp, shutil

# Change directory to location of Import folder
os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.8/EPS/Import/"))

currentDir = os.getcwd()
completedDir = "Completed"
thisEPSnewPath = ""
PUAglyphs = []
xMax = []
yMax = []
sameMax = []

# Find and group PUA category
for myFont in Glyphs.fonts:
    for myGlyph in myFont.glyphs:
        if myGlyph.category == "Private Use":
        	PUAglyphs.append(myGlyph)
    print "PUAglyphs collected."

# Sort by width or height or square
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

# Transforms along width and square categories
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

# Transforms along height categories
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

# Centers glyps in middle of frame                                
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
```
### Important notes before running script:
Similar to previous steps, this time you must update this line of code to match the location of the EPS files. Be careful to note backslashes and your Mac's username, and it may be necessary to begin the path with `~/`:
```python
# Change directory to location of Import folder
os.chdir("/Users/YourUsername/Location/Of/Project/Folder/EPS/Import/")
```

When Transforming glyphs in this way, it's helpful to skim through the icons after this script runs to check for any anomalies in the objects. Individual glyphs can be manually scaled to 1024 units by selecting all the paths, locking the aspect ratio, and changing the width to 1024.

![Manual adjusting of glyphs can be done](https://i.imgur.com/E2CXWjT.png "Manual adjustment")

[Return to top](#top)

<a name="OT"></a>4.5 Generate OTF ligature code
-----------------------
### What does this script do?
This script takes any glyph categorized as Private Use and generates a full-word ligature substitution. This is the feature that allows a user to type the name of the pictogram and replace those letterforms with the pictogram. After creating a line of code for each pictogram, it updates the OpenType features panel in the Font Info settings.
### What's in this script?
```Python
import GlyphsApp

separator = "\n"
PUAglyphs = []
illegals = {" 0 ":" zero ", " 1 ":" one ", " 2 ":" two ", " 3 ":" three ", " 4 ":" four ", " 5 ":" five ", " 6 ":" six ", " 7 ":" seven ", " 8 ":" eight ", " 9 ":" nine ", " - ":" hyphen ", " _ ": " underscore ", " . ":" period "}

for myFont in Glyphs.fonts:
    for myGlyph in myFont.glyphs:
        if myGlyph.category == "Private Use":
        	PUAglyphs.append(str(myGlyph.name))


subLines = [ 'sub ' + " ".join(x) + ' by ' + x + ';'for x in PUAglyphs ]
ligaCode = separator.join( subLines )

for i in xrange(10):
	for i,j in illegals.iteritems():
		ligaCode = ligaCode.replace(i, j)

del(font.features['liga'])
font.features.append(GSFeature('liga', ligaCode))
font.updateFeatures()
print ligaCode
```
### Important notes before running script:
You must still Update and Compile the Features code in the Font Info panel. These Update the font with changes to the Features code, and Compile the font to binary so that it can be exported.

The script contains a list of special characters that are used in the names of the Pictograms. Right now, this list contains 0-9, periods, hyphens and underscores. These all may be used in names, however any other special characters must be added to the `illegals` dictionary, where the key:value pair is the special character and the name of that special character, respectively.

This code exports in the form of [Adobe'd Feature File Syntax](https://www.adobe.com/devnet/opentype/afdko/topic_feature_file_syntax.html). A great explanation of OpenType features can be found in Tal Leming's [OpenType Cookbook](http://opentypecookbook.com/).

[Return to top](#top)

<a name="export"></a>4.6 Export Font files
-----------------------
Using standard methods in Glyphs, export the project to all major font versions.

### What does this step do?
This is a multistep process of exporting the different types of font files that are needed for print and web usage.

The following font files are needed:
- OTF
- EOT
- TTF
- WOFF
- WOFF2

### Important notes for this step:
These files will be referenced in the HTML Guide, and so will be helpful to store these fonts in a nearby and easily referenced folder like `/fonts` in the same location as the HTML Guide.

The names of these files will be the same as the name used in the Font Info menu.

[Return to top](#top)

<a name="htmlguide"></a>4.7 Create HTML guide for reference
-----------------------
Select all the Pictograms in the project and run the script `Create HTML Guide from Selected Glyphs...`

### What does this script do?
This script creates an HTML page that contains a list of all the Pictograms, with some basic info including the name, icon, and unicode value for reference.
### What's in this script?
```Python
import os, GlyphsApp

lineBreak = '\n'
tab = '\t'
cssIconList = []
htmlIconList = []
separator = lineBreak

htmlBeforeCSS = '<!doctype html> ' + lineBreak + '<html lang="en"> ' + lineBreak + '<head> ' + lineBreak + tab + '	<meta charset="utf-8">' + lineBreak + tab + '<title>SE Icon Cheat Sheet</title>' + lineBreak + tab + '<meta name="description" content="SE Icon Cheat Sheet">' + lineBreak + tab + '<!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script><![endif]-->' + lineBreak + tab + '<style>' + lineBreak + tab + tab + '@font-face {' + lineBreak + tab + 'font-family: "' + Glyphs.font.familyName + '";' + lineBreak + tab + 'src: url("fonts/' + Glyphs.font.familyName + '-Regular.eot"); /* IE9 Compat Modes */' + lineBreak + tab + 'src: url("fonts/' + Glyphs.font.familyName + '-Regular.eot?#iefix") format("embedded-opentype"), /* IE6-IE8 */' + lineBreak + tab + 'url("fonts/' + Glyphs.font.familyName + '-Regular.woff2") format("woff2"), /* Super Modern Browsers */' + lineBreak + tab + 'url("fonts/' + Glyphs.font.familyName + '-Regular.woff") format("woff"), /* Pretty Modern Browsers */' + lineBreak + tab + 'url("fonts/' + Glyphs.font.familyName + '-Regular.ttf")  format("truetype"); /* Safari, Android, iOS */' + lineBreak + '}' + lineBreak + '.se-icons {' + lineBreak + tab + 'font-family: "' + Glyphs.font.familyName + '", Times, sans-serif;' + lineBreak + '}' + lineBreak + '.se-icon-liga {' + lineBreak + tab + 'font-family: "' + Glyphs.font.familyName + '", Times, sans-serif;' + lineBreak + tab + 'font-variant-ligatures: common-ligatures;' + lineBreak + tab + '-moz-font-feature-settings: "liga", "clig";' + lineBreak + tab + '-webkit-font-feature-settings: "liga", "clig";' + lineBreak + tab + 'font-feature-settings: "liga", "clig";' + lineBreak + '}' + lineBreak + 'div.container' + lineBreak + '{' + lineBreak + tab + tab + tab + 'width: 100%;' + lineBreak + tab +  tab + '}' + lineBreak + lineBreak + tab + tab + 'header, footer {' + lineBreak + tab +  tab + tab + 'padding: 1em;' + lineBreak + tab + tab + tab + 'color: white;' + lineBreak + tab + tab + tab + 'background-color: green;' + lineBreak + tab + tab + tab + 'clear: left;' + lineBreak + tab +  tab + tab + 'text-align: center;' + lineBreak + tab + tab + tab + 'font-family: Arial, sans-serif;' + lineBreak + tab + tab + '}' + lineBreak + lineBreak + tab + tab + 'nav ul {' + lineBreak + tab + tab + tab + 'list-style-type: none;' + lineBreak + tab + tab + tab + 'padding: 0;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + 'nav ul a {' + lineBreak + tab + tab + tab + 'text-decoration: none;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + 'div.main-icon-layout {' + lineBreak + tab + tab + tab + 'padding: 1em;' + lineBreak + tab + tab + tab + 'font-family: Arial, sans-serif;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.icon-parent {' + lineBreak + tab + tab + tab + 'padding: 0;' + lineBreak + tab + tab + tab + 'margin: 0;' + lineBreak + tab + tab + tab + 'list-style: none;' + lineBreak + tab + tab + tab + 'display: -webkit-box;' + lineBreak + tab + tab + tab + 'display: -moz-box;' + lineBreak + tab + tab + tab + 'display: -ms-flexbox;' + lineBreak + tab + tab + tab + 'display: -webkit-flex;' + lineBreak + tab + tab + tab + 'display: flex;' + lineBreak + tab + tab + tab + 'flex-flow: row wrap;' + lineBreak + tab + tab + tab + '-webkit-flex-flow: row wrap;' + lineBreak + tab + tab + tab + 'justify-content: space-around;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.icon-child {' + lineBreak + tab + tab + tab + 'background: #F0F0F0;' + lineBreak + tab + tab + tab + 'padding: 5px;' + lineBreak + tab + tab + tab + 'width: 320px;' + lineBreak + tab + tab + tab + 'height: 200px;' + lineBreak + tab + tab + tab + 'margin-top: 10px;' + lineBreak + tab + tab + tab + 'text-align: center;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.iconTitle {' + lineBreak + tab + tab + tab + 'padding-top: 10px;' + lineBreak + tab + tab + tab + 'font-family: Arial, sans-serif;' + lineBreak + tab + tab + tab + 'font-weight: bold;' + lineBreak + tab + tab + tab + 'font-size: 1em;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.cheatSheetIcon {' + lineBreak + tab + tab + tab + 'font-size: 100px;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.unicodeChar {' + lineBreak + tab + tab + tab + 'font-family: Arial, sans-serif;' + lineBreak + tab + tab + tab + 'color: gray;' + lineBreak + tab + tab + tab + 'padding-top: 15px;' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.testDiv {' + lineBreak + tab + tab + tab + 'background: green;' + lineBreak + tab + tab + tab + 'height: 100px;' + lineBreak + tab + tab + tab + 'width: 100px' + lineBreak + tab + tab + '}' + lineBreak + tab + tab + '.testType {' + lineBreak + tab + tab + 'font-size: 100px;' + lineBreak + tab + tab + '}'
htmlAfterCSS =  lineBreak + tab + tab + '</style>' + lineBreak + '</head>' + lineBreak + '<body>' + lineBreak + tab + '	<div class="container">' + lineBreak + tab + tab + '<header>' + lineBreak + tab + tab + '<h1>Schneider Electric Icon Font</h1>' + lineBreak + tab + tab + '<h6>version 0.2, Nov. 1 2016</h6>' + lineBreak + tab + tab + '</header>' + lineBreak + tab + '<div class="main-icon-layout">' + lineBreak + tab + tab + '<h3>Overview</h3>' + lineBreak + tab + tab + '<p>The primary intent of this icon font is to provide an additional tool for designers and developers to implement branded iconograpy. Using a font has the bonus of browser compatibility as well as a faster workflow when using the SE Icons. </p>' + lineBreak + tab + tab + '<h3>Usage</h3>' + lineBreak + tab + tab + '<p>There are a variety of ways that these icons can be implemented using the font files and CSS. The primary method on the web involves the use of pseudo elements.	By adding the prefix <code>se-</code> to an icon&#8217;s name (no spaces, no punctuation, CamelCase) you have created the class associated with the icon and this class will create a pseudo element when associated with an object. Ex. <code>se-ActionAnnotateClosed</code> </p>' + lineBreak + tab + tab + '<h3>OpenType</h3>' + lineBreak + tab + tab + '<p>When compatible, this font allows OT standard ligatures to replace the name of the icon with the icon itself. After ensuring this feature is enabled in your design software or CSS code, you can simply type the name of the icon and the corresponding image will replace the name. The icon names are case-sensitive and do not contain any spaces or punctuation.</p>' + lineBreak + tab + tab + '<h3>Updates</h3>' + lineBreak + tab + tab + '<p>There are a few relevant Python scripts used for updating and maintaining this font with new icons. These can be accessed <a href="https://github.com/benhami1ton/iconfont-build-update">via GitHub</a></p>' + lineBreak + tab + '</div>' + lineBreak + tab + '<div class="">' + lineBreak + tab +  tab + '<ul class="icon-parent">'
htmlFooter = lineBreak + tab + tab + '</ul>' + lineBreak + tab + '</div>' + lineBreak + '</div>' + lineBreak + '<script src="js/scripts.js"></script>' + lineBreak + '</body>' + lineBreak + '</html>'
for myFont in Glyphs.fonts:
    for myGlyph in myFont.glyphs:
        if myGlyph.category == "Private Use":
        	PUAglyphs.append(myGlyph)
    print "PUAglyphs collected."

for myGlyph in PUAglyphs:
	myGlyphUnicodeString = str(myGlyph.unicode)
	cssIconComponent = tab + tab + '.se-' + myGlyph.name + ':before {' + lineBreak + tab + tab + tab + 'content: "\\' + myGlyphUnicodeString.lower() + '";' + lineBreak + tab + tab + '}'
	cssIconList.append( cssIconComponent )

	htmlIconComponent = tab + tab + tab + tab + '<li class="icon-child">' + lineBreak + tab + tab + tab + tab + tab + '<div class="iconTitle">' + myGlyph.name + '</div>' + lineBreak + tab + tab + tab + tab + tab + '<div class="se-icons cheatSheetIcon se-' + myGlyph.name + '"></div>' + lineBreak + tab + tab + tab + tab + tab + '<div class="unicodeChar"> unicode: <code>' + myGlyph.unicode + '</code></div>' + lineBreak + tab + tab + tab + tab + '</li>' + lineBreak
	htmlIconList.append( htmlIconComponent )

os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.8/"))

file = open("PictogramGuide.html","w")

file.write(str(lineBreak + htmlBeforeCSS + lineBreak + separator.join( cssIconList ) + lineBreak + htmlAfterCSS + separator.join( htmlIconList ) + lineBreak + htmlFooter))
print ("Guide File Created.")
```
### Important notes before running script:
While it is not the most eloquent piece of HTML/CSS code, this is meant to be as self-contained as possible. In this version, you only need to share the `.html` file and `/fonts` folder together.

If you want to make the latest version of the Pictogram font always accessible, it is best to store exported font files on a web server that can be called up by this guide. That would allow this single HTML file to be shared and always show the latest version of the pictograms. You would then change the link to these files to a URL instead of file path.

[Return to top](#top)
