#UpdateDesc.py
# Used to update metadata blob in mxd
import arcpy

# INPUT
InvGDB = "Inventory.gdb/Inventory"

# Open a searchcursor 
#  Input: Inventory.gdb/Inventory
#  FieldList: Data_Layer_Name; Owner; Type 
#  SortFields: Owner A; Type A
# 
rows = arcpy.SearchCursor(InvGDB, "InClipShip = 'Y'", "", "InClipShip; ClipShipTitle; MetaDataBlob2","ClipShipTitle A") 

theTitle = "" 

# Iterate through the rows in the cursor 
# 
for row in rows: 
    if theTitle != row.ClipShipTitle: 
        theTitle = row.ClipShipTitle 
    print row.ClipShipTitle
    
    lookfor = row.ClipShipTitle
    # INPUT
    mxd = arcpy.mapping.MapDocument(r"gdgtest.mxd")
    df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    for lyr in arcpy.mapping.ListLayers(mxd, "*", df):        
        if (lyr.name == lookfor):
        	lyr.description = row.MetaDataBlob2
        	print lyr.description
        
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()        
        
    mxd.save()
    del mxd


