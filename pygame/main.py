import pygame
import os
import button

os.environ['SDL_VIDEO_CENTERED'] = '1'
#initialize
pygame.init()


info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h


#Create the window
screen = pygame.display.set_mode((screen_width - 10, screen_height - 50), pygame.RESIZABLE)

#Create title of the game
pygame.display.set_caption("Word Ladder")
icon = pygame.image.load('pygame/Assets/icon.png')
pygame.display.set_icon(icon)


#variable
menu_state = "main"

#menu
icon_menu = pygame.image.load('pygame/Assets/icon_menu.png')
icon_menu_x = 850
icon_menu_y = 30

#title_menu
title_menu = pygame.image.load('pygame/Assets/title_menu.png')
title_menu_x = 720
title_menu_y = 17

#settings menu
close_img = pygame.image.load('pygame/Assets/settings/exit_icon.png')
close_img_x = 450
close_img_y = 30

#load button image
play_img = pygame.image.load('pygame/Assets/play_icon.png').convert_alpha()
levels_img = pygame.image.load('pygame/Assets/levels_icon.png').convert_alpha()
settings_img = pygame.image.load('pygame/Assets/settings_icon.png').convert_alpha()
quit_img = pygame.image.load('pygame/Assets/quit_icon.png').convert_alpha()

#create button
play_button = button.Button(520, 520, play_img, 1)
levels_button = button.Button(520, 530, levels_img, 1)
settings_button = button.Button(865, 800, settings_img, 1)
quit_button = button.Button(900, 850, quit_img, 1)
close_button = button.Button(450, 30 , close_img, 1)

#function menu
def menu():
    screen.blit(icon_menu, (icon_menu_x, icon_menu_y))
    screen.blit(title_menu, (title_menu_x, title_menu_y))

#function settings
def settings():
    menu_state == "settings"
    screen.blit(close_img, (close_img_x, close_img_y))

#looping game
running = True
while running:
    screen.fill((60, 72, 107))
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))
    if menu_state == "main":
        if settings_button.draw(screen):
            settings()
        if quit_button.draw(screen):
            running = False
    elif menu_state == "settings":
        if close_button.draw(screen):
            menu_state == "main"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
    #screen color
    menu()
    pygame.display.update()