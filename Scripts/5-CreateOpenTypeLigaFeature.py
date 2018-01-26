#MenuTitle: 3. Import New EPS Outlines...
# -*- coding: utf-8 -*-
__doc__="""
Clear any leftover pictograms/ test paths in any glyphs that have a matching EPS file. Find EPS files in designated folder, move them to the Import folder, then open the Import Outlines dialog to allow user to import outlines

QUICK START: Only select glyphs with a unicode of E700 or higher. Script will add text to the clipboard, so go to the Font Info > Features > Liga and overwrite the existing text with what's on the clipboard.
"""
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
