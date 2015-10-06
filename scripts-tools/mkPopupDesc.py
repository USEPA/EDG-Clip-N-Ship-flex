# mkPopupDesc.py
# Usage: mkPopupDesc.py <GeoDatabase> <Feature class> <Out xml file descriptor>
# Create by Frank Roberts, Innvovate Inc.

# Create a popup.xml file for give featureclass, and geodatabase 
import arcpy, os, sys
from arcpy import env



# Set the current workspace
gdb = sys.argv[1]
env.workspace = gdb

#  the field name, type, and length.
layer = sys.argv[2]
#fieldList = arcpy.ListFields("testFC")
fieldList = arcpy.ListFields(layer)

# Phase to add in between Popup and Layer Name.xml
newfile = sys.argv[3]

bad_strings = set(['OBJECTID', 'SHAPE', 'SHAPE_Length', 'SHAPE_Area', 'Shape', 'Shape_Length', 'Shape_Area', 'OBJECTID_1'])

if os.path.exists(newfile):
	os.remove(newfile)
	
file = open(newfile, 'w')

print '<?xml version="1.0" ?>'
file.write ('<?xml version="1.0" ?>\n')

print '<!-- File Created with mkPopupDesc.py by Frank Roberts - froberts@innovateteam.com -->'
file.write ('<!-- File Created with mkPopupDesc.py by Frank Roberts - froberts@innovateteam.com -->\n')

print "<configuration>"
file.write ("<configuration>\n")

print "<!-- Add field name with curly brackets in title tag below -->"
file.write ("<!-- Add field name with curly brackets for the title -->\n")

print "	<title></title>"
file.write ("	<title></title>\n")

print "	<description>\n" 
file.write ("	<description>\n" )

print "	<![CDATA[" 
file.write ("	<![CDATA[" )

for field in fieldList:
	if field.name not in bad_strings:
		#print '<b><i>' + field.aliasName + ': </i></b>{' +  field.name + '}\n'
		file.write (field.aliasName + ': <FONT COLOR="#5E5B5B"><b>{' +  field.name + '}</b></FONT><br>')

print "	]]>" 
file.write ("	]]>")

print "	</description>\n" 
file.write ("	</description>\n" )

print "	<fields>"
file.write ("	<fields>\n")

for field in fieldList:
	if field.name not in bad_strings:
		print '		<field name="' + field.name + '" alias="' + field.aliasName +'" visible="true"/>'
		file.write ('		<field name="' + field.name + '"' + ' />\n')

print "	</fields>"
file.write ("	</fields>\n")

print '	<!-- Show attachments = either true or false -->'
file.write ('	<!-- Show attachments = either true or false -->\n')

print "	<showattachments>false</showattachments>"
file.write ("	<showattachments>false</showattachments>\n")

print "</configuration>"
file.write ("</configuration>\n")


file.close()