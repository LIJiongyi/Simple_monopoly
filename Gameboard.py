
import pygame
import sys
import random
from Board_back import Boardclass, Property_Slot, Chance_Slot, Gotojail_Slot,Goslot,Tax_Slot,Free_Parking_Slot, Visiting_Slot
from Player import Playerclass
from monopoly_game_logic import Monopolyclass

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
#check point init


#load images
go_image=pygame.image.load('Image_monopoly/Go.png')
go_image=pygame.transform.scale(go_image, (block_size-5, block_size-5))

central_image=pygame.image.load('Image_monopoly/Central.png')
central_image=pygame.transform.scale(central_image, (block_size-5, block_size-5))

wanchai_image=pygame.image.load('Image_monopoly/Wan Chai.png')
wanchai_image=pygame.transform.scale(wanchai_image, (block_size-5, block_size-5))

incometax_image=pygame.image.load('Image_monopoly/income tax.png')
incometax_image=pygame.transform.scale(incometax_image, (block_size-5, block_size-5))

Stanley_image=pygame.image.load('Image_monopoly/Stanley.png')
Stanley_image=pygame.transform.scale(Stanley_image, (block_size-5, block_size-5))

Jail_image=pygame.image.load('Image_monopoly/In Jail.png')
Jail_image=pygame.transform.scale(Jail_image, (block_size-5, block_size-5))

sheko_image=pygame.image.load('Image_monopoly/Sheko.png')
sheko_image=pygame.transform.scale(sheko_image, (block_size-5, block_size-5))

mongkok_image=pygame.image.load('Image_monopoly/Mong kok.png')
mongkok_image=pygame.transform.scale(mongkok_image, (block_size-5, block_size-5))

chance1_image=pygame.image.load('Image_monopoly/chance 1.png')
chance1_image=pygame.transform.scale(chance1_image, (block_size-5, block_size-5))

TsingYi_image=pygame.image.load('Image_monopoly/Tsing YI.png')
TsingYi_image=pygame.transform.scale(TsingYi_image, (block_size-5, block_size-5))

Freeparking_image=pygame.image.load('Image_monopoly/Free parking.png')
Freeparking_image=pygame.transform.scale(Freeparking_image, (block_size-5, block_size-5))

Shatin_image=pygame.image.load('Image_monopoly/Shatin.png')
Shatin_image=pygame.transform.scale(Shatin_image, (block_size-5, block_size-5))

chance2_image=pygame.image.load('Image_monopoly/chance 2.png')
chance2_image=pygame.transform.scale(chance2_image, (block_size-5, block_size-5))

TuenMun_image=pygame.image.load('Image_monopoly/Tuen Mun.png')
TuenMun_image=pygame.transform.scale(TuenMun_image, (block_size-5, block_size-5))

Taipo_image=pygame.image.load('Image_monopoly/Tai po.png')
Taipo_image=pygame.transform.scale(Taipo_image, (block_size-5, block_size-5))

Go_to_jail_image=pygame.image.load('Image_monopoly/Go to jail.png')
Go_to_jail_image=pygame.transform.scale(Go_to_jail_image, (block_size-5, block_size-5))

Saikung_image=pygame.image.load('Image_monopoly/Sai Kung.png')
Saikung_image=pygame.transform.scale(Saikung_image, (block_size-5, block_size-5))

Yuenlong_image=pygame.image.load('Image_monopoly/Yuen Long.png')
Yuenlong_image=pygame.transform.scale(Yuenlong_image, (block_size-5, block_size-5))

chance3_image=pygame.image.load('Image_monopoly/chance 3.png')
chance3_image=pygame.transform.scale(Yuenlong_image, (block_size-5, block_size-5))

TaiO_image=pygame.image.load('Image_monopoly/Tai O.png')
TaiO_image=pygame.transform.scale(TaiO_image, (block_size-5, block_size-5))

