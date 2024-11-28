from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y(100)
rect2.draw()

oval = Oval()
oval.randomize()
oval.draw()

tri = Triangle(0,0,10,0,0,20)
tri.draw()

paper.display()
