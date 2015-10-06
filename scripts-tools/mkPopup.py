# Create a popup.xml file for give featureclass, and geodatabase 
import arcpy, os, sys
from arcpy import env

# Set the current workspace
gdb = sys.argv[1]
env.workspace = gdb

#  the field name, type, and length.
layer = sys.argv[2]
fieldList = arcpy.ListFields(layer)

newfile = sys.argv[3]
#newfile = "Popup.xml"

if os.path.exists(newfile):
	os.remove(newfile)
	
file = open(newfile, 'w')

print '<?xml version="1.0" ?>'
file.write ('<?xml version="1.0" ?>\n')

print '<!-- File Created with mkPopup.py by Frank Roberts - froberts@innovateteam.com -->'
file.write ('<!-- File Created with mkPopup.py by Frank Roberts - froberts@innovateteam.com -->\n')

print "<configuration>"
file.write ("<configuration>\n")

print "<!-- Add field name with curly brackets in title tag below -->"
file.write ("<!-- Add field name with curly brackets for the title -->\n")

print "	<title></title>"
file.write ("	<title></title>\n")

print "	<fields>" 
file.write ("	<fields>\n" )


bad_strings = set(['OBJECTID', 'SHAPE', 'SHAPE_Length', 'SHAPE_Area', 'Shape', 'Shape_Length', 'Shape_Area', 'OBJECTID_1'])

for field in fieldList:
	#if field.name <> "OBJECTID" AND field.name <> "SHAPE":
	if field.name not in bad_strings:
		print '		<field name="' + field.name + '" alias="' + field.aliasName +'" visible="true"/>'
		file.write ('		<field name="' + field.name + '" alias="' + field.aliasName +'" visible="true"/>\n')

print "	</fields>"
file.write ("	</fields>\n")

print '	<!-- Show attachments = either true or false -->'
file.write ('	<!-- Show attachments = either true or false -->\n')

print "	<showattachments>false</showattachments>"
file.write ("	<showattachments>false</showattachments>\n")

print "</configuration>"
file.write ("</configuration>\n")


file.close()