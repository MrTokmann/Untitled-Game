import turtle, time, winsound, random
image = turtle.Turtle()
screen = turtle.Screen()
kyna = turtle.Turtle()
kyna.penup()
image.hideturtle()
screen.title("Nimetön hakkaus peli")
screen.bgcolor("#68386c")
kyna.hideturtle()
kyna.speed(0)

sounds = ["sounds/1.wav", "sounds/2.wav", "sounds/3.wav", "sounds/4.wav"]

def credit():
    kyna.setpos(-320,50)
    kyna.write("Code by MrTokmann", font=("Comic Sans MS", 50, "normal"))
    kyna.setpos(-455,-50)
    kyna.write("Graphics by Tohtori Gerhard", font=("Comic Sans MS", 50, "normal"))
    time.sleep(3)
    kyna.setpos(-110,-150)
    kyna.write(":D :D :D", font=("Comic Sans MS", 40, "normal"))
    time.sleep(0.2)
    kyna.clear()
    kuva()

def kuva():
    image.showturtle()
    screen.register_shape('img/1.gif')
    screen.register_shape('img/2.gif')
    image.shape('img/1.gif')

    Button_x = -95
    Button_y = -200
    ButtonLength = 190
    ButtonWidth = 370

    kyna.penup()
    kyna.goto(Button_x, Button_y)
    kyna.goto(Button_x + ButtonLength, Button_y)
    kyna.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    kyna.goto(Button_x, Button_y + ButtonWidth)
    kyna.goto(Button_x, Button_y)

    screen.onclick(kuva_nappi)
    turtle.done()

def kuva_nappi(x,y):
    Button_x = -95
    Button_y = -200
    ButtonLength = 190
    ButtonWidth = 370
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            image.shape('img/2.gif')
            winsound.PlaySound(random.choice(sounds), winsound.SND_ASYNC)
            time.sleep(0.1)
            image.shape('img/1.gif')
            kuva()


credit()
