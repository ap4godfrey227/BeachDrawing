'''
Title: Luscious Seren8ty
Author: Aaron Godfrey and Kole Croffoot
Date: 10/29/18
    
Description:


'''

import turtle

import random

################################################################################
# Functions to draw parts of the picture                                       #
################################################################################

def drawWater(karla, width, height):
    '''Creates a rectangular space for water (Aaron)'''
    karla.goto(0, 400) 
    karla.down()
    karla.fillcolor('blue')
    karla.begin_fill()
    karla.goto(800, 400)
    karla.goto(800, 200)
    karla.goto(0, 200)
    karla.goto(0, 400)
    karla.end_fill()
    karla.up()
    
def drawSand(karla, width, height):
    '''Creates a rectangular space for sand (Aaron)'''
    karla.goto(0, 600)
    karla.down()
    karla.fillcolor('tan')
    karla.begin_fill()
    for i in range(2):
        karla.forward(800)
        karla.right(90)
        karla.forward(200)
        karla.right(90)
    karla.end_fill()
    karla.up()

def drawSky(karla, width, height):
    '''Creates a rectangular space for the sky (Aaron)'''
    karla.goto(0, 0)
    karla.down()
    karla.fillcolor('light blue')
    karla.begin_fill()
    for i in range(2):
        karla.forward(800)
        karla.right(-90)
        karla.forward(200)
        karla.right(-90)
    karla.end_fill()
    karla.up()

def drawSun(karla, width, height):
    '''Draws a yellow circle to represent the sun (Aaron)'''
    karla.goto(100, 0)
    karla.pencolor('yellow')
    karla.fillcolor('yellow')
    karla.begin_fill()
    for i in range(45):
        karla.forward(10)
        karla.right(-10)
    karla.end_fill()
    karla.up()

def drawSandTexture(karla, width, height):
    '''Creates dots to make the sand look like sand (Aaron)'''
    karla.pencolor('black')
    karla.color('black')
    karla.shape('circle')
    karla.turtlesize(0.1)
    for i in range(200):
        x = random.randrange(0, 800)
        y = random.randrange(400, 600)
        karla.goto(x, y)
        karla.stamp()

def drawWaves(karla, width, height):
    '''Creates a few lines to give the water texture (Aaron)'''
    karla.pencolor('black')
    karla.pensize(1)
    karla.left(30)
    for i in range(30):
        a = random.randrange(0, 800)
        b = random.randrange(200, 400)
        karla.goto(a, b)
        karla.down()
        for i in range(10):
            karla.forward(1)
            karla.left(10)
        for i in range(10):
            karla.right(10)
            karla.forward(1)
        karla.up()
    karla.right(120)
    
def drawBoat(karla, size):
    '''Determines how to draw a singular boat using angles and direction (Kole)'''
    karla.color('brown')
    karla.begin_fill()
    karla.forward(size)
    karla.right(-135)
    karla.forward(size/3)
    karla.right(-45)
    karla.forward(size/2)
    karla.right(-45)
    karla.forward(size/3)
    karla.end_fill()
    karla.right(-135)
   
def drawAllBoats(karla, width):
    '''Determines how to draw each singular boat using angles and direction, all at the same time (Kole)'''
    for i in range(5):
        x = random.randrange(width)
        y = random.randrange(600/3, 1200/3)
        karla.goto(x, y)
        karla.down()
        drawBoat(karla, random.randrange(50, 75))
        karla.penup()
        
def drawStarfish(karla,size):
    '''Determines how to draw a singular starfish using angles and direction (Kole)'''
    karla.color('pink')
    karla.fillcolor('pink')
    karla.begin_fill()
    for i in range(5):
        karla.forward(size)
        karla.right(144)
    karla.end_fill()
    
def drawAllStarfish(karla, width):
    '''Determines how to draw each singular starfish using angles and direction (Kole)'''
    for i in range(6):
        x = random.randrange(width)
        y = random.randrange(1200/3, 1800/3)
        karla.goto(x, y)
        karla.down()
        drawStarfish(karla, random.randrange(20, 30))
        karla.penup()
    
    
       
def drawScene(width, height):
    ''' Draw the entire picture '''

    draw_speed = 11 # the speed the turtle will draw, 1 - 11 with 11 the fastest
    
    # Get a turtle, name her karla, and place her in a window
    karla = setupTurtleWindow(width, height, "black", "My Picture", draw_speed)
    
    # DRAW YOUR SCENE HERE
    drawWater(karla, 0, 400)
    drawSand(karla, 0, 200)
    drawSky(karla, 0, 0)
    drawSun(karla, 200, 0)
    drawSandTexture(karla, 0, 200)
    drawWaves(karla, 0, 400)
    drawAllBoats(karla, width)
    drawAllStarfish(karla, width)
    
    # Make karla disappear
    karla.hideturtle()

################################################################################
# Setup function - DONT EDIT THIS FUNCTION                                     #
################################################################################
def setupTurtleWindow(window_width, window_height, background_color, title, speed):
    ''' Prepare a turtle to draw a picture '''
    
    # Setup the window - handle weird canopy error
    try:
        turtle.setup(width=window_width, height=window_height)
    except:
        turtle.setup(width=window_width, height=window_height)
    
    # make a new turtle
    t = turtle.Turtle()
    
    # set the turtle's speed
    turtle.speed(speed)
    if turtle.speed() == 0:
        turtle.delay(0)
        
    # setup the turtle's window
    t.screen.title(title)
    t.screen.bgcolor(background_color)
    t.screen.setworldcoordinates(0, window_height, window_width, 0)
            
    # Pickup the turtle's pen
    t.up()
    
    # give back the turtle    
    return t
    
################################################################################
drawScene(800, 600)  # draw my pretty picture in an 800x600 window
turtle.exitonclick() # wait for the window to close
