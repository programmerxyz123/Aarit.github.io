import turtle
#set up the window
wn = turtle.Screen()
wn.title("Halloween Maze")
wn.bgcolor("white")
wn.setup(width = 600 , height = 400)
#create a turtle for drawing text and shapes
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


#Draw the title
pen.goto(0,100)
pen.write("Welcome to The Halloween Maze", align="center", font=("Arial", 24, "bold"))
#draw the play button
button_width = 120
button_height = 50
button_x, button_y = 0, 0 #center of the button


pen.goto(button_x - button_width/2, button_y - button_width/2)
pen.pendown()
pen.fillcolor("orange")
pen.begin_fill()
for _ in range(2):
    pen.forward(button_width)
    pen.left(90)
    pen.forward(button_height)
    pen.left(90)
pen.end_fill()
pen.penup()


# write the button text
pen.goto(button_x, button_y - 50)
pen.color("black")
pen.write("PLAY", align="center",font=("Arial", 18, "bold"))
pen.color("black")



# define click function
def on_click(x,y):
    # check if click is inside button bounds
    if (button_x - button_width/2 <= x  <= button_x + button_width/2 and
         button_y - button_height/2 <= y <= button_y + button_height/2):
        start_game()

def start_game():
    #Clear the screen
    pen.clear()
    wn.bgcolor("white")
    pen.goto(0,0)
    pen.write("Game started!", align="center", font=("Arial", 24, "bold"))
    #here you can add game logic

#Listen for Clicks
wn.onclick(on_click)



#keep window open
wn.mainloop()