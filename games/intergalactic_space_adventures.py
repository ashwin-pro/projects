# Importing the necessary modules.
# Activating pygame and ending program if import fails.
import pygame
if p.init()[1]:
    print(f"Sorry, there was an error. Please try again later.")

width,height = 500,500
screen = p.display.set_mode((width,height))
running = True
while running:
    for event in p.event.get():
        if event == p.QUIT:
            running = False
        else:
            p.display.set_caption('Intergalactic Space Adventures')
            p.display.update()
                               
p.quit()