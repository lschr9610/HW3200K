import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise08"
newfc = "Results2/newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
array.add(arcpy.Point(0, 0))
array.add(arcpy.Point(0, 1000))
array.add(arcpy.Point(1000, 1000))
array.add(arcpy.Point(1000, 0))
array.add(arcpy.Point(0, 0))
cursor.insertRow([arcpy.Polygon(array)])
del cursor
