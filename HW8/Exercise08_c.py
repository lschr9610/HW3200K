import arcpy
fc     = "P:/PythonArcMap/ESRI Press/Python/Data/Exercise08/Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"])  
for row in cursor:
    length = 0
    area   = 0
    if row[0].isMultipart:
        for part in row[0]:
            polygon = arcpy.Polygon(part)
            length = polygon.length
            area   = polygon.area
            print "perimeter length: " + str(int(length)) + " meters"
            print "area: " + str(int(area)) + " square meters"
            print
