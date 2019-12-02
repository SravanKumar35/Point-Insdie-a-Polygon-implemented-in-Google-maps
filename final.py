INF = 1000000.0

#Returns True if Point P lies inside the polygon
def isInside(poly, n, p):	
	
	extreme = [INF, p[1]]
	count=0
	i=0
	
	while True:
		next = (i+1)%n
		if doIntersect(poly[i], poly[next], p, extreme) == True:
			if orientation(poly[i], p, poly[next]) == 0:
				return onSegment(poly[i], p, poly[next])
			count = count + 1

		i = next
		if i == 0:
			break
			
	return count&1


#Returns true if the side of polygon and extended line intersects
def doIntersect(p1, q1, p2, q2):	
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)
	
	if o1!= o2 and o3!=o4:
		return True
	
	if o1 == 0 and onSegment(p1, p2, q1):
		return True
		
	if o2 == 0 and onSegment(p1, q2, q1):
		return True
		
	if o3 == 0 and onSegment(p2, p1, q2):
		return True
		
	if o4 == 0 and onSegment(p2, q1, q2):
		return True
		
	return False


#Finds out the orientation of 3 points(0 - collinear, 1 - clockwise, 2 - anti-clockwise)
def orientation(p, q, r):
	#Collinearity condition - Area of Triangle = 0
	det = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])
	
	if det == 0:
		return 0
	
	if det > 0:
		return 1
	else:
		return 2


#Given 3 collinear points, the function checks if point q lies on line segment pr
def onSegment(p, q, r):
	if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
		return True
	
	return False





import gmplot
n = int(input("Enter no. of points: "))

if n<3:
	print("Can't construct polygon")
else:
	poly = []
	lat = []
	lon = []
	print("Enter X and Y cordinates seperated by Space:")
	for i in range(n):
		temp = str(input())
		x = list(temp.split(" "))
		x = [float(i) for i in x]
		lat.append(x[0])
		lon.append(x[1])
		poly.append(x)		
	
	gmap5 = gmplot.GoogleMapPlotter(sum(lat)/len(lat), sum(lon)/len(lon), 13)
	gmap5.scatter(lat, lon, '# FF0000', size = 120, marker = False)
	gmap5.polygon(lat, lon, color = 'cornflowerblue')
	                
	temp = str(input("Enter the point to classify: \n"))
	p = list(temp.split(" "))
	p = [float(i) for i in p]
	gmap5.marker(p[0], p[1])
	gmap5.draw( "Output.html" ) 

	if isInside(poly, n, p) == True:
		print("Point lies inside the Polygon")
	else:
		print("Point lies Outside the Polygon")

