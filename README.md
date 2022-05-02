# CVAT_to_Culane

Work in Progress 

Input: Annotations in the following Format: XML - CVAT for Images (annotations.xml)

Output: txt file with the appropriate name (frameXXXX.lines.txt)

The converter.py node reads the annotation file and finds all items with the name images. Then it gets the points from the polylines to calculate the points.
The code also outputs the calculated points into a text file compliant with the CULANE Dataset format. 

Additionally, the code at the moment only supports one or two polylines, and only takes in polylines that are defined by three points. This will be fixed soon
