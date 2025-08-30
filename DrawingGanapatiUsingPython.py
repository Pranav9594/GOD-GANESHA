from turtle import *
import pygame
import threading

# ================== Setup ===================
title('CoderHuBhai')
bgcolor("black")
speed(10)
pencolor('red')
fillcolor('orange')

# ==================== MUSIC ====================
def play_music():
    """Plays the background music in a separate thread."""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\prana\Pictures\Danka Baja - RaagJatt.mp3")  # update path
        pygame.mixer.music.play(-1)  # loop infinitely
    except Exception as e:
        print(f"Could not play music: {e}")

# Start music thread
threading.Thread(target=play_music, daemon=True).start()

def CoderHu(x, y):
    penup()
    goto(x, y)
    pendown()

# ================== Extra Functions ==================
def draw_main_face_outline():
    """Draws the larger outline of the face."""
    print("वक्रतुंड महाकाय सूर्यकोटि समप्रभ।")
    pencolor("gold")
    pensize(5)
    penup()
    goto(-50, 180)
    pendown()
    seth(30)
    fd(120)
    circle(60, 270)

def draw_trunk():
    """Draws the trunk."""
    print("निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥")
    penup()
    goto(0, 40)
    pendown()
    seth(-90)
    pensize(10)
    forward(50)
    circle(100, 80)
    pensize(9)
    circle(150, 50)
    pensize(7)
    circle(100, 60)
    pensize(5)
    circle(90, 60)
    pensize(4)
    circle(40, 60)
    circle(10, 90)

def add_text():
    """Adds 'Happy Ganesh Chaturthi' text in Sky Blue only."""
    penup()
    goto(-270, 320)   # Move to top-left corner
    color("skyblue")  # ✅ Only sky blue
    write("HAPPY GANESH CHATURTHI", align="left", font=("Arial", 30, "bold"))

def add_mantra():
    """Adds full mantra at the middle-right beside the drawing."""
    penup()
    goto(220, 5)   # Adjusted to middle right side
    color("gold")
    write("वक्रतुंड महाकाय सूर्यकोटि समप्रभ।\nनिर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥",
          align="left", font=("Arial", 25, "bold"))

# ================== Main Drawing ==================

# trunk    
CoderHu(-130,150)
seth(-120)
begin_fill()
circle(100,90)
circle(280,10)
circle(-120,90)
circle(-60,150)
circle(-30,60)
seth(-120)
circle(30,60)
circle(55,150)
circle(120,77)
circle(-100,115)
end_fill()

CoderHu(0,50)
seth(20)
begin_fill()
circle(-50,80)
circle(-200,70)
circle(-50,60)
seth(-20)
circle(50,70)
circle(205,70)
circle(50,85)
end_fill()

CoderHu(70,10)
seth(15)
begin_fill()
circle(90,120)
seth(-52)
circle(-90,110)
end_fill()

# eyes
def eye():
    seth(-55)
    begin_fill()
    circle(20,120)
    seth(-90)
    circle(-17,165)
    end_fill()

CoderHu(-100,110)    
eye()
CoderHu(40,110)
eye()

# tilak
def cir(r):
    begin_fill()
    circle(r)
    end_fill()

CoderHu(0,150)    
cir(10)
CoderHu(-2,125)
cir(8)
CoderHu(-4,105)
cir(5)

# crown
CoderHu(-80,200)
seth(30)
begin_fill()
circle(-150,60)
seth(141)
circle(120,80)
end_fill()

CoderHu(-70,225)
seth(30)
begin_fill()
circle(-120,60)
seth(141)
circle(95,80)
end_fill()

CoderHu(-30,280)
seth(-120)
begin_fill()
circle(20,250)
circle(-50,40)
seth(-100)
circle(50,42)
circle(-15,240)
end_fill()

CoderHu(-5,268)
cir(9)

# left ear
CoderHu(-160,130)
seth(120)
begin_fill()
circle(70,60)
circle(15,100)
circle(90,30)
circle(-15,40)
circle(90,30)
circle(20,100)
seth(-130)
circle(-20,100)
circle(-90,30)
circle(15,35)
circle(-90,50)
circle(-18,80)
circle(-70,80)
end_fill()

# right ear
CoderHu(140,130)
seth(60)
begin_fill()
circle(-70,60)
circle(-15,100)
circle(-90,30)
circle(15,40)
circle(-90,30)
circle(-20,100)
seth(-50)
circle(20,100)
circle(90,30)
circle(-15,35)
circle(90,50)
circle(18,80)
circle(70,80)
end_fill()

# belly
CoderHu(-130,-20)
seth(-60)
begin_fill()
circle(-20,60)
circle(150,50)
circle(60,60)
seth(175)
circle(-70,70)
circle(-132,50)
circle(40,40)
end_fill()

# left leg
CoderHu(-90,-250)
seth(180)
begin_fill()
circle(-100,60)
circle(20,90)
circle(40,40)
circle(20,60)
circle(120,40)
seth(178)
circle(-120,40)
circle(-25,60)
circle(-50,50)
circle(-30,90)
circle(70,50)
end_fill()

# right leg
CoderHu(120,-260)
seth(15)
begin_fill()
circle(120,50)
circle(20,90)
circle(70,40)
circle(120,40)
circle(-60,60)
circle(70,60)
circle(20,90)
seth(-120)
circle(20,120)
circle(40,50)
circle(-70,40)
seth(180)
circle(65,40)
circle(-35,40)
circle(-17,120)
seth(120)
circle(-14,70)
circle(-65,60)
circle(40,70)
circle(-115,50)
circle(-60,20)
circle(-15,98)
circle(-110,50)
end_fill()

# left hand
CoderHu(-170,-60)
seth(180)
begin_fill()
circle(20,80)
circle(-30,150)
circle(20,80)
seth(0)
circle(-20,80)
circle(32,170)
circle(-20,80)
end_fill()

CoderHu(-205,-80)
seth(75)
begin_fill()
circle(40,60)
seth(-150)
circle(40,60)
seth(65)
circle(-40,40)
seth(-45)
circle(-40,35)
end_fill()

# right hand
CoderHu(240,-60)
seth(180)
begin_fill()
circle(20,80)
circle(-30,150)
circle(20,80)
seth(0)
circle(-20,80)
circle(32,170)
circle(-20,80)
end_fill()

CoderHu(205,-80)
seth(75)
begin_fill()
circle(40,60)
seth(-150)
circle(40,60)
seth(65)
circle(-40,40)
seth(-45)
circle(-40,35)
end_fill()

# ================== Extra Features ==================
add_text()
add_mantra()

hideturtle()
done()
