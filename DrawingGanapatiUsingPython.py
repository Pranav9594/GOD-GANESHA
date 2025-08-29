import turtle
import threading
import pygame
import random
import time


def play_music():
    """Plays the background music in a separate thread."""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\prana\Pictures\Danka Baja - RaagJatt.mp3")
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    except Exception as e:
        print(f"Could not play music: {e}")


def draw_flower(t, x, y, size, color):
    """Draws a single flower at specified position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(2)

    # Draw flower petals
    for _ in range(6):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(60)

    # Draw center
    t.penup()
    t.goto(x, y - size//2)
    t.pendown()
    t.color("yellow")
    t.dot(size//2)


def falling_flowers(screen):
    """Creates continuous falling flowers effect."""
    flower_turtle = turtle.Turtle()
    flower_turtle.hideturtle()
    flower_turtle.speed(0)

    colors = ["red", "pink", "orange", "purple", "white", "light blue", "yellow"]

    while True:
        try:
            # Create flower at random x position at top
            x = random.randint(-400, 400)
            y = 350
            size = random.randint(8, 15)
            color = random.choice(colors)

            # Create a new turtle for this flower
            flower = turtle.Turtle()
            flower.hideturtle()
            flower.speed(1)
            flower.penup()

            # Draw flower and make it fall
            draw_flower(flower, x, y, size, color)

            # Animate falling
            for _ in range(100):  # Fall down the screen
                flower.sety(flower.ycor() - 2)
                time.sleep(0.02)

            # Clean up
            flower.clear()
            flower.hideturtle()

            # Wait before creating next flower
            time.sleep(random.uniform(0.5, 1.5))

        except:
            break  # Exit if there's an error (window closed)


def setup_turtle(t):
    """Sets up the initial turtle properties."""
    t.speed(6)
    t.screen.bgcolor("black")
    t.pensize(5)


def draw_head_curves(t):
    """Draws the initial curves of the head."""
    print("\n" + "="*60)
    print("🎨 Creating Lord Ganesha's divine form...")
    print("🙏 Chanting sacred prayer:")
    print()

    # First head curve
    t.color("gold")
    t.left(60)
    t.fd(50)
    t.left(15)
    t.circle(100, 90)
    t.fd(30)
    t.pensize(10)
    t.penup()
    t.right(90)
    t.fd(20)
    t.pendown()
    t.right(40)
    t.circle(-50, 90)
    t.fd(20)
    t.left(150)

    # Second head curve
    t.color("red")
    t.penup()
    t.fd(40)
    t.left(20)
    t.pendown()
    t.circle(50, 90)


def draw_main_face_outline(t):
    """Draws the larger outline of the face."""
    print("वक्रतुंड महाकाय सूर्यकोटि समप्रभ।")
    print("Creating the divine face outline... ✨")
    t.color("gold")
    t.penup()
    t.goto(0, 0)
    t.pensize(5)
    t.pendown()
    t.left(30)
    t.fd(120)
    t.circle(60, 270)


def draw_eyes_and_brows(t):
    """Draws the eyes and eyebrows."""
    # Eye
    t.color("gold")
    t.penup()
    t.forward(30)
    t.right(50)
    t.forward(135)
    t.pendown()
    t.pensize(8)
    t.circle(50, 90)
    t.left(95)
    t.penup()
    t.circle(60, 75)

    # Eyebrow
    t.penup()
    t.forward(15)
    t.left(90)
    t.pensize(2)
    t.pendown()
    t.circle(70, 90)


def draw_ears(t):
    """Draws the ears."""
    t.pensize(5)
    t.penup()
    t.forward(75)
    t.right(90)
    t.forward(20)
    t.pendown()
    t.circle(90, 90)
    t.forward(20)
    t.circle(30, 170)
    t.right(180)
    t.circle(28, 180)
    t.right(160)
    t.circle(25, 180)
    t.right(160)
    t.circle(22, 160)
    t.forward(20)
    t.circle(60, 45)


def draw_trunk(t):
    """Draws the trunk."""
    print("निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥")
    print("Drawing the sacred trunk... 🐘")
    t.penup()
    t.goto(0, 0)
    t.left(130)
    t.fd(140)
    t.right(250)
    t.backward(20)
    t.circle(80, 20)
    t.circle(20, 40)
    t.right(110)
    t.penup()
    t.fd(20)
    t.pendown()
    t.pensize(10)
    t.forward(50)
    t.circle(100, 80)
    t.pensize(9)
    t.circle(150, 50)
    t.pensize(7)
    t.circle(100, 60)
    t.pensize(5)
    t.circle(90, 60)
    t.pensize(4)
    t.circle(40, 60)
    t.circle(10, 90)


def draw_head_decorations(t):
    """Draws the decorations on the head."""
    t.color("red")
    t.penup()
    t.goto(-90, 290)
    t.right(230)
    t.pendown()
    t.circle(-100, 50)
    t.circle(200, 20)
    t.circle(50, 30)
    t.right(180)
    t.circle(50, 30)
    t.circle(200, 20)
    t.circle(-100, 40)
    t.right(95)
    t.penup()
    t.fd(40)
    t.right(90)
    t.pendown()
    t.circle(100, 40)
    t.penup()
    t.circle(35, 120)
    t.right(30)
    t.pendown()
    t.pensize(5)
    t.circle(60, 50)


def draw_tilak(t):
    """Draws the tilak and other red marks."""
    t.penup()
    t.goto(-70, 90)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(20, 180)
    t.end_fill()

    t.penup()
    t.left(75)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(70, 35)
    t.end_fill()

    t.left(180)
    t.backward(10)
    t.pendown()
    t.left(6)
    t.pensize(5)
    t.color("red")
    t.circle(-80, 40)


def draw_border_and_text(t):
    """Draws the border and writes the message."""
    print("\n" + "="*60)
    print("🎉 Completing Lord Ganesha's divine form...")
    print("🙏 Final blessings and completion:")
    print()

    t.penup()
    t.goto(0, 0)
    t.color("deep sky blue")
    t.setposition(-250, -300)
    t.write("Happy\nGanesh\nChaturthi", font=("arial", 20, "normal"), align="left")

    # Add Sanskrit prayer beside the Ganapati face (right side, clear of drawing lines)
    t.setposition(250, -50)  # Position to the right of the face, at middle height
    t.color("gold")
    prayer_text = "वक्रतुंड महाकाय\nसूर्यकोटि समप्रभ।\n\nनिर्विघ्नं कुरु मे देव\nसर्वकार्येषु सर्वदा॥"
    t.write(prayer_text, font=("arial", 22, "bold"), align="left")

    # Border/frame lines removed as requested


def draw_final_touch(t):
    """Draws a final decorative curve."""
    t.color("red")
    t.penup()
    t.goto(0, 0)
    t.left(118)
    t.fd(240)
    t.right(30)
    t.pendown()
    t.circle(90, 65)
    t.penup()


def main():
    """Main function to run the turtle drawing with music."""
    try:
        # Clean up any existing turtle instances
        if hasattr(turtle, '_screens') and turtle._screens:
            for screen in turtle._screens:
                try:
                    screen.bye()
                except:
                    pass

        # Start music in a background thread so turtle keeps drawing
        music_thread = threading.Thread(target=play_music, daemon=True)
        music_thread.start()

        screen = turtle.Screen()
        screen.setup(width=900, height=700)  # Set specific window size
        t = turtle.Turtle()

        setup_turtle(t)

        draw_head_curves(t)
        draw_main_face_outline(t)
        draw_eyes_and_brows(t)
        draw_ears(t)
        draw_trunk(t)
        draw_head_decorations(t)
        draw_tilak(t)
        draw_border_and_text(t)
        draw_final_touch(t)

        t.hideturtle()

        # Start falling flowers effect
        print("\n🌸 Starting divine flower shower... 🌸")
        flowers_thread = threading.Thread(target=falling_flowers, args=(screen,), daemon=True)
        flowers_thread.start()

        # Keep the window open
        screen.mainloop()

    except turtle.Terminator:
        print("Turtle graphics terminated. Please close any existing turtle windows and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