#load dice images
dice1=pygame.image.load('Image_monopoly/dice_1.png')
dice1=pygame.transform.scale(dice1, (block_size-5, block_size-5))
dice2=pygame.image.load('Image_monopoly/dice_2.png')
dice2=pygame.transform.scale(dice2, (block_size-5, block_size-5))
dice3=pygame.image.load('Image_monopoly/dice_3.png')
dice3=pygame.transform.scale(dice3, (block_size-5, block_size-5))
dice4=pygame.image.load('Image_monopoly/dice_4.png')
dice4=pygame.transform.scale(dice4, (block_size-5, block_size-5))
dice5=pygame.image.load('Image_monopoly/dice_5.png')
dice5=pygame.transform.scale(dice5, (block_size-5, block_size-5))
dice6=pygame.image.load('Image_monopoly/dice_6.png')
dice6=pygame.transform.scale(dice6, (block_size-5, block_size-5))

#sketch board item
#add image function
def add_image(image,x,y):
    img_rect = image.get_rect(center=(x, y))
    screen.blit(image, img_rect)
#add text function
def text_in_box(text,font,color,x,y,length,height):
    textsurface=font.render(text,True,color)
    text_rect=textsurface.get_rect()
    text_rect.center=(x+length/2,y+height/2)
    screen.blit(textsurface,text_rect)
#add animation function
def roll_dice_animation(game_instance):
    # First generate the final dice values
    final_dice1 = random.randint(1, 6)
    final_dice2 = random.randint(1, 6)

    # Animate
    for _ in range(30):  # 30 frames of random values
        game_instance.dice1 = random.randint(1, 6)
        game_instance.dice2 = random.randint(1, 6)
        drawing(game_instance)
        pygame.display.flip()
        pygame.time.delay(100)

    # Show final values
    game_instance.dice1 = final_dice1
    game_instance.dice2 = final_dice2
    game_instance.dice_rolled=True
    drawing(game_instance)
    pygame.display.flip()

    return final_dice1, final_dice2

#sketch board
def drawing(game_instance):
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

    add_image(chance1_image,block_x+block_size // 2,block_y+block_size // 2)

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
    if game_instance.players:
        current_player = game_instance.players[game_instance.current_position]
        text_in_box(f"{current_player.name} 's turn", font, sky_blue, 240, 300, 300, 40)
    else:
        text_in_box("no player", font, sky_blue, 240, 300, 300, 40)
    x_axis_dice1=260
    x_axis_dice2=500
    y_axis=200

    if game_instance.dice1 == 1:
        add_image(dice1, x_axis_dice1, y_axis)
    elif game_instance.dice1 == 2:
        add_image(dice2, x_axis_dice1, y_axis)
    elif game_instance.dice1 == 3:
        add_image(dice3, x_axis_dice1, y_axis)
    elif game_instance.dice1 == 4:
        add_image(dice4, x_axis_dice1, y_axis)
    elif game_instance.dice1 == 5:
        add_image(dice5, x_axis_dice1, y_axis)
    elif game_instance.dice1 == 6:
        add_image(dice6, x_axis_dice1, y_axis)

    if game_instance.dice2 == 1:
        add_image(dice1, x_axis_dice2, y_axis)
    elif game_instance.dice2 == 2:
        add_image(dice2, x_axis_dice2, y_axis)
    elif game_instance.dice2 == 3:
        add_image(dice3, x_axis_dice2, y_axis)
    elif game_instance.dice2 == 4:
        add_image(dice4, x_axis_dice2, y_axis)
    elif game_instance.dice2 == 5:
        add_image(dice5, x_axis_dice2, y_axis)
    elif game_instance.dice2 == 6:
        add_image(dice6, x_axis_dice2, y_axis)
    #sketch botton
    game_instance.button(screen,font)





def draw_players(player_positions):
    for position in player_positions:
        # Calculate player position on the board
        player_x = (position % 10) * block_size
        player_y = (position // 10) * block_size
        pygame.draw.circle(screen, red, (player_x, player_y), 10)



#Main function
def mainscreen(game_instance, continue_game): # game_instance is the instance of the Monopolyclass
    # Main loop
    running = True
    if continue_game:
        game_instance.turns()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_instance.if_button_clicked(mouse_pos):
                    roll_dice_animation(game_instance)
                    game_instance.turns()  # 处理玩家回合


        # Fill the background with white
        screen.fill(white)
        #Keeping drawing board
        drawing(game_instance)

        #draw_players([p.position for p in game.players])
        # Update the display
        pygame.display.flip()
