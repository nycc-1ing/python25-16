from myFunctions import * 
from random import randint 
turtle.tracer( 0 )
bob.width(2)
turtle.colormode( 255 )

turtle.bgcolor( "black" )
bob.color( "yellow" ) 

#draws polygons in a circle 
for times in range( 10000 ):
	r = randint( 0, 255 ) 
	g = randint( 0, 255 ) 
	b = randint( 0, 255 ) 
	num = randint( 3, 6) 
	c = ( r, 0, b )
	polygon( 4, 40, c ) 
	bob.forward( times )
	bob.left( 50 * times )

