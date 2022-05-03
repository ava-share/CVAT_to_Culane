# CVAT_to_Culane

Work in Progress 

Input: Annotations in the following Format: XML - CVAT for Images (annotations.xml)

Output: txt file with the appropriate name (frameXXXX.lines.txt) for each individual image

The converter.py node reads the annotation file and finds all items with the name images. Then it gets the points that define the polylines to calculate the points along the line and scale them properly.
The code also outputs the calculated points into a text file compliant with the CULANE Dataset format. 

Currently, the maximum number of lines supported are 2, which can be easily modified to accept more than that. 
