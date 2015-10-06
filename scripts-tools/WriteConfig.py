# WriteConfig.py
import arcpy, os, sys
from arcpy import env

# INPUT
InvGDB = "Inventory.gdb/Inventory"

newfile = "Popup.xml"

if os.path.exists(newfile):
	os.remove(newfile)
file = open(newfile, 'w')	
	
	

query = "InClipShip = 'Y'"
rows = arcpy.SearchCursor(InvGDB, query, "", "InClipShip; ClipShipTitle; GDBName; PopUpFileName; MxdOrder; MetaDataBlob2","MxdOrder A")
for row in rows:
	print row.ClipShipTitle
	#print row.GDBName
	#print row.MxdOrder
	print
	print '<sublayer id=\"' + str(row.MxdOrder) + '\" popupconfig=\"popups/' + row.PopUpFileName + '\"/>'
	file.write ('<sublayer id=\"' + str(row.MxdOrder) + '\" popupconfig=\"popups/' + row.PopUpFileName + '\"/>\n')
 
 
# Delete cursor and row objects to remove locks on the data 
del row 
del rows

file.close()