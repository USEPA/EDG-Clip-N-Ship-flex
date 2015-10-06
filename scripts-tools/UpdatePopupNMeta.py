# UpdatePopupName.py
# Updates popup file name field and metadatablob field
import arcpy

# Create update cursor for feature class 
# 
# INPUT
InvGDB = "Inventory.gdb/Inventory"
query = "InClipShip = 'Y'"
rows = arcpy.UpdateCursor(InvGDB, query) 

# Update the field  
for row in rows:
    # Fields from the table can be dynamically accessed from the row object.    
    row.PopUpFileName = 'PopupCandS' + row.GDBName + '.xml'
    row.MetaDataBlob2 = row.Description2 + '<br><A HREF="' + row.EDGLink + '" target="_blank"><IMG SRC="https://edg.epa.gov/clipship/doc/metadata.png" BORDER=0></A>'
    rows.updateRow(row) 

# Delete cursor and row objects to remove locks on the data 
# 
del row 
del rows
