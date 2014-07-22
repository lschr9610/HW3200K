###   (( Note to self: CHECK WHETHER PYTHON 2.7 OR PYTHON 3.4!!! ))
## Challenge 1
## Write a script that creates a 15,000-meter buffer around features in the
#  airports.shp feature class classified as an airport ( based on the FEATURE
#  field ) and a 7,500-meter buffer around features classified as a seaplane
#  base. The results should be two separate feature classes, one for each
#  airport type.

## Challenge 2
## Write a script that adds a text field to the roads.shp feature class called
#  FERRY and populates this field with YES and NO values, depending on
#  the value of the FEATURE field.


import arcpy
from arcpy import env
env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise07"
fc = "airports.shp"
cursor = arcpy.da.SearchCursor(fc, "", '"FEATURE" == "Airport"')
unique_name = arcpy.CreateUniqueName("Results/C1AIRPORTSbuffer.shp")
arcpy.Buffer_analysis(cursor, unique_name, "15000 METERS")
#   RuntimeError: Object: Error in executing tool


##import arcpy
##from arcpy import env
##env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise07"
##fc = "roads.shp"
##newfield = "FERRY"
##fieldtype = "TEXT"
##arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)
