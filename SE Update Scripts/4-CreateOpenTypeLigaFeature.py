#MenuTitle: 4. Update OT Ligature Features...
# -*- coding: utf-8 -*-
__doc__="""
Selects only Private Use category items and creates ligature code
(sub e x a m p l e by example). Applies feature to font.

QUICK START: Paste into Macro Window and run. Must Update and Compile
before exporting font.
"""
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

del(Glyphs.font.features['liga'])
Glyphs.font.features.append(GSFeature('liga', ligaCode))
Glyphs.font.updateFeatures()
print ligaCode
