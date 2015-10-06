# listFolderProject.py
# created to batch project data in folders or geoDB
import arcpy, os

# Set workspace environment to a folder
arcpy.env.workspace = "C:/Data/GISData/GDG/ClipAndShip/NewData/SoleSourceAquifers.gdb" 
# Set local variables
outWorkspace = "C:/Data/GISData/GDG/ClipAndShip/Temp.gdb"


# A list of shapefiles
fcList = []
lstFCs = arcpy.ListFeatureClasses("*")
for fc in lstFCs:
    #fcList.append(os.path.join(folder + "\\" + fc))
    print fc
    dsc = arcpy.Describe(fc)
    if dsc.spatialReference.Name == "Unknown":    
            print ('skipped this fc due to undefined coordinate system: ' + infc)
    else:
    	    print dsc.spatialReference.Name
    	    print dsc.spatialReference.Name.find("1983")
    	    # Determine the new output feature class path and name
    	    newname = fc.strip('.shp')
    	    print newname
    	    outfc = os.path.join(outWorkspace, newname)    	    
    	    
    	    # Set output coordinate system
    	    prjFile = "C:\Program Files (x86)\ArcGIS\Desktop10.0\Coordinate Systems\WGS 1984 Web Mercator (Auxiliary Sphere).prj"
    	    outCS = arcpy.SpatialReference(prjFile)
    	    print outfc
    	    if dsc.spatialReference.Name.find("1983") > 1:
	        print "This has an 1983 Datum"
	        arcpy.Project_management(fc, outfc, outCS,"NAD_1983_To_WGS_1984_1")
	        	    
	    if dsc.spatialReference.Name.find("1984") > 1:
    	    	print "This has an 1984 Datum"
    	  	arcpy.Project_management(fc, outfc, outCS)
    	    
    	    print
    	    print 
    	    print