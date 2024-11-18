import pygame
import sys
from Board_back import Boardclass, Property_Slot, Chance_Slot, Gotojail_Slot,Goslot,Tax_Slot,Free_Parking_Slot, Visiting_Slot
from Player import Playerclass



# Initialize Pygame
pygame.init()

# Initial colors
white=(255, 255, 255)
black=(0, 0, 0)
green=(0,255,0)
sky_blue=(135,206,235)
dark_blue=(0,0,139)
orange=(255, 165, 0)
red=(255, 0, 0)
yellow=(255, 255, 0)

# Set up the display
font = pygame.font.Font(None, 50)
screen_size = 760
block_size=120
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Monopoly Game Board")

#Initial check point data
player_index=0





# Set up fonts
font = pygame.font.Font(None, 50)

#load images
go_image=pygame.image.load('Image_monopoly/Go.png')
go_image=pygame.transform.scale(go_image, (block_size-5, block_size-5))

central_image=pygame.image.load('Image_monopoly/Central.png')
central_image=pygame.transform.scale(central_image, (block_size-5, block_size-5))

wanchai_image=pygame.image.load('Image_monopoly/Wan_chai.png')
wanchai_image=pygame.transform.scale(wanchai_image, (block_size-5, block_size-5))

incometax_image=pygame.image.load('Image_monopoly/Income_tax.png')
incometax_image=pygame.transform.scale(incometax_image, (block_size-5, block_size-5))

Stanley_image=pygame.image.load('Image_monopoly/Stanley.png')
Stanley_image=pygame.transform.scale(Stanley_image, (block_size-5, block_size-5))

Jail_image=pygame.image.load('Image_monopoly/In_Jail.png')
Jail_image=pygame.transform.scale(Jail_image, (block_size-5, block_size-5))

sheko_image=pygame.image.load('Image_monopoly/Sheko.png')
sheko_image=pygame.transform.scale(sheko_image, (block_size-5, block_size-5))

mongkok_image=pygame.image.load('Image_monopoly/Mong_kok.png')
mongkok_image=pygame.transform.scale(mongkok_image, (block_size-5, block_size-5))

chance_image=pygame.image.load('Image_monopoly/Chance.png')
chance_image=pygame.transform.scale(chance_image, (block_size-5, block_size-5))

TsingYi_image=pygame.image.load('Image_monopoly/Tsing_Yi.png')
TsingYi_image=pygame.transform.scale(TsingYi_image, (block_size-5, block_size-5))

Freeparking_image=pygame.image.load('Image_monopoly/Free_parking.png')
Freeparking_image=pygame.transform.scale(Freeparking_image, (block_size-5, block_size-5))

Shatin_image=pygame.image.load('Image_monopoly/Shatin.png')
Shatin_image=pygame.transform.scale(Shatin_image, (block_size-5, block_size-5))

chance2_image=pygame.image.load('Image_monopoly/Chance_2.png')
chance2_image=pygame.transform.scale(chance2_image, (block_size-5, block_size-5))

TuenMun_image=pygame.image.load('Image_monopoly/Tuen_Mun.png')
TuenMun_image=pygame.transform.scale(TuenMun_image, (block_size-5, block_size-5))

Taipo_image=pygame.image.load('Image_monopoly/Tai_O.png')
Taipo_image=pygame.transform.scale(Taipo_image, (block_size-5, block_size-5))

Go_to_jail_image=pygame.image.load('Image_monopoly/Go_to_jail.png')
Go_to_jail_image=pygame.transform.scale(Go_to_jail_image, (block_size-5, block_size-5))

Saikung_image=pygame.image.load('Image_monopoly/Sai_Kung.png')
Saikung_image=pygame.transform.scale(Saikung_image, (block_size-5, block_size-5))

Yuenlong_image=pygame.image.load('Image_monopoly/Yuen_Long.png')
Yuenlong_image=pygame.transform.scale(Yuenlong_image, (block_size-5, block_size-5))

chance3_image=pygame.image.load('Image_monopoly/chance_3.png')
chance3_image=pygame.transform.scale(Yuenlong_image, (block_size-5, block_size-5))

TaiO_image=pygame.image.load('Image_monopoly/Tai_O.png')
TaiO_image=pygame.transform.scale(TaiO_image, (block_size-5, block_size-5))

#load dice images
'''dice1=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_1.png')
dice1=pygame.transform.scale(dice1, (block_size-5, block_size-5))
dice2=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_2.png')
dice2=pygame.transform.scale(dice2, (block_size-5, block_size-5))
dice3=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_3.png')
dice3=pygame.transform.scale(dice3, (block_size-5, block_size-5))
dice4=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_4.png')
dice4=pygame.transform.scale(dice4, (block_size-5, block_size-5))
dice5=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_5.png')
dice5=pygame.transform.scale(dice5, (block_size-5, block_size-5))
dice6=pygame.image.load('/Users/sherlock/Documents/程序/Python-code/Monopoly/Image monopoly/dice_6.png')
dice6=pygame.transform.scale(dice6, (block_size-5, block_size-5))
'''
dice1=pygame.image.load('Image_monopoly/Go.png')  # only for testing
dice1=pygame.transform.scale(dice1, (block_size-5, block_size-5))
dice2=pygame.image.load('Image_monopoly/Go.png')
dice2=pygame.transform.scale(dice2, (block_size-5, block_size-5))
dice3=pygame.image.load('Image_monopoly/Go.png')
dice3=pygame.transform.scale(dice3, (block_size-5, block_size-5))
dice4=pygame.image.load('Image_monopoly/Go.png')
dice4=pygame.transform.scale(dice4, (block_size-5, block_size-5))
dice5=pygame.image.load('Image_monopoly/Go.png')
dice5=pygame.transform.scale(dice5, (block_size-5, block_size-5))
dice6=pygame.image.load('Image_monopoly/Go.png')
dice6=pygame.transform.scale(dice6, (block_size-5, block_size-5))
#addimage
def add_image(image,x,y):
    img_rect = image.get_rect(center=(x, y))
    screen.blit(image, img_rect)

