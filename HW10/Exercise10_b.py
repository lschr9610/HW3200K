import arcpy
mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
parkslyr = None
for df in arcpy.mapping.ListDataFrames(mapdoc):
    if df.name == "Parks":
        print "Data frame " + df.name + " contains the following layers: "
        lyrlist = arcpy.mapping.ListLayers(mapdoc, "", df)
        for lyr in lyrlist:
            if lyr.name == "parks":
                print lyr.name
                parkslyr = lyr
if parkslyr:
    for df in arcpy.mapping.ListDataFrames(mapdoc):
        if df.name != "Parks":
            arcpy.mapping.AddLayer(df, parkslyr, "BOTTOM")
mapdoc.save()

##for df in arcpy.mapping.ListDataFrames(mapdoc):
##    print "Data frame " + df.name + " contains the following layers: "
##    lyrlist = arcpy.mapping.ListLayers(mapdoc, "", df)
##    for lyr in lyrlist:
##         print lyr.name
del mapdoc
