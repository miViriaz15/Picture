"""
picture.py
Author: miViriaz15
Credit: I used the internet for drawing inspiration, https://www.rapidtables.com/web/color/html-color-codes.html for color codes 

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sqrt
# add your code here \/  \/  \/
#defining colors
cornflowerblue = Color(0x6495ED, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)

#defining line
thinlineblue = LineStyle(1, cornflowerblue) 
thinlinewhite = LineStyle(1, white)
thinlineblack = LineStyle(1, black)

#Defining Shapes
triangle = PolygonAsset([(500,500), (1000,500), (750, 500+ 250*sqrt(3))],thinlineblue, cornflowerblue)
circle = CircleAsset(100,thinlineblue,cornflowerblue)
smalltriangle = PolygonAsset([(725,600), (775,600), (750, 500+ 25*sqrt(3))],thinlineblack, black)

#print
s=Sprite(triangle, (120,120))
s.scale=0.8
Sprite(circle, (60,45))
Sprite(circle, (380,45))
Sprite(smalltriangle, (120,120))
#s.rotation=inradians
# add your code here /\  /\  /\


myapp = App()
myapp.run()
