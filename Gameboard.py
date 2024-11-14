import pygame
import sys
from Board_back import Boardclass
from monopoly_game_logic import Monopolyclass


# Initialize Pygame
pygame.init()

# Set up the display
screen_size = 760
block_size=120
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Monopoly Game Board")

# Initial colors
white=(255, 255, 255)
black=(0, 0, 0)
green=(0,255,0)
sky_blue=(135,206,235)
dark_blue=(0,0,139)
orange=(255, 165, 0)
red=(255, 0, 0)
yellow=(255, 255, 0)
#Initial check point data






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

#Sketch board
def draw_board():
    #draw outerline
    pygame.draw.rect(screen, black, (20, 20, screen_size - 40, screen_size - 40), 3)

def add_image(image,x,y):
    img_rect = image.get_rect(center=(x, y))
    screen.blit(image, img_rect)

def draw_go_block():
    block_x=screen_size - 20 - block_size
    block_y=screen_size - 20 - block_size
    pygame.draw.rect(screen, black,
                     (block_x, block_y, block_size, block_size), 3)
    add_image(go_image, block_x + block_size // 2, block_y + block_size // 2)

def draw_central_block():
    block_x=screen_size- 140- block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)
    add_image(central_image, block_x + block_size // 2, block_y + block_size // 2)

def draw_wanchai_block():
    block_x=screen_size- 260 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)
    add_image(wanchai_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_incometax_block():
    block_x=screen_size- 380 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen,black,
                     (block_x,block_y,block_size,block_size), 3)

    add_image(incometax_image,block_x+block_size // 2,block_y+block_size // 2)


def draw_stanley_block():
    block_x=screen_size- 500 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Stanley_image,block_x+block_size // 2,block_y+block_size // 2)


def draw_jail_block():
    block_x=screen_size- 620 -block_size
    block_y=screen_size- 20 -block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Jail_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_sheko_block():
    block_x=screen_size- 620 -block_size
    block_y=screen_size- 140-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y ,block_size,block_size), 3)

    add_image(sheko_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_mongkok_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-260-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(mongkok_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_chance_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-380-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(chance_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_TsingYi_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-500-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TsingYi_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_Freeparking_block():
    block_x=screen_size-620-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Freeparking_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_Shatin_block():
    block_x=screen_size-500-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Shatin_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_chance2_block():
    block_x=screen_size-380-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(chance2_image,block_x+block_size // 2,block_y+block_size // 2)


def draw_Tuenmun_block():
    block_x=screen_size-260-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TuenMun_image,block_x+block_size // 2,block_y+block_size // 2)
def draw_taipo_block():
    block_x=screen_size-140-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Taipo_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_Go_to_jail_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-620-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Go_to_jail_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_saikung_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-500-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Saikung_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_yuenlong_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-380-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(Yuenlong_image,block_x+block_size // 2,block_y+block_size // 2)


def draw_chance3_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-260-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(chance3_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_taio_block():
    block_x=screen_size-20-block_size
    block_y=screen_size-140-block_size
    pygame.draw.rect(screen, black,
                     (block_x,block_y , block_size, block_size), 3)

    add_image(TaiO_image,block_x+block_size // 2,block_y+block_size // 2)

def draw_players(player_positions):
    for position in player_positions:
        # Calculate player position on the board
        player_x = (position % 10) * block_size
        player_y = (position // 10) * block_size
        pygame.draw.circle(screen, red, (player_x, player_y), 10)

#sketch dice
def draw_dice():
    if Monopolyclass.dice1 == 1:
        add_image()
    if Monopolyclass.dice1 == 2:
        add_image()
    if Monopolyclass.dice1 == 3:
        add_image()
    if Monopolyclass.dice1 == 4:
        add_image()
    if Monopolyclass.dice1 == 5:
        add_image()
    if Monopolyclass.dice1 == 6:
        add_image()
    if Monopolyclass.dice2 == 1:
        add_image()
    if Monopolyclass.dice2 == 2:
        add_image()
    if Monopolyclass.dice2 == 3:
        add_image()
    if Monopolyclass.dice2 == 4:
        add_image()
    if Monopolyclass.dice2 == 5:
        add_image()
    if Monopolyclass.dice2 == 6:
        add_image()




def mainscreen(player_positions):
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background with white
        screen.fill(white)

        # Render the text
        text = font.render("MONOPOLY", True, black)
        text_rect = text.get_rect(center=(screen_size // 2, screen_size // 2))
        screen.blit(text, text_rect)

        # Draw the board lines
        draw_board()
        #draw blocks
        draw_go_block()
        draw_central_block()
        draw_wanchai_block()
        draw_incometax_block()
        draw_stanley_block()
        draw_jail_block()
        draw_sheko_block()
        draw_mongkok_block()
        draw_chance_block()
        draw_TsingYi_block()
        draw_Freeparking_block()
        draw_Shatin_block()
        draw_chance2_block()
        draw_Tuenmun_block()
        draw_taipo_block()
        draw_Go_to_jail_block()
        draw_saikung_block()
        draw_yuenlong_block()
        draw_chance3_block()
        draw_taio_block()

        draw_players(player_positions)

        # Update the display
        pygame.display.flip()
