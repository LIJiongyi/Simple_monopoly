import pygame


def mainscreen():
    from Gameboard import drawing,draw_players,screen,font
    # Main loop

    # Fill the background with white
    screen.fill(255,255,255)
    # Keeping drawing board
    drawing()
    # draw_players(playerposition)
    # Update the display
    pygame.display.flip()