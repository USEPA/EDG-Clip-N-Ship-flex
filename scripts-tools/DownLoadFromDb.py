#DownLoadFromDb.py
# Used to query inventory db and download zipfiles flagged in DownLoadIt item
# run unzipdir.py after downloading
import arcpy, sys, urllib2, zipfile, os

# INPUT
InvGDB = "Inventory.gdb/Inventory"
workingdir = 'C:\Data\GISData\GDG\ClipAndShip\NewZips'

# Open a searchcursor 
#  Input: Inventory.gdb/Inventory
#  FieldList: Data_Layer_Name; Owner; Type 
#  SortFields: Owner A; Type A
# 
rows = arcpy.SearchCursor(InvGDB, "DownLoadIt = 'Y'", "", "DownLoadIt; DataLink; InClipShip; ClipShipTitle","ClipShipTitle A") 

theTitle = "" 

# Iterate through the rows in the cursor 
# 
for row in rows: 
    if theTitle != row.ClipShipTitle: 
        theTitle = row.ClipShipTitle 
    print row.ClipShipTitle
    print row.DataLink    
    urlIn = row.DataLink
    file=os.path.basename(urlIn)
    print file
    filefullpath = workingdir + "\\" + file
    print filefullpath
    # Delete file if exists
    if os.path.exists(filefullpath):
	os.remove(filefullpath)
    u = urllib2.urlopen(urlIn)
    localFile = open(filefullpath, 'wb')
    localFile.write(u.read())
    localFile.close()
    print 
    
del row 
del rows
