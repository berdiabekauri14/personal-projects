import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)

class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)

    def go_up(self):
        self.setheading(90)
        self.forward(24)

    def go_down(self):
        self.setheading(270)
        self.forward(24)

    def go_left(self):
        self.setheading(180)
        self.forward(24)

    def go_right(self):
        self.setheading(0)
        self.forward(24)

maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX           XXXXX",
    "X  XXXXXXX  XXXXXXX   XXXX",
    "X       XX  XXXXXXX   XXXX",
    "X       XX  XXX         XX",
    "XXXXXX  XX  XXX  XXXXXX  X",
    "XXXXXX  XX  XXX  XXXXXX  X",
    "XXXXXX  XX  XXX  XXXXXX  X",
    "X  XXX      XXX          X",
    "X  XXX  XXXXXXXXXXXXXXX  X",
    "X       XXXXXXXXXXXXXX   X",
    "XXXXXXXXXXXXXXXXXXXXXXX  X",
    "XXXXXXXX                 X",
    "XXXXXXXXXXXXXXXXXX   XXXXX"
]

def setup_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
            if character == "P":
                player.goto(screen_x, screen_y)

pen = Pen()
player = Player()

setup_maze(maze)

turtle.listen()
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")

while True:
    wn.update()