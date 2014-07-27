import arcpy
import random
from arcpy import env
env.overwriteoutput = True
inputfc = arcpy.GetParameterAsText(0) 
outputfc = arcpy.GetParameterAsText(1) 
outpercent = int(arcpy.GetParameterAsText(2))   
desc = arcpy.Describe(inputfc)
inlist = []
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
count = 0
while row:
    id = row.getValue(fldname)
    inlist.append(id)
    row = rows.next()
    count += 1
outcount = count * outpercent / 100
while len(randomlist) < outcount:
    selitem = random.choice(inlist)
    randomlist.append(selitem)
    inlist.remove(selitem)
length = len(str(randomlist))
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)
