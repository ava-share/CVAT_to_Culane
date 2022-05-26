# CVAT_to_Culane

Work in Progress 

Input: Annotations in the following Format: XML - CVAT for Images (annotations.xml) (see the examples folder)

Output: txt file with the appropriate name (frameXXXX.lines.txt) for each individual image (see the examples folder)

The converter.py node reads the annotation file and finds all items with the name images. Then it gets the points that define the polylines to calculate the points along the line and scale them properly.
The code also outputs the calculated points into a text file compliant with the CULANE Dataset format. A maximum of four lanes is supported as per CULANEs standart
