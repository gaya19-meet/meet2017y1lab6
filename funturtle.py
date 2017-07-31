import turtle # python needs this to use all the turtle functions

turtle.shape('turtle') #changes the shape to a square
square = turtle.clone () #creats new turtle and saves it in square
square.shape('square') #changes shape of 2nd turtle to square
square.goto(100,100) #moves square to (x=100,y=100)

# draw a square
square.goto(0,0)
square.goto(50,0)
square.goto(50,50)
square.goto(0,50)
square.goto(0,0)
triangle = turtle.clone()


turtle.mainloop()
