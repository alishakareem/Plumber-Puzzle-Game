import pygame
import tkinter as tk
import sys
from assets import *
from coordSetup import *
from main import main


# -------------------------------
class GameScreen:

    ''' This function initiates the game screen resolution and background image of the screen'''

    def __init__(self):
        self.res = (750, 525)
        self.screen = pygame.display.set_mode(self.res)
        self.background_image = pygame.image.load(
            'PlumrBGNew.png').convert_alpha()

    ''' This function handles all the buttons and its functionalities'''

    def gameScreen(self):
        color = (255, 255, 255)          # default color
        color_light = (170, 170, 170)    # light shade of the button
        color_dark = (100, 100, 100)     # dark shade of the button
        width = self.screen.get_width()  # stores the width of the screen into a variable
        # stores the height of the screen into a variable
        height = self.screen.get_height()

        # default font style
        smallfont = pygame.font.SysFont('impact', 35)

        '''footer design'''
        notefont = pygame.font.SysFont('arial', 20)    # footer font style
        # footer text
        note = notefont.render("Game developers: Kavya, Abhinav, Alisha, Jason, Jordan", False,
                               (255, 255, 255))
        noteRect = note.get_rect()  # getting the rectangle of that footer
        # arranging the text in the center of the window
        noteRect.center = (375, 500)

        '''header design'''
        headerfont = pygame.font.SysFont(
            'impact', 57, bold=False, italic=True)   # header font style
        # header text
        header = headerfont.render("- PLUMR -", False, (255, 255, 255))
        headerRect = header.get_rect()   # getting the rectangle of that header
        # arranging the text in the center of the window
        headerRect.center = (375, 100)

        '''buttons design'''
        # button 1
        text1 = smallfont.render('Start', True, color)
        # button 2
        text2 = smallfont.render('Instructions', True, color)
        # button 3
        text = smallfont.render('Quit', True, color)

        '''Based on the mouse events, all the game screen and buttons functionality enables  '''
        try:
            while True:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                    if ev.type == pygame.MOUSEBUTTONDOWN:    # checks if the mouse button is clicked
                        # executes the 'Instructions' button functionality
                        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                            showInstructions()
                        # executes the 'Start' button functionality
                        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 3 + 40:
                            main()
                        # executes the 'Quit' button functionality
                        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 3 <= mouse[1] <= height / 1.5 + 40:
                            quitGame()

                '''This function is used to adjust the opacity of the background image by passing
                 the position of the image & degree of opacity '''
                blit_alpha(self.screen, self.background_image, [0, 0], 3)

                # Displays the footer onto the screen
                self.screen.blit(note, noteRect)
                # Displays the header onto the screen
                self.screen.blit(header, headerRect)

                '''This part of code checks if the button is pressed or not'''
                mouse = pygame.mouse.get_pos()          # gets the mouse coordinates
                # points to the center of the screen
                if width / 2 <= mouse[0] <= width / 2 + 140:
                    #  if player hovers onto the position of the instruction button, it changes to light color
                    if height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.draw.rect(self.screen, color_light, [
                                         width / 2.75, height / 2, 200, 44])
                    #  if player hovers onto the position of the start button, it changes to light color
                    if height / 3 <= mouse[1] <= height / 3 + 40:
                        pygame.draw.rect(self.screen, color_light, [
                                         width / 2.5, height / 3, 140, 40])
                    #  if player hovers onto the position of the quit button, it changes to light color
                    if height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                        pygame.draw.rect(self.screen, color_light, [
                                         width / 2.5, height / 1.5, 140, 40])

                # by default the button color is displayed as dark color
                else:
                    pygame.draw.rect(self.screen, color_dark, [
                                     width / 2.75, height / 2, 200, 44])
                    pygame.draw.rect(self.screen, color_dark, [
                                     width / 2.5, height / 3, 140, 40])
                    pygame.draw.rect(self.screen, color_dark, [
                                     width / 2.5, height / 1.5, 140, 40])

                '''superimposing the text onto our button'''
                # start text
                self.screen.blit(text2, (width / 2.5, height / 2))
                # instruction text
                self.screen.blit(text1, (width / 2.2, height / 3))
                # quit text
                self.screen.blit(text, (width / 2.2, height / 1.5))

                # updating the display of the screen
                pygame.display.update()

        # handles exception
        except Exception as exe:
            print(type(exe), "-", exe.args, "-", exe)


''' This function is used to adjust the opacity of the background image'''


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (1, 1))
    temp.set_alpha(opacity)
    target.blit(temp, location)


'''This function deals with the Instructions button on the game screen'''


