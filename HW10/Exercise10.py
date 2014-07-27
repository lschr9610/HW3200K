##  In ArcGIS Desktop Help, research the AddLayer function of the ArcPy
##  mapping module and use it to write a script that adds the parks layer
##  from the Parks data frame in Austin_TX.mxd to the other two data
##  frames in the same map document.
###====================================================
##import arcpy
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin_TX.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##listdf = arcpy.mapping.ListDataFrames(mapdoc)
##for df in listdf:
##    print df.name
##del mapdoc
##del listdf
###====================================================
##import arcpy
##arcpy.env.overwriteOutput = True
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin_TX.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##dataset = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin/base.shp"
##spatialref = arcpy.Describe(dataset).spatialReference
##extent = arcpy.Describe(dataset).extent
##for df in arcpy.mapping.ListDataFrames(mapdoc):
##    df.spatialReference = spatialref
##    df.panToExtent(extent)
##    df.scale = 15000
##mapdoc.save()
##del mapdoc
###====================================================
##import arcpy
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin_TX.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##for df in arcpy.mapping.ListDataFrames(mapdoc):
##    print "Data frame " + df.name + " contains the following layers:"
##    lyrlist = arcpy.mapping.ListLayers(mapdoc, "", df)
##    for lyr in lyrlist:
##        print lyr.name
##del mapdoc
###====================================================
##import arcpy
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Austin_TX.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##lyrlist = arcpy.mapping.ListLayers(mapdoc)
##for lyr in lyrlist:
##    if lyr.name == "parks":
##        print lyr.name
##        lyr.visible = True
##        lyr.showLabels = True
##mapdoc.save()
##del mapdoc
##del lyrlist
###====================================================
##import arcpy
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Georgia.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
##for elem in elemlist:
##    print(elem.name + " " + elem.type)
##del mapdoc
###====================================================
##import arcpy
##mxd = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise10/Georgia.mxd"
##mapdoc = arcpy.mapping.MapDocument(mxd)
##elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
##title = elemlist[0]
##title.text = "Housing Vacancy for Georgia Counties (2000)"
##mapdoc.save()
##del mapdoc
