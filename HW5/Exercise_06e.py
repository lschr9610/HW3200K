import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("P:/PythonArcMap/ESRI Press/Python/Data/Exercise06/Results", "NM_hw.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == "Polygon":
        arcpy.CopyFeatures_management(fc, "P:/PythonArcMap/ESRI Press/Python/Data/Exercise06/Results/NM_hw.gdb/" + fcdesc.basename)
