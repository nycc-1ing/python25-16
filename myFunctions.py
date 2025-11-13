import turtle 
bob=turtle.Turtle()

def polygon( sides, distance, color ):
	angle = 360 / sides	
	bob.fillcolor( color )
	bob.begin_fill()
	for times in range( sides ):
		bob.forward( distance )
		bob.left( angle )
	bob.end_fill() 

def comet( c, distance, angle ): 
	bob.color( c )
	for times in range( 10 ):
		bob.pensize( times / 2 )
		bob.forward( distance )
		bob.left( angle )

def jump( x,y ):
	bob.penup()
	bob.goto( x,y ) 
	bob.pendown()