def showInstructions():
    pygame.init()
    # define the RGB value for white,green, blue colour .
    white = (255, 255, 255)
    peach = (255, 229, 180)
    black = (0, 0, 0)
    blue = (0, 0, 128)
    color_light = (170, 170, 170)  # light shade of the button
    color_dark = (100, 100, 100)  # dark shade of the button
    # assigning values to X and Y variable
    width = 750
    height = 525

    # create the display surface object of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((width, height))

    # set the pygame window name
    pygame.display.set_caption('Game Instructions')

    # create a font object.
    # 1st parameter is the font file which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.SysFont('malgungothic', 25)

    # create a text surface object,on which text is drawn on it.
    Instruction_text = "This plumber puzzle game is all about connecting the correct pipes to reach the destination. Intially, the player will be shown the random pipes " \
        "and player must tap on the pipe inorder to make it rotate and connect it to the destination.\nThere will be 3 levels and player needs"\
        " to complete each level inorder to unlock the next level.\nIf player completes all the three levels HOORAY!!! Player WINS\n"\
        "                       ********Best of luck********"

    smallfont = pygame.font.SysFont('timesnewroman', 25)
    color = (0, 0, 0)
    button_text = smallfont.render('Back to Main Menu', True, color)
    while True:

        # completely fill the surface object with white color
        display_surface.fill(peach)
        flag = 0
        # copying the text surface object to the display surface object at the center coordinate.
        blit_text(display_surface, Instruction_text, (20, 20), font, blue)

        # iterate over the list of Event objects that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT then quitting the pygame and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks if the mouse button is clicked
                # executes the 'Instructions' button functionality
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 1.55 <= mouse[1] <= height / 1.55 + 40:
                    new_obj = GameScreen()
                    new_obj.gameScreen()

        mouse = pygame.mouse.get_pos()  # gets the mouse coordinates
        # points to the center of the screen
        if width / 2 <= mouse[0] <= width / 2 + 140:
            #  if player hovers onto the position of the instruction button, it changes to light color
            if height / 1.55 <= mouse[1] <= height / 1.55 + 40:
                pygame.draw.rect(display_surface, color_light, [
                                 width / 2.95, height / 1.55, 200, 40])

            # by default the button color is displayed as dark color
            else:
                pygame.draw.rect(display_surface, peach, [
                                 width / 2.95, height / 1.55, 200, 40])

        '''superimposing the text onto our button'''
        # instruction text
        display_surface.blit(button_text, (width / 2.95, height / 1.55))
        # Draws the surface object to the screen.
        pygame.display.update()


def blit_text(display_surface, text, pos, font, color=pygame.Color('black')):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = display_surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]         # Reset the x.
                y += word_height  # Start on new row.
            display_surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


'''This function deals with the quit button functionality'''


def quitGame():
    # creating the tkinter window
    window = tk.Tk()

    # setting the size of window
    window.geometry("500x100")

    # creating and labeling a frame
    frame_a = tk.Frame()
    label_a = tk.Label(master=frame_a, text="Thank you for choosing this game")

    # display label and frame onto the window
    label_a.pack()
    frame_a.pack()

    # creating a button named 'Close'
    button = tk.Button(frame_a,
                       text="Close",
                       fg="red",
                       command=quit)

    # showing the button onto the window
    button.pack(side=tk.TOP)

    # runs the tkinter event loop
    window.mainloop()


'''Creation of the object to the class and calling its method'''
obj = GameScreen()
obj.gameScreen()


# Allows players to rotate tiles in 90 degree increments
def rotate_tile(tilecoords):
    oldTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            oldTile = tile[0]
            # break
    pipe_values = level1_pipes[oldTile]
    for i in pipe_values:
        if(isinstance(i, int)):
            rotation_value = i
        else:
            pipe = i
    # Sanity check that keeps it under 360
    pipe_copy = pygame.transform.rotate(pipe, 180)
    if(rotation_value+90 >= 360):
        rotation_value = 0
    else:
        rotation_value = rotation_value+90
    level1_pipes[oldTile] = {pipe_copy, rotation_value}
    active_keys = level1_pipes_active_pipes.items()
    for i in active_keys:
        if(oldTile == i[0]):
            level1_pipes_active_pipes[oldTile] = rotation_value
    final_check()


def final_check():
    print(level1_pipes_active_pipes)
    print(level1_pipes_values_correct)
    if (level1_pipes_active_pipes == level1_pipes_values_correct):
        print("WE DID IT!!")
        # create the display surface object
        # (x, y) is the height and width of pygame window
        x = 750
        y = 525
        win = pygame.display.set_mode((x, y))

        pygame.display.set_caption("Level Complete")

        # define the RGB value for black,
        black = (0, 0, 0)

        # completely fill the surface object with white color
        win.fill(black)
        win.blit(levelcomplete, (50, 0))

        # Draws the surface object to the screen.
        pygame.display.update()

        while True:
            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method
            for event in pygame.event.get():
                # if event object type is QUIT then quitting the pygame and program both.
                if event.type == pygame.QUIT:
                    pygame.quit()


def map_tile(pos):
    for i in range(25, 725, 50):
        for j in range(50, 500, 50):
            if i <= pos[0] <= i + 50:
                if j <= pos[1] <= j + 50:
                    return i, j

# Creates new tile class with pipe type and coordinates


def new_tile(pipe, tilecoords):
    newTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            newTile = tile[0]
            break
    level1_pipes[newTile] = pipe

# Initiates all tiles in place, and allows rotation


def init_tiles():
    window.fill(COLOUR)
    window.blit(background, (0, 0))
    for i in coords.keys():
        coord = coords[i]
        # print(coord)
        pipe_values = level1_pipes[i]
        # print(pipe_values)
        for i in pipe_values:
            if(isinstance(i, int)):
                rotation_value = i
            else:
                pipe = i
        # print(rotation_value)
        # print(pipe)
        pipe_copy = pipe
        pipe_copy = pygame.transform.rotate(pipe_copy, rotation_value)
        window.blit(pipe_copy, (coord[0], coord[1]))
        if(rotation_value+90 >= 360):
            rotation_value = 0
        else:
            rotation_value = rotation_value+90
        level1_pipes[i] = {pipe_copy, rotation_value}

# Defines initial pipe rotations


def init_rotate(pipe_values):
    for i in pipe_values:
        if(isinstance(i, int)):
            rotation_value = i
        else:
            pipe = i
        # print(rotation_value)
        # print(pipe)
    pipe_copy = pipe
    pipe_copy = pygame.transform.rotate(pipe_copy, 90)
    return(pipe_copy)

# Main Game loop
