# ListMxdCalcTable.py
# steps through layers in mxd and describes components of them
# adds mxdOrder to inventory table
import arcpy, datetime

# INPUT
InvGDB = "Inventory.gdb/Inventory"


mxd = arcpy.mapping.MapDocument(r"gdgtest.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

order = 0
for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
    print
    print lyr.name
    print 'Order: ' + str(order)
    # Get feature count for layer
    result = arcpy.GetCount_management(lyr)
    print 'Number of features: ' + result.getOutput(0)
    # Get date
    now = datetime.datetime.now()
    print now.strftime("%Y-%m-%d %H:%M")
    print
    
    query = 'ClipShipTitle = \'' + lyr.name + '\''
    print query
    rows = arcpy.UpdateCursor(InvGDB, query, "", "InClipShip; ClipShipTitle; MetaDataBlob2","ClipShipTitle A")
    for row in rows:
    	row.MxdOrder = order
    	#row.MxdOrder = 1
    	rows.updateRow(row) 
    
    order = order + 1
 
# Delete cursor and row objects to remove locks on the data 
# 
del row 
del rows 
#mxd.save()
del mxd