import pygame
import os
import button
import collections
from collections import deque

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

icon_menu_y = 30

#title_menu
title_menu = pygame.image.load('pygame/Assets/title_menu.png')

title_menu_y = 17

#settings menu
close_img = pygame.image.load('pygame/Assets/settings/exit_icon.png')
close_img_x = 450
close_img_y = 30

#load image for gameplay
ans_benar = pygame.image.load('pygame/Assets/gameplay/correct.png')

#load button image
play_img = pygame.image.load('pygame/Assets/play_icon.png').convert_alpha()
levels_img = pygame.image.load('pygame/Assets/levels_icon.png').convert_alpha()
settings_img = pygame.image.load('pygame/Assets/settings_icon.png').convert_alpha()
quit_img = pygame.image.load('pygame/Assets/quit_icon.png').convert_alpha()

back_img = pygame.image.load('pygame/Assets/gameplay/Vector.png').convert_alpha()
submit_img = pygame.image.load('pygame/Assets/gameplay/submit.png').convert_alpha()

#load gameplay image
gameplaytitle_img = pygame.image.load('pygame/Assets/gameplay/Title.png')
gameplaytitle_x = (screen_width/2 - gameplaytitle_img.get_width()/2)
gameplaytitle_y = 17

next_img = pygame.image.load('pygame/Assets/gameplay/next.png')

#load wordlistlvl 1 
lvl1_img = pygame.image.load('pygame/Assets/gameplay/levels/level1.png')
lvl2_img = pygame.image.load('pygame/Assets/gameplay/levels/level2.png')
lvl3_img = pygame.image.load('pygame/Assets/gameplay/levels/level3.png')
lvl4_img = pygame.image.load('pygame/Assets/gameplay/levels/level4.png')
#create button
play_button = button.Button((screen_width/2 - play_img.get_width()/2), 500, play_img, 1)
levels_button = button.Button(520, 530, levels_img, 1)
settings_button = button.Button(400, 400, settings_img, 1)
quit_button = button.Button((screen_width/2 - play_img.get_width()/2) - 7, 570, quit_img, 1)
close_button = button.Button(450, 30 , close_img, 1)
next_button = button.Button(screen_width - 200, screen_height - 150, next_img, 1)

back_button = button.Button((screen_width-1150), 30 , back_img, 1)
submit_button = button.Button((screen_width/2 - submit_img.get_width()/2), screen_height/3, submit_img, 1)
#text
base_font = pygame.font.Font(None,32)
user_text = ''
writeInp_text = 'Write your answer here'

#input
# input_rect = pygame.Rect(200, 200, 280, 32)
color = (0,0,0)

# count = 1
#function menu
def menu():
    icon_menu_x = screen_width/2 - icon_menu.get_width()/2
    title_menu_x = screen_width/2 - title_menu.get_width()/2
    screen.blit(icon_menu, (icon_menu_x, icon_menu_y))
    screen.blit(title_menu, (title_menu_x, title_menu_y))

#function settings
def settings():
    menu_state == "settings"
    screen.blit(close_img, (close_img_x, close_img_y))
number = 1
#function gameplay
#looping game
count = 1
active = False
running = "menu"
ans = ''
def gameplay(count, number):
    menu_state == "gameplay"
    # input_rect = pygame.Rect(screen_width/2-140, 200, 280, 32)
    pygame.draw.rect(screen, color, input_rect, 2)
    if number == 1:
        screen.blit(lvl1_img, (screen_width/9, screen_height/6))
    elif number == 2:
        screen.blit(lvl2_img, (screen_width/9, screen_height/6))
    elif number == 3:
        screen.blit(lvl3_img, (screen_width/9, screen_height/6))
    elif number == 4:
        screen.blit(lvl4_img, (screen_width/9, screen_height/6))
    screen.blit(gameplaytitle_img, (gameplaytitle_x, gameplaytitle_y))
    text_surface = base_font.render(user_text, True, (45, 60, 104))
    text_writeInp = base_font.render(writeInp_text, True, (45, 60, 104))
    # ans_benar = base_font.render("Anda Benar", True, (45, 60, 104))
    # ans_salah = base_font.render("Anda Salah", True, (45, 60, 104))
    # hint = base_font.render("Hint :", True, (45, 60, 104))
    screen.blit(text_surface, ((input_rect.x + 5), (input_rect.y + 5)))
    if len(user_text) == 0 and active == False:
        screen.blit(text_writeInp, ((input_rect.x + 5), (input_rect.y + 5)))
    
    # if ans == 'benar':
    #     screen.blit(ans_benar, ((input_rect.x + 5), (input_rect.y + 200)))   
    #     if next_button.draw(screen):
    #         ans == ''
    #         number += 1 
    #         if number == 2:

    #     count = 1
    #         # number = number + 1

    #     # count = 0
    # if ans == 'salah':
    #     screen.blit(ans_salah, ((input_rect.x + 5), (input_rect.y + 200)))
    #     screen.blit(hint, ((input_rect.x + 5), (input_rect.y + 250)))
    #     ans_hint = base_font.render(("->".join(wordPath[:count])), True, (45, 60, 104))
    #     screen.blit(ans_hint, ((input_rect.x + 5), (input_rect.y + 285)))
    # screen.fill((240, 240, 240))



