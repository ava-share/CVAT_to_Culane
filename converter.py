from xml.dom import minidom
    
def func(x,y,xp,yp):
    if x1 != x2:
        m=(yp-y)/(xp-x)
        b=y-m*x
    elif x==xp:
        b=x1
        m=9999
    return m,b
# parse an xml file by name
mydoc = minidom.parse('annotations.xml')

#get all items with the name image
items = mydoc.getElementsByTagName('image')

i = 0
#go through all images, and find polylines (aka childNodes), extract points and convert to floats
while i < items.length - 1:

    if items[i].childNodes.item(1).attributes['label'].value == 'line3':
        line3_points = items[i].childNodes.item(1).attributes['points'].value
        output_line3 = line3_points.replace(';',',')
        x1, y1, x2, y2, x3, y3 = map( float, output_line3.split(',') )

    elif items[i].childNodes.item(1).attributes['label'].value == 'line2':
        line2_points = items[i].childNodes.item(1).attributes['points'].value
        output_line2 = line2_points.replace(';',',')
        x1, y1, x2, y2, x3, y3 = map( float, output_line2.split(',') )
    
    coordinates1=[]

    for j in range(590, 300, -10):
          if j>=y2 and j<=y1 :
              m, b= func(x1,y1,x2,y2)
              x_desired=(j-b)/m
              coordinates1.append((x_desired,j))
          elif j>=y3 and j<=y2 :
              m, b= func(x2,y2,x3,y3)
              x_desired=(j-b)/m
              coordinates1.append((x_desired,j))

    print(coordinates1)

    if  items[i].childNodes.length == 5:
        if items[i].childNodes.item(3).attributes['label'].value == 'line3':
            line3_points = items[i].childNodes.item(3).attributes['points'].value
            output_line3 = line3_points.replace(';',',')
            x1, y1, x2, y2, x3, y3 = map( float, output_line3.split(',') )

        elif items[i].childNodes.item(3).attributes['label'].value == 'line2':
            line2_points = items[i].childNodes.item(3).attributes['points'].value
            output_line2 = line2_points.replace(';',',')
            x1, y1, x2, y2, x3, y3 = map( float, output_line2.split(',') )

    coordinates2=[]
    for j in range(590, 300, -10):
          if j>=y2 and j<=y1 :
              m, b= func(x1,y1,x2,y2)
              x_desired=(j-b)/m
              coordinates2.append((x_desired,j))
          elif j>=y3 and j<=y2 :
              m, b= func(x2,y2,x3,y3)
              x_desired=(j-b)/m
              coordinates2.append((x_desired,j)) 
    print(coordinates1)
   
    i = i + 1 
