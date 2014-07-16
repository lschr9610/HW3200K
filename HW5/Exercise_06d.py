import arcpy
from arcpy import env
env.workspace = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    fcdict = {'name': fcdescribe.basename, 'type': str(fcdescribe.shapeType)}
    print "%(name)s is a %(type)s feature class" % fcdict