#textinbox
def text_in_box(text,font,color,x,y,length,height):
    textsurface=font.render(text,True,color)
    text_rect=textsurface.get_rect()
    text_rect.center=(x+length/2,y+height/2)
    screen.blit(textsurface,text_rect)

#Sketch board
def drawing():
    from monopoly_game_logic import Monopolyclass

    #draw the board
    pygame.draw.rect(screen, black, (20, 20, screen_size - 40, screen_size - 40), 3)
    # Render the text
    text = font.render("MONOPOLY", True, black)
    text_rect = text.get_rect(center=(screen_size // 2, screen_size // 2))
    screen.blit(text, text_rect)

    #draw_go_block():
    block_x=screen_size - 20 - block_size
    block_y=screen_size - 20 - block_size
    pygame.draw.rect(screen, black,
                     (block_x, block_y, block_size, block_size), 3)
    add_image(go_image, block_x + block_size // 2, block_y + block_size // 2)


    #draw_central_block():
    block_x=screen_size- 140- block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)
    add_image(central_image, block_x + block_size // 2, block_y + block_size // 2)

    #draw_wanchai_block():
    block_x=screen_size- 260 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)
    add_image(wanchai_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_incometax_block():
    block_x=screen_size- 380 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)

    add_image(incometax_image,block_x+block_size // 2,block_y+block_size // 2)


    #draw_stanley_block():
    block_x=screen_size- 500 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Stanley_image,block_x+block_size // 2,block_y+block_size // 2)


    #draw_jail_block():
    block_x=screen_size- 620 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Jail_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_sheko_block():
    block_x=screen_size- 620 -block_size
    block_y=screen_size- 140-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y ,block_size,block_size), 3)

    add_image(sheko_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_mongkok_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-260-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(mongkok_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_chance_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-380-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    # add_image(chance1_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_TsingYi_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-500-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TsingYi_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_Freeparking_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Freeparking_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_Shatin_block():
    block_x=screen_size-500-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Shatin_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_chance2_block():
    block_x=screen_size-380-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(chance2_image,block_x+block_size // 2,block_y+block_size // 2)


    #draw_Tuenmun_block():
    block_x=screen_size-260-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TuenMun_image,block_x+block_size // 2,block_y+block_size // 2)
    #draw_taipo_block():
    block_x=screen_size-140-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Taipo_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_Go_to_jail_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Go_to_jail_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_saikung_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-500-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Saikung_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_yuenlong_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-380-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Yuenlong_image,block_x+block_size // 2,block_y+block_size // 2)


    #draw_chance3_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-260-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(chance3_image,block_x+block_size // 2,block_y+block_size // 2)

    #draw_taio_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-140-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TaiO_image,block_x+block_size // 2,block_y+block_size // 2)
########################################################################################################################

        #sketch dice
    text_in_box("Player %r's turn "%(player_index+1),font,sky_blue,240,300,300,40)
    x_axis_dice1=260
    x_axis_dice2=500
    y_axis=200


    if Monopolyclass.dice1 == 1:
        add_image(dice1,x_axis_dice1,y_axis)
    if Monopolyclass.dice1 == 2:
        add_image(dice2,x_axis_dice1,y_axis)
    if Monopolyclass.dice1 == 3:
        add_image(dice3,x_axis_dice1,y_axis)
    if Monopolyclass.dice1 == 4:
        add_image(dice4,x_axis_dice1,y_axis)
    if Monopolyclass.dice1 == 5:
        add_image(dice5,x_axis_dice1,y_axis)
    if Monopolyclass.dice1 == 6:
        add_image(dice6,x_axis_dice1,y_axis)
    if Monopolyclass.dice2 == 1:
        add_image(dice1,x_axis_dice2,y_axis)
    if Monopolyclass.dice2 == 2:
        add_image(dice2,x_axis_dice2,y_axis)
    if Monopolyclass.dice2 == 3:
        add_image(dice3,x_axis_dice2,y_axis)
    if Monopolyclass.dice2 == 4:
        add_image(dice4,x_axis_dice2,y_axis)
    if Monopolyclass.dice2 == 5:
        add_image(dice5,x_axis_dice2,y_axis)
    if Monopolyclass.dice2 == 6:
        add_image(dice6,x_axis_dice2,y_axis)

    #Sketch botton
    














def draw_players(player_positions):
    for position in player_positions:
        # Calculate player position on the board
        player_x = (position % 10) * block_size
        player_y = (position // 10) * block_size
        pygame.draw.circle(screen, red, (player_x, player_y), 10)

#Main function
def mainscreen(playerposition):

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Fill the background with white
        screen.fill(white)
        #Keeping drawing board
        drawing()
        draw_players(playerposition)
        # Update the display
        pygame.display.flip()
# mainscreen()
