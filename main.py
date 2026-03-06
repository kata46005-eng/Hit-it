from turtle import *


class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True 
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = Sprite(0,-100,10,'circle','orange')
goal = Sprite(-30, 150,0, 'triangle', 'green')
enemy1 = Sprite(-200,- 30, 10, 'square','red')
enemy1.set_move(-200, -30, 200, -30)
enemy2 = Sprite(200,30, 10, 'square','red')
enemy2.set_move(200, 30, -200, 30)
scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')
p = Turtle()
p.penup()
p.goto(-220,180)
p.pendown()
p.color('red')
p.forward(440)
p.right(90)
p.forward(300)
p.right(90)
p.forward(440)
p.right(90)
p.forward(300)
p.hideturtle()
w = Turtle()
w.penup()
w.goto(150,150)
w.points = 0
w.write(f'Счёт: {w.points}', font = ('Arial', 14, 'normal'))
w.hideturtle()
o = Turtle()
o.hideturtle()
r = Turtle()
r.hideturtle()
while w.points < 3:
    enemy1.make_step()
    enemy2.make_step()
    if player.is_collide(goal):
        player.goto(0,-100)
        w.points += 1
        w.clear()
        w.write(f'Счёт: {w.points}', font = ('Arial', 14, 'normal'))
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        o.write(f'Ты проиграл!', font = ('Arial', 14, 'normal'))
        break
if w.points == 3:
    r.write(f'Ты выиграл!', font = ('Arial', 14, 'normal'))

enemy1.hideturtle()
enemy2.hideturtle()