#BFS


def ladderLength(beginWord: str, endWord: str, wordList):
    if endWord not in wordList:
        return 0
    
    nei = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)
            
    visit = {beginWord: None}  # store the parent node of beginWord as None
    q = deque([beginWord])
    while q:
        word = q.popleft()
        if word == endWord:
            # construct the path by backtracking from endWord to beginWord
            path = [endWord]
            while word != beginWord:
                path.append(visit[word])
                word = visit[word]
            return path[::-1]  # reverse the path to get it from beginWord to endWord
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            for neiWord in nei[pattern]:
                if neiWord not in visit:
                    visit[neiWord] = word  # store the parent node of neiWord
                    q.append(neiWord)
    return []

if number == 1 :
    beginWord = "Lead"
    endWord = "Gold"
    wordList = ["Lock", "Loss", "Load", "Goad", "Gold"]
    wordPath = ladderLength(beginWord, endWord, wordList)
while True:
    screen_width = pygame.display.get_surface().get_width()
    input_rect = pygame.Rect(screen_width/2-140, 200, 280, 32)
    # screen.fill((60, 72, 107))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN and running == 'gameplay':
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if user_text == str(len(wordPath)):
                        ans = 'benar'
                        
                        # number += 1
                        count = 1
                    elif user_text != str(len(wordPath)) and len(user_text) != 0:
                        if count < len(wordList)/2:
                            count += 1
                        ans = 'salah'
                else:
                    user_text += event.unicode
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))
    if running == "menu":
        screen.fill((60, 72, 107))
        menu()
        # if settings_button.draw(screen):
        #     # settings()
        #     running = 'setting'
        if quit_button.draw(screen):
            exit()
        if play_button.draw(screen):
            running = 'gameplay'
            
    # if menu_state == "main":
    #     menu()
    #     if settings_button.draw(screen):
    #         settings()
    #     if quit_button.draw(screen):
    #         running = False
    # elif menu_state == "settings":
    # elif running == 'setting':
    #     screen.fill((60, 72, 107))
    #     if close_button.draw(screen):
    #         # menu_state == "main"
    #         running = 'menu'
    elif running == 'gameplay':
        screen.fill((240, 240, 240))
        if back_button.draw(screen):
                # menu_state == "main"
                running = 'menu'
        # wordPath = ladderLength(beginWord, endWord, wordList)
        gameplay(count, number)
        ans_salah = base_font.render("Anda Salah", True, (45, 60, 104))
        hint = base_font.render("Hint :", True, (45, 60, 104))
        if ans == 'benar':
            # ans == ''
            screen.blit(ans_benar, ((input_rect.x + 285),(input_rect.y - 3)))   
            if next_button.draw(screen):
                # if number == 5:

                number += 1 
                if number == 2:
                    beginWord = "Ball"
                    endWord = "Goat"
                    wordList = ["Fall", "Bell", "Bail", "Belt", "Bolt", "Boat", "Goat"]
                    wordPath = ladderLength(beginWord, endWord, wordList)
                elif number == 3:
                    beginWord = "Hand"
                    endWord = "Font"
                    wordList = ["Band", "Bane", "Bond", "Boat", "Fond", "Foot", "Font"]
                    wordPath = ladderLength(beginWord, endWord, wordList)
                elif number == 4:
                    beginWord = "Wheat"
                    endWord = "Break"
                    wordList = ["Wheel", "Cheat", "Clear", "Cleat", "Bleat", "Bread", "Bleak", "Bleed", "Break"]
                    wordPath = ladderLength(beginWord, endWord, wordList)
                ans = ''
                # screen.fill((240, 240, 240))
            count = 1
            # number = number + 1

        # count = 0
        if ans == 'salah':
            screen.blit(ans_salah, ((input_rect.x + 5), (input_rect.y + 200)))
            screen.blit(hint, ((input_rect.x + 5), (input_rect.y + 250)))
            ans_hint = base_font.render(("->".join(wordPath[:count])), True, (45, 60, 104))
            screen.blit(ans_hint, ((input_rect.x + 5), (input_rect.y + 285)))
            
        if submit_button.draw(screen):
            if user_text == str(len(wordPath)):
                ans = 'benar'
                    # number = number + 1
                count = 1
            elif user_text != str(len(wordPath)) and len(user_text) != 0:
                if count < len(wordList)/2:
                    count += 1
                ans = 'salah'
    pygame.display.update()