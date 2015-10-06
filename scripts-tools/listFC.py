# listFc.py
# list contents of geodatabase and runs mkPopup.py against them
# usage: python listFc.py mygedb.gdb txtadd
import arcpy, os, sys
from arcpy import env
from arcpy import mapping

# Set the current workspace
gdb = sys.argv[1]
filetag = sys.argv[2]

folder = gdb
env.workspace = folder

fcList = []

lstFCs = arcpy.ListFeatureClasses("*")
for fc in lstFCs:
    #fcList.append(os.path.join(folder + "\\" + fc))
    print fc
    string = gdb + " " + fc + " Popup" + filetag + fc + ".xml"
    print string
    os.system("mkPopup.py "+ string )

