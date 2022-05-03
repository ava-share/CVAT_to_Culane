# Authors: Pardis Taghavi & Jonas Lossner
# May 2022
# This program converts annotations in 'CVAT for images' format to Culane Dataset compliant format
# Input: annotations.xml - (name may differ) from CVAT
# Output: frameXXXX.lines.txt - individual textfile for each image
# Limitations: The code currently only handles 2 Lines, it can handle less than 2 lines but not more (this would be easy to add)

from xml.dom import minidom
    
def func(x,y,xp,yp):
    if x != xp:
        m=(yp-y)/(xp-x)
        b=y-m*x
    elif x==xp:
        b=x
        m=999999
    return m,b

def func2(listOfCoef):
  for n in range (0,len(listOfCoef),2):
    x.append(float(listOfCoef[n]))
  for m in range (1,len(listOfCoef),2):
    y.append(float(listOfCoef[m]))
  return x,y


def finding_piecewise_equations(x,y):
  coordinates=[]
  CoefNumber=len(y) 
  c=1
  for j in range(590, 300, -10):
    if c!=CoefNumber and len(y)!=0 :   
      if j>y[c] and j<=y[c-1] :
        m, b= func(x[c-1],y[c-1],x[c],y[c])
        x_desired=(j-b)/m
        coordinates.append((x_desired,j))
      if j<= y[c]:
        c+=1
  return coordinates


# parse an xml file by name
mydoc = minidom.parse('annotations.xml')

#get all items with the name image
items = mydoc.getElementsByTagName('image')

i = 0
#go through all images, and find polylines (aka childNodes), extract points and convert to floats
while i < items.length - 1:
   
    image_name = items[i].attributes['name'].value #get image name
    txt_file_name = image_name.replace('.jpg','.lines.txt') #get image name and convert to text file name
    #print(txt_file_name)

    gListA=[]
    gListB=[]
    x=[]
    y=[]
    if items[i].childNodes.length >= 2: #if there are no lines there is still a length of 1 so if less than 2 then there are no lines and we create an empty file

        if items[i].childNodes.item(1).attributes['label'].value == 'line3':
            line3_points = items[i].childNodes.item(1).attributes['points'].value
            output_line3 = line3_points.replace(';',',')
            gListA= output_line3.split(',')

        elif items[i].childNodes.item(1).attributes['label'].value == 'line2':
            line2_points = items[i].childNodes.item(1).attributes['points'].value
            output_line2 = line2_points.replace(';',',')
            gListA= output_line2.split(',')
        
           
        x,y = func2(gListA)
        coordinates1=finding_piecewise_equations(x,y)
        #print(coordinates1)

        line_points1 = ' '.join(map(str,coordinates1))
        line_points1 = line_points1.replace(') (',',')
        line_points1 = line_points1.replace(')','')
        line_points1 = line_points1.replace('(','')
        line_points1 = line_points1.replace(', ',' ')
        line_points1 = line_points1.replace(',',' ')
        #print(line_points1)
        with open(txt_file_name, 'w') as f: #write points to text file
            f.write(line_points1)
            f.write('\n')
        
    x=[]
    y=[]
    if  items[i].childNodes.length == 5: #check if there is a second polyline
        
        if items[i].childNodes.item(3).attributes['label'].value == 'line3':
            line3_points = items[i].childNodes.item(3).attributes['points'].value
            output_line3 = line3_points.replace(';',',')
            gListB= output_line3.split(',')

        elif items[i].childNodes.item(3).attributes['label'].value == 'line2':
            line2_points = items[i].childNodes.item(3).attributes['points'].value
            output_line2 = line2_points.replace(';',',')
            gListB= output_line2.split(',')

    
    x,y = func2(gListB)
    coordinates2=finding_piecewise_equations(x,y)
    #print(coordinates2)


    line_points2 = ' '.join(map(str,coordinates2))
    line_points2 = line_points2.replace(') (',',')
    line_points2 = line_points2.replace(')','')
    line_points2 = line_points2.replace('(','')
    line_points2 = line_points2.replace(', ',' ')
    line_points2 = line_points2.replace(',',' ')
    #print(line_points2)
    with open(txt_file_name, 'a') as f: #note a instead of w to append and not overwrite the previous points
        f.write(line_points2)

    i = i + 1 
