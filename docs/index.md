<a name="top"></a>

### **[0. Setup](#setup)**
- [0.1 Install Scripts](#setup)
- [0.2 Helpful Resources](#setup)

### **[1. Create Project Directory](#setup)**
### **[2. Export Pictograms from Adobe Illustrator](#setup)**
- [2.1 Exporting EPS](#setup)

### **[3. Prepare Pictogram CSV File](#setup)**
- [3.1 Convert Spreadsheet to CSV](#setup)

### **[4. Working With Glyphs](#setup)**
- [4.1 Create Working Glyphs Document](#setup)
- [4.2 Create new glyph slots using the CSV file](#setup)
- [4.3 Update the names of all glyphs using the CSV file](#setup)
- [4.4 Import the EPS outlines to their corresponding glyph](#setup)
- [4.5 Resize the glyphs that are not 1024 units](#setup)
- [4.6 Generate OTF ligature code](#setup)
- [4.7 Create HTML guide for reference](#setup)

### **[5. Export Pictograms from Adobe Illustrator](#setup)**


[Return to top](#top)

# <a name="setup"></a>0. Setup

0.1 Install Scripts
----------
The bulk of the automation work is handled by Python scripts that are placed within Glyphs, and can be accessed from the menu bar when Glyphs is running. To install these, place the contents of the `Glyphs Scripts` folder into `~/Library/Application Support/Glyphs/Scripts`. The scripts can be kept in a deeper folder for cleaner organization, or each file can be placed in the Scripts folder individually.

After the files have been placed, open the Glyphs app and while holding the Option key, select the Scripts menu item and click "Reload Scripts". This will tell Glyphs to look in the Scripts folder and update it's list within the app. Currently they are not listing in alphabetical order, however this is a bug that the Glyphs developer is aware of.

[Return to top](#top)

0.2 Helpful Resources
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

<hr>

# 1. Create Project Directory
The location of your stored files is crucial to the success of using these tools, because many of the scripts reference exact locations on your computer. Familiarize yourself with how your Mac files are stored, and choose a place to store the project files. This can be anywhere on your computer, but the folders within your project folder must resemble this outline:

```
Project Folder
├── SpreadsheetExport
├── EPS
│   └── Import
│       └── Completed
└── Glyphs
```
The `EPS > Import > Completed` tree is the most important in this step, because the scripts are looking for those folders to move EPS files as they are being processed.

[Return to top](#top)

# 2. Export Pictograms from Adobe Illustrator
The first major step will be to prepare all of the icons to be imported into a font design software. This includes working with each icon and manipulating it in Illustrator until it is ready for export as an EPS file to be brought into Glyphs. *It is important to note that the name of the exported file must match exactly to the names that will be listed in the CSV file used later.*

The


### 2.1 Exporting EPS

The f

[Return to top](#top)

# 3. Prepare Pictogram CSV File

An important tool that will be reference in the beginning is the spreadsheet and comma separated values (CSV) file that will hold the Unicode value, the old name, and new name of the pictogram. Currently this file also contains images of the pictograms, and while the images do not need to be placed in the cells, those columns need to remain. Otherwise the scripts will pull information from the wrong columns.

### Convert Spreadsheet to CSV
1. Remove any blank columns before the Unicode column, which must be the first column.
2. Remove any blank columns after the last Pictogram Image column, which must be the last column.
3. It is okay to have empty rows at the bottom or throughout the document.
4. Export the Pictograms sheet to a Comma Separated Values file and place it in the SpreadsheetExport folder.

[Return to top](#top)

<hr>

# 4. Working With Glyphs

In this Section, we will:
1. Make a copy of an existing Glyphs file
2. Create new glyph slots, using the CSV file
3. Update the names of all glyphs, using the CSV file
4. Import the EPS outlines to their corresponding glyph
5. Resize the glyphs that are not 1024 units
6. Generate OTF ligature code
7. Export Font files
8. Create HTML guide for reference

[Return to top](#top)


4.1 Create Working Glyphs Document
-----------------------
Save the most recent Glyphs app file as a new document for the purposes of this update. This can be saved for future updates, but it's important to save new versions of this file to prevent overwriting if mistakes occur.

[Return to top](#top)

4.2 Create new glyph slots, using the CSV file
-----------------------
Using the first script in the Scripts menu bar, run `Add New Glyphs Based on CSV...`. No Glyphs need to be selected to run this script.

### What does this script do?
This script compares the CSV file to the existing Glyphs file that is open. If there are new entries with Unicode values that are unknown to the Glyphs file, it will create new glyph slots with the name and unicode value from the CSV file.

### What's in this script?
```python
# Import modules needed to run script
import os, csv, GlyphsApp
# Import `csv` module

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()

# Change directory to location of CSV file
os.chdir("/Users/YourUsername/Location/Of/Folder/Containing/CSVfile/")

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
with open('CSV-FILE-NAME.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip header information
    next(csv_reader)
    GetUpdatedNames()

# Create list of Unicode values already present in Glyphs App
unicodeChecker = []
for glyph in Glyphs.font.glyphs:
	unicodeChecker.append(str(glyph.unicode))


# Compare the unicode values in the CSV file to the Glyphs file, if there's a new unicode value then add it to the Glyphs file.
for key, val in newNames.items():
	if key in unicodeChecker:
		print(key + ' exists already')
	else:
		newGlyph = Glyphs.font.glyphs['E700'].copy()
		newGlyph.name = val
		newGlyph.unicode = key
		Font.glyphs.append(newGlyph)
		print(key + " doesn't exist already, new glyph made")

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

This script uses the line of code `newGlyph = Glyphs.font.glyphs['E700'].copy()` to duplicate the `TestSquare` glyph as a template for all new glyphs. It will keep a 1024x1024 square until Step 4.4 when it is removed.

[Return to top](#top)

4.3 Update the names of all glyphs, using the CSV file
-----------------------
Using the first script in the Scripts menu bar, run `Rename Glyphs from Pictogram CSV...`. No Glyphs need to be selected to run this script.
### What does this script do?
This script, like in step 4.2, systematically checks the Glyphs file for unicode values that match the CSV file being used. If the unicode values match, it will rename the glyph's name to match what's in the CSV file.
### What's in this script?
```python
# Import modules needed to run script
import os, csv, GlyphsApp

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory
os.chdir("/Users/YourUsername/Location/Of/Folder/Containing/CSVfile/")

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
with open('CSV-FILE-NAME', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip header information
    next(csv_reader)
    GetUpdatedNames()

# Compare the unicode values in the CSV file to the Glyphs file, if the unicode values match, then make the names equal as well.
for key, val in newNames.items():
  for glyph in Glyphs.font.glyphs:
		if glyph.unicode == key:
			glyph.name = val
			print(str(glyph.unicode) + ' has become ' + str(glyph.name))
		else:
			print(str(glyph.unicode) + ' is unchanged')

```
### Important notes before running script:
Like in step 4.2, you must update this line of code to match the location of the CSV file. Be careful to note backslashes and your Mac's username, and it may be necessary to begin the path with `~/`:
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

[Return to top](#top)

4.4 Import the EPS outlines to their corresponding glyph
-----------------------
With all the glyphs in your Glyphs App file now containing the correct unicode and name values, we can import the EPS outlines of the pictograms.

With all the glyphs in the file selected run `Import New Outlines...`.
### What does this script do?
This script checks the EPS folder to see if there are files that match the names of pictograms in the Glyphs App file. If there are, it will remove any existing paths or objects in that glyph, in preparation for importing the new paths and objects. It will then move the EPS files that do match into an `Import` folder. Then it will open the `Import > Outlines...` menu item, go to the `Import` folder, and allow you to select all files and open them.
### What's in this script?
```Python
import os, errno, shutil, GlyphsApp, subprocess, time
from subprocess import Popen, PIPE

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory to location of EPS folder
os.chdir("/Users/YourUsername/Location/Of/Project/Folder/EPS/")


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
			keystroke "i" using command down
			delay 0.5
			keystroke "g" using {command down, shift down}
			delay 0.5
			keystroke "~/Documents/Professional/Schneider Electric/17EC001_IconFont_MaintenanceAndGuide/EPS/Import/"
			delay 2
			keystroke return

		end tell
		"""
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(ascript)
	print (p.returncode, stdout, stderr)

# Loop through selected glyphs, to check if there's a new glyph. If there is, it deletes the paths of the selected glyph, imports the new ones, resizes them to the UPM
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

The `runascript()` function is a string of AppleScript code that will use the keyboard shortcut `Command + I` to open the Import Outlines... menu item. This must be assigned in System Preferences, under Keyboard Settings, and in the Shortcuts tab. The shortcut must be listed exactly as `File->Import->Outlines...` to access the menu item properly.

`runascript()` is a part of this script that is not crucial to its success. If there are any errors with running AppleScript within Python, this script should still remove the paths of each glyph and you can manually Import Outlines, choose all the EPS files, and Glyphs will bring them into their respective slots.

[Return to top](#top)

4.5 Resize the glyphs that are not 1024 units
-----------------------
Select only the glyphs with a unicode value of `E700` or higher, then run `Resize Icons to Full Width...`

### What does this script do?
This script calculates the size of each pictogram and scales it to the full width of 1024 units, which is the UPM of the font. This will ensure that no matter the size of the original icon, it will match the others and allow for reliable placement of the icon along the baseline.

This script also moves the EPS files that are currently in the `Import` folder into the `Completed` folder. This will help you know which pictograms have been fully manipulated. In order to see which pictograms did not import, the script will move the successful ones out of sight, leaving only the potentially problematic files.
### What's in this script?
```Python
import os, GlyphsApp, shutil

# Change directory to location of Import folder
os.chdir("/Users/YourUsername/Location/Of/Project/Folder/EPS/Import/")

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


# Loop through selected glyphs, to check if there's a new glyph. If there is, it deletes the paths of the selected glyph, imports the new ones, resizes them to the UPM
for thisLayer in myLayers:
    thisEPSfile = "%s.eps" % (thisLayer.parent.name)
    if os.path.exists(thisEPSfile):
    	moveToCompletedDir()
    	scaleToUPM()
#     	print (thisLayer.parent.name + ' was updated. \n')
    else:
    	print (thisLayer.parent.name + ' was not affected. \n')

```
### Important notes before running script:
Similar to previous steps, this time you must update this line of code to match the location of the EPS files. Be careful to note backslashes and your Mac's username, and it may be necessary to begin the path with `~/`:
```python
# Change directory to location of Import folder
os.chdir("/Users/YourUsername/Location/Of/Project/Folder/EPS/Import/")
```

When Transforming glyphs in this way, it's helpful to skim through the icons after this script runs to check for any anomalies in the objects. Individual glyphs can be manually scaled to 1024 units by selecting all the paths, locking the aspect ratio, and changing the width to 1024.

[Return to top](#top)

4.6 Generate OTF ligature code
-----------------------
### What does this script do?
This script takes selected glyphs and converts their names to the OTF code needed to substitute the individual letters into the specific Pictogram. After creating the needed code, it copies the data
### What's in this script?
```Python
import GlyphsApp
from AppKit import *

separator = "\n"
thisFont = Glyphs.font # frontmost font
listOfGlyphNames = [ l.parent.name for l in thisFont.selectedLayers ]
listOfGlyphNames = [ 'sub ' + " ".join(x) + ' by ' + x for x in listOfGlyphNames ]
clipboardText = separator.join( listOfGlyphNames )

def setClipboard( myText ):
	"""
	Sets the contents of the clipboard to myText.
	Returns True if successful, False if unsuccessful.
	"""
	try:
		myClipboard = NSPasteboard.generalPasteboard()
		myClipboard.declareTypes_owner_( [NSStringPboardType], None )
		myClipboard.setString_forType_( myText, NSStringPboardType )
		return True
	except Exception as e:
		return False

if not setClipboard(clipboardText):
	print "Warning: could not set clipboard to %s" % ( clipboardText )
```
### Important notes before running script:

[Return to top](#top)

4.7 Export Font files
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

4.7 Create HTML guide for reference
-----------------------
Select all the Pictograms in the project and run the script `Create HTML Guide from Selected Glyphs...`

### What does this script do?
This script creates an HTML page that contains a list of all the Pictograms, with some basic info including the name, icon, and unicode value for reference.
### What's in this script?
### Important notes before running script:
While it is not the most eloquent piece of HTML/CSS code, this is meant to be as self-contained as possible. In this version, you only need to share the `.html` file and `/fonts` folder together.

If you want to make the latest version of the Pictogram font always accessible, it is best to store exported font files on a web server that can be called up by this guide. That would allow this single HTML file to be shared and always show the latest version of the pictograms.

[Return to top](#top)

4.3 Scripting in Glyphs
-----------------------
### Dependencies Needed for Programming in Glyphs
There are a few packages that you will need to maximize the efficiency of using Python in Glyphs. As I am not a full fledged developer, I fully admit that some of these tools may not be needed in every instance, but it's what I have at my disposal to get these jobs completed.
#### Python
I've installed [Python 2.7.14](https://www.python.org/downloads/release/python-2714/) on my Mac OS X 10.13.2.
#### Vanilla
Go to Glyphs > Preferences > Addons > Modules and click the Install Modules button. This is often needed when interacting with the Glyphs GUI itself. Not required for all scripts, but some utilize Vanilla to manipulate Glyphs directly, so it's best to install it before starting.
