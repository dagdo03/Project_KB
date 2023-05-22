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
surface = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
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

closeEnd_img = pygame.image.load('pygame/Assets/gameplay/close_end.png')
closeEnd_img_y = 30

#load image for gameplay
ans_benar = pygame.image.load('pygame/Assets/gameplay/correct.png')
ans_salah = pygame.image.load('pygame/Assets/gameplay/wrong.png')
tamat_img = pygame.image.load('pygame/Assets/gameplay/congrat.png')
tamat_img_x = (screen_width/2 - tamat_img.get_width()/2)

#load button image
play_img = pygame.image.load('pygame/Assets/play_icon.png').convert_alpha()

settings_img = pygame.image.load('pygame/Assets/settings_icon.png').convert_alpha()
quit_img = pygame.image.load('pygame/Assets/quit_icon.png').convert_alpha()

back_img = pygame.image.load('pygame/Assets/gameplay/Vector.png').convert_alpha()
submit_img = pygame.image.load('pygame/Assets/gameplay/submit.png').convert_alpha()
hint_img = pygame.image.load('pygame/Assets/gameplay/hint.png')

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
levels_img = pygame.image.load('pygame/Assets/levels_icon.png').convert_alpha()
levels_button = button.Button((screen_width/2 - levels_img.get_width()/2), 570, levels_img, 1)
settings_button = button.Button(400, 400, settings_img, 1)
quit_button = button.Button((screen_width/2 - play_img.get_width()/2) - 5, 640, quit_img, 1)
close_button = button.Button(450, 30 , close_img, 1)
closeEnd_button = button.Button(tamat_img_x + 15, 113 , closeEnd_img, 1)
next_button = button.Button(screen_width - 350, screen_height - 150, next_img, 1)
hint_button = button.Button(screen_width - screen_width / 8, screen_height/25, hint_img, 1)

back_button = button.Button(screen_width / 8, screen_height / 25 , back_img, 1)
submit_button = button.Button((screen_width/2 - submit_img.get_width()/2), screen_height/3, submit_img, 1)
#text
base_font = pygame.font.Font(None,30)
user_text = ''
writeInp_text = 'Ketik Angka di sini'

#input
end_rect = pygame.Rect(0, 0, screen_width, screen_height)
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
hint_cek = False
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
    if hint_cek == True:
        
        screen.blit(hint, ((input_rect.x + 5), (input_rect.y + 250)))
        ans_hint = base_font.render(("->".join(wordPath[:count])), True, (45, 60, 104))
        screen.blit(ans_hint, ((input_rect.x + 5), (input_rect.y + 285)))
    if number == 5:
        pygame.draw.rect(surface, (0,0,0,100), end_rect)
        screen.blit(surface, (0,0))
        screen.blit(tamat_img, (tamat_img_x, 100))
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

#import button select level
title_lvl_img = pygame.image.load('pygame/Assets/gameplay/selectlevel/title.png')
title_lvl_img_x = (screen_width/2 - title_lvl_img.get_width()/2)
title_lvl_img_y = screen_height / 20

close_level_img = pygame.image.load('pygame/Assets/gameplay/selectlevel/close.png')
close_level_x = screen_width / 15
close_level_y = screen_height / 20
close_level_button = button.Button(close_level_x, close_level_y, close_level_img, 1)

bg_level = pygame.image.load('pygame/Assets/gameplay/selectlevel/background.png').convert_alpha()
bg_level_x = (screen_width/2 - bg_level.get_width()/2)
bg_level_y = screen_height / 2 - bg_level.get_height()/2

select_level_1 = pygame.image.load('pygame/Assets/gameplay/selectlevel/level1.png').convert_alpha()
select_level_1_x = bg_level.get_width() / 3.5
select_level_1_y = bg_level.get_height() /3
select_level_1_button = button.Button(select_level_1_x, select_level_1_y, select_level_1, 1)
select_level_2 = pygame.image.load('pygame/Assets/gameplay/selectlevel/level2.png').convert_alpha()
select_level_2_x = bg_level.get_width() / 2.8
select_level_2_y = bg_level.get_height() / 3
select_level_2_button = button.Button(select_level_2_x, select_level_2_y, select_level_2, 1)
#BFS
def selectLevel():
    menu_state = "levels"
    screen.blit(title_lvl_img, (title_lvl_img_x, title_lvl_img_y))
    screen.blit(bg_level, (bg_level_x, bg_level_y))
    screen.blit(close_level_img, (close_level_x, close_level_y))
    

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

# if number == 1 :
#     beginWord = "Lead"
#     endWord = "Gold"
#     wordList = ["Lock", "Loss", "Load", "Goad", "Gold"]
#     wordPath = ladderLength(beginWord, endWord, wordList)
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
        if levels_button.draw(screen):
            running = "levels"
        if play_button.draw(screen):
            number = 1
            count = 1
            if number == 1 :
                beginWord = "Lead"
                endWord = "Gold"
                wordList = ["Lock", "Loss", "Load", "Goad", "Gold"]
                wordPath = ladderLength(beginWord, endWord, wordList)
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
        # number = 1
        screen.fill((240, 240, 240))
        if back_button.draw(screen):
                ans = ''
                hint_cek = False
                user_text = ''
                # menu_state == "main"
                running = 'menu'
        # wordPath = ladderLength(beginWord, endWord, wordList)
        gameplay(count, number)
        # ans_salah = base_font.render("Anda Salah", True, (45, 60, 104))
        hint = base_font.render("Hint :", True, (45, 60, 104))
        if ans == 'benar':
            hint_cek = False
            # ans == ''
            screen.blit(ans_benar, ((input_rect.x + 285),(input_rect.y - 3)))   
            if next_button.draw(screen):
                # if number == 5:

                number += 1 
                # if number == 1 :
                #     beginWord = "Lead"
                #     endWord = "Gold"
                #     wordList = ["Lock", "Loss", "Load", "Goad", "Gold"]
                #     wordPath = ladderLength(beginWord, endWord, wordList)
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
                # if number == 5:
                #     beginWord = "Lead"
                #     endWord = "Gold"
                #     wordList = ["Lock", "Loss", "Load", "Goad", "Gold"]
                #     wordPath = ladderLength(beginWord, endWord, wordList)
                    
                ans = ''
                user_text = ''
                # screen.fill((240, 240, 240))
            count = 1
            # number = number + 1

        # count = 0
        if ans == 'salah':
            screen.blit(ans_salah, ((input_rect.x + 285),(input_rect.y - 5)))
        if hint_button.draw(screen):
            if count < 3:
                count += 1
            hint_cek = True
        if number < 5:    
            if submit_button.draw(screen):
                if user_text == str(len(wordPath)):
                    ans = 'benar'
                        # number = number + 1
                    count = 1
                elif user_text != str(len(wordPath)) and len(user_text) != 0:
                    if count < len(wordList)/2:
                        count += 1
                    ans = 'salah'
        else:
            if closeEnd_button.draw(screen):
                number = 1
    #         # menu_state == "main"
                running = 'menu'
    elif running == "levels":
        screen.fill((33, 42, 62))
        selectLevel()
        
        if close_level_button.draw(screen):
                number = 1
    #         # menu_state == "main"
                running = 'menu'
        if select_level_1_button.draw(screen):
            number = 1
            count = 1
            running = "gameplay"
        elif select_level_2_button.draw(screen):
            number = 2
            count = 1
            running = "gameplay"
    pygame.display.update()