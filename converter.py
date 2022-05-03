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
    x1, y1, x2, y2, x3, y3 = 0, 0, 0, 0, 0, 0
    image_name = items[i].attributes['name'].value #get image name
    txt_file_name = image_name.replace('.jpg','.lines.txt') #get image name and convert to text file name
    #print(txt_file_name)
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

    if  items[i].childNodes.length == 5:
        x1, y1, x2, y2, x3, y3 = 0, 0, 0, 0, 0, 0
        if items[i].childNodes.item(3).attributes['label'].value == 'line3':
            line3_points = items[i].childNodes.item(3).attributes['points'].value
            output_line3 = line3_points.replace(';',',')
            x1, y1, x2, y2, x3, y3 = map(float, output_line3.split(',') )

        elif items[i].childNodes.item(3).attributes['label'].value == 'line2':
            line2_points = items[i].childNodes.item(3).attributes['points'].value
            output_line2 = line2_points.replace(';',',')
            x1, y1, x2, y2, x3, y3 = map(float, output_line2.split(',') )

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
