import arcpy
from arcpy import env
env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise08"
inFeatures = "Hawaii.shp"
outFeatureClass = "Hawaii_fc.shp"
arcpy.FeatureEnvelopeToPolygon_management(inFeatures, outFeatureClass, "MULTIPART")
