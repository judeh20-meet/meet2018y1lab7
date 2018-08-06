import turtle



UP = 0
direction = None

def up():
    print("You pressed the up key.")
    turtle.forward(50)

def right():
    print("You pressed the right key.")
    turtle.right(45)

def left():
    print("You pressed the left key.")
    turtle.left(45)
    
def bottom():
    print("You presssed the bottom key.")
    turtle.backwards(50)


turtle.onkey(up, "Up") 
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")
turtle.onkey(bottom, "Down")
turtle.listen()
