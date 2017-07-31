import turtle # python needs this to use all the turtle functions

turtle.shape('turtle') #changes the shape to a square
square = turtle.clone () #creats new turtle and saves it in square
square.shape('square') #changes shape of 2nd turtle to square
square.goto(100,100) #moves square to (x=100,y=100)

turtle.pendown()

# draw a square
square.goto(0,0)
square.goto(50,0)
square.goto(50,50)
square.goto(0,50)
square.goto(0,0)
square.penup()


turtle.shape('triangle')
triangle = turtle.clone()
triangle.penup()
triangle.goto(-100,-100)
triangle.pendown()
triangle.goto(-100,0)
triangle.goto(0,-100)
triangle.goto(-100,-100)
triangle.penup()


turtle.mainloop()
