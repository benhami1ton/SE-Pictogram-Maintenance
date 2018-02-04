#MenuTitle: 5. Create HTML Guide...
# -*- coding: utf-8 -*-
__doc__="""
Generates HTML page to show usage for each glyph. Can be searched to find the names or unicode.

QUICK START: Paste into Macro panel and run script. File will be placed in Downloads > SE-Pictogram-Maintenance-0.5
Requires fonts to be exported in OTF, TTF, WOFF, and WOFF2 in the /fonts folder to fully work.
"""
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

os.chdir(os.path.expanduser("~/Downloads/SE-Pictogram-Maintenance-0.5/"))

file = open("PictogramGuide.html","w")

file.write(str(lineBreak + htmlBeforeCSS + lineBreak + separator.join( cssIconList ) + lineBreak + htmlAfterCSS + separator.join( htmlIconList ) + lineBreak + htmlFooter))
print ("Guide File Created.")
