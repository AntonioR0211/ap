import pygame as pg
import pyautogui as ag
from tkinter import *

# For Infinite Loop
i = 1
# First Time Opening
t = 1
# Define Menu For Easy Pause Access In Game
def menu():
    game = 0
    window = Tk()
    myfont = ("Roboto", 90, "normal")
    alert = ("Roboto", 20, "italic")
    title=Label(window, text="Art Studio", font=myfont)
    title.place(x=130, y=10)

    # Help Explaination in Menu
    help1=Label(window, text="Controls:")
    help1.place(x=130, y=250)
    help2=Label(window, text="Draw on Board = Left Click")
    help2.place(x=130, y=275)
    help3=Label(window, text="Erase on Board = Right Click")
    help3.place(x=130, y=300)
    help7=Label(window, text="Erase ALL Board = Delete")
    help7.place(x=130, y=325)
    help4=Label(window, text="Cycle Through Colors = A or D")
    help4.place(x=450, y=275)
    help5=Label(window, text="Increase Pen Size = W")
    help5.place(x=450, y=300)
    help6=Label(window, text="Decrease Pen Size = S")
    help6.place(x=450, y=325)
    help8=Label(window, text="Space To Return To Controls")
    help8.place(x=450, y=250)
    help9=Label(window, text="Escape To Quick Exit")
    help9.place(x=450, y=350)
    # Don't Want To Annoy Player So Removes Text After Seeing It Once
    if t == 1:
            help9=Label(window, text="READ CONTROLS TO UNDERSTAND HOW TO PLAY", font=alert)
            help9.place(x=50, y=375)

    # Confirm Button
    confirmbtn = Button(window, text="To Canvas", command=window.destroy)
    confirmbtn.place(x=250, y=500)
    exitbtn = Button(window, text="Exit Program", command=escape)
    exitbtn.place(x=400, y=500)

    # Window Setup
    window.title("Art Studio")
    window.geometry("800x600+10+10")
    window.mainloop()

# Exit Application
def escape():
    print("Thanks for Playing!")
    quit()

# Begin Process
menu()

game = 1

# Beginning of Art Section
while i == 1:
    if game == 1:
        game = 0
        t = 0
        # Beginning User Input
        pen_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black']
        background = ("White")
        pen_option = pen_colors.index("black")

        # Canvas and Art Pieces
        x, y = ag.size()
        pg.init()
        size = width, length = x, y
        screen = pg.display.set_mode(size)
        screen.fill(background)
        pg.display.set_caption("Art Studio")
        pensize = 5

        # Checks For Inputs From User
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    escape()
                # Drawing and Erasing
                elif pg.mouse.get_pressed() == (1, 0, 0):
                    mouse_pos = pg.mouse.get_pos()
                    pg.draw.circle(screen, pen_colors[pen_option], mouse_pos, pensize)
                elif pg.mouse.get_pressed() == (0, 0, 1):
                    mouse_pos = pg.mouse.get_pos()
                    pg.draw.circle(screen, background, mouse_pos, (pensize * 2))
                # Keyboard Inputs
                if event.type == pg.KEYDOWN:
                    key = event.key
                    if key == pg.K_a:
                        if pen_option == 0:
                            pen_option = (len(pen_colors) - 1)
                        else:
                            pen_option -= 1
                    elif key == pg.K_d:
                        if pen_option == (len(pen_colors) - 1):
                            pen_option = 0
                        else:
                            pen_option += 1
                    elif key == pg.K_w:
                        pensize += 1
                    elif key == pg.K_s:
                        if pensize != 1:
                            pensize -= 1
                    elif key == pg.K_DELETE:
                        screen.fill(background)
                    elif key == pg.K_ESCAPE:
                        escape()
                    elif key == pg.K_SPACE:
                        menu()

            pg.display.update()
