import turtle 

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(400,500)
polygon=turtle.Turtle()

length =30
side = 6
angle = 360.0 / side
for n in range(side):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()
    
