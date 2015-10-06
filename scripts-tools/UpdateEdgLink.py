# UpdateEdgLink.py
# Updates Link to Edg
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
    row.EDGLink = 'https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid={' + row.MetaUuid + '}'
    rows.updateRow(row) 

# Delete cursor and row objects to remove locks on the data 
# 
del row 
del rows
