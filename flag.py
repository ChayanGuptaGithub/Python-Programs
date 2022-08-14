import turtle 
t= turtle.Turtle()
t.speed(10)
t.up()
t.goto(200,1200)
t.down()
#orange
t.begin_fill()
t.color('#F79B21')
t.right(90)
t.fd(2400)
for i in range(1,3):
    t.left(90)
    if(i==2):
        t.fd(2400)
    else:
        t.fd(400)
t.end_fill()
#orange
t.up()
t.right(180)
t.goto(-200,1200)
t.down()
#green
t.begin_fill()
t.color('#0AA132')
t.fd(2400)
for i in range(1,3):
    t.right(90)
    if(i==2):
        t.fd(2400)
    else:
        t.fd(400)        
t.end_fill()
#green
t.up()
t.right(180)
t.goto(-200,0)
t.down()
#blue wheel
t.begin_fill()
t.color('navy')
t.circle(200)
t.end_fill()
t.up()
t.left(90)
t.fd(20)
t.right(90)
t.down()
t.begin_fill()
t.color('white')
t.circle(180)
t.end_fill()
#blue wheel
t.up()
t.left(90)
t.goto(-40,0)
t.right(90)
t.down()
#blue wheel(middle)
t.begin_fill()
t.color('navy')
t.circle(40)
t.end_fill()
t.up()
t.left(90)
t.goto(0,0)
t.right(90)
t.down()

#blue wheel(middle)
t.right(90)
for i in range(80):
    t.right(5)
    t.fd(180)
    t.back(180)
turtle.hideturtle()
turtle.done()