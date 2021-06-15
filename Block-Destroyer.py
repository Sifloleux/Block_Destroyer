import time
import pygame
from pygame.locals import *
import random
import os.path
import math

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 710
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
MENU_COLOR = (14,206,246)
FPS = 60
SHOOTING_SPEED = 4
SPEED = [0, 0]
BLOCK_MOVEMENT = SCREEN_WIDTH/10
MENU_BAR_HEIGHT = 655
menu_height = SCREEN_HEIGHT - MENU_BAR_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Block Destroyer')

starting_point = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
draw_line = 0
x = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
y=[float('nan'),float('nan')]
mouse_draging = False
shoot = 0
num_of_balls = 4
NUM_of_balls = 4
block_update_time = 0
shot_already = 0
difficulty = 0
coins = 0
game_on = 1
game_on_ = 1
GAME_TITLE = True
introduction = False
introduction1 = False
main_menu = False
game_screen = False
escape_menu = False
game_over_screen = False
scoreboard = False
end_of_game = False

h_scores = open('HIGHSCORES.txt','r')
highscore_easy = h_scores.read().split(',')[0]
h_scores.close()
h_scores = open('HIGHSCORES.txt','r')
highscore_medium = h_scores.read().split(',')[1]
h_scores.close()
h_scores = open('HIGHSCORES.txt','r')
highscore_hard = h_scores.read().split(',')[2]
h_scores.close()

SCORE = 0

EASY = True
MEDIUM = False
HARD = False

if EASY:
    difficulty = 5
    num_of_balls = 4
    NUM_of_balls = 4
elif MEDIUM :
    difficulty = 8
    num_of_balls = 4
    NUM_of_balls = 4
elif HARD:
    difficulty = 8
    num_of_balls = 3
    NUM_of_balls = 3
    
set_first_rows = 0

set_diff = 1

def reload():
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 710
    WHITE = (255, 255, 255)
    RED   = (255, 0, 0)
    BLACK = (0, 0, 0)
    FPS = 60
    SHOOTING_SPEED = 4
    SPEED = [0, 0]
    BLOCK_MOVEMENT = SCREEN_WIDTH/10
    MENU_BAR_HEIGHT = 655
    menu_height = SCREEN_HEIGHT - MENU_BAR_HEIGHT
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Block Destroyer')
    
    starting_point = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
    draw_line = 0
    x = [SCREEN_WIDTH/2,SCREEN_HEIGHT-60]
    y=[float('nan'),float('nan')]
    mouse_draging = False
    shoot = 0
    num_of_balls = 4
    NUM_of_balls = 4
    block_update_time = 0
    shot_already = 0
    difficulty = 0
    coins = 0
    game_on = 1
    game_on_ = 1
    GAME_TITLE = False
    introduction = False
    introduction1 = False
    main_menu = True
    game_screen = False
    escape_menu = False
    game_over_screen = False
    scoreboard = False
    end_of_game = False    
    SCORE = 0
    
    EASY = True
    MEDIUM = False
    HARD = False
    
    if EASY:
        difficulty = 5
        num_of_balls = 4
        NUM_of_balls = 4
    elif MEDIUM :
        difficulty = 8
        num_of_balls = 4
        NUM_of_balls = 4
    elif HARD:
        difficulty = 8
        num_of_balls = 3
        NUM_of_balls = 3
        
    set_first_rows = 0
    
    set_diff = 1
    

def loadSound(name):
    fullname = os.path.join("data",name)
    sound = pygame.mixer.Sound(fullname)
    return sound

def get_speed(starting_point,pointer_point):
    hypotenuse = math.sqrt((abs(pointer_point[1]-starting_point[1]))**2 + \
                           (abs(pointer_point[0]-starting_point[0]))**2)
        
    if starting_point[0] > pointer_point[0]:
        speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]
            
    elif starting_point[0] < pointer_point[0]:
         speed = [(pointer_point[0]-starting_point[0])/hypotenuse \
                 ,-(starting_point[1]-pointer_point[1])/hypotenuse]     
    else:
        speed=[0,1]
    return speed
   
def add_ball(mouse_position, SHOOTING_SPEED,starting_point):
    speed = get_speed(starting_point,mouse_position)
    ball1 = Ball(MENU_COLOR,20,20,[SHOOTING_SPEED*speed[0],SHOOTING_SPEED*speed[1]])
    ball1.rect.x = starting_point[0] - 10
    ball1.rect.y = starting_point[1] - 10
    all_balls_list.add(ball1)
    all_balls_list.draw(screen)
    pygame.display.flip()


def hover_on_button(x,y,width,height):
    xm, ym = pygame.mouse.get_pos()
    if xm > x and xm < x + width and ym > y and ym < y + height:
        return True
    else:
        return False

def add_block_line(SCREEN_WIDTH,difficulty):
        if difficulty <= 5:
            samples = random.sample(range(10),5)
            coin = random.choice(samples)
            samples.remove(coin)
            for i in samples:   
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                
                line_a = hor_Line(RED, 1)
                line_a.rect.x = (SCREEN_WIDTH/10) * i 
                line_a.rect.y = 1
                
                line_b = hor_Line(RED, 1)
                line_b.rect.x = (SCREEN_WIDTH/10) * i 
                line_b.rect.y = (SCREEN_WIDTH/10) - 1
                
                line_c = ver_Line(RED, 1)
                line_c.rect.x = (SCREEN_WIDTH/10) * i -1
                line_c.rect.y = 1
                
                line_d = ver_Line(RED, 1)
                line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
                line_d.rect.y = 1
                
                all_vertical_list.add(line_c)
                all_vertical_list.add(line_d)
                all_horizontal_list.add(line_a)
                all_horizontal_list.add(line_b)
                all_blocks_list.add(block)
                
            block1 = Coin(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1)
            block1.rect.x = (SCREEN_WIDTH/10) * coin
            block1.rect.y = 1
            
            line_a1 = hor_Line(RED, 1)
            line_a1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_a1.rect.y = 1
            
            line_b1 = hor_Line(RED, 1)
            line_b1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_b1.rect.y = (SCREEN_WIDTH/10) - 2
            
            line_c1 = ver_Line(RED, 1)
            line_c1.rect.x = (SCREEN_WIDTH/10) * coin -1
            line_c1.rect.y = 1
            
            line_d1 = ver_Line(RED, 1)
            line_d1.rect.x = (SCREEN_WIDTH/10) * (coin+1) -2
            line_d1.rect.y = 1
            
            all_coins_list.add(block1)

                
        elif difficulty <= 15 and difficulty > 5 :
            samples = random.sample(range(10),6)
            coin = random.choice(samples)
            samples.remove(coin)
            for i in samples:   
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                
                line_a = hor_Line(RED, 1)
                line_a.rect.x = (SCREEN_WIDTH/10) * i 
                line_a.rect.y = 1
                
                line_b = hor_Line(RED, 1)
                line_b.rect.x = (SCREEN_WIDTH/10) * i 
                line_b.rect.y = (SCREEN_WIDTH/10) - 2
                
                line_c = ver_Line(RED, 1)
                line_c.rect.x = (SCREEN_WIDTH/10) * i -1
                line_c.rect.y = 1
                
                line_d = ver_Line(RED, 1)
                line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
                line_d.rect.y = 1
                
                all_vertical_list.add(line_c)
                all_vertical_list.add(line_d)
                all_horizontal_list.add(line_a)
                all_horizontal_list.add(line_b)
                all_blocks_list.add(block)
            
            block1 = Coin(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1)
            block1.rect.x = (SCREEN_WIDTH/10) * coin
            block1.rect.y = 1
            
            line_a1 = hor_Line(RED, 1)
            line_a1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_a1.rect.y = 1
            
            line_b1 = hor_Line(RED, 1)
            line_b1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_b1.rect.y = (SCREEN_WIDTH/10) - 2
            
            line_c1 = ver_Line(RED, 1)
            line_c1.rect.x = (SCREEN_WIDTH/10) * coin -1
            line_c1.rect.y = 1
            
            line_d1 = ver_Line(RED, 1)
            line_d1.rect.x = (SCREEN_WIDTH/10) * (coin+1) -2
            line_d1.rect.y = 1
            
            all_coins_list.add(block1)
            
        elif difficulty <= 25 and difficulty > 15 :
            samples = random.sample(range(10),7)
            coin = random.choice(samples)
            samples.remove(coin)
            for i in samples:   
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                
                line_a = hor_Line(RED, 1)
                line_a.rect.x = (SCREEN_WIDTH/10) * i 
                line_a.rect.y = 1
                
                line_b = hor_Line(RED, 1)
                line_b.rect.x = (SCREEN_WIDTH/10) * i 
                line_b.rect.y = (SCREEN_WIDTH/10) - 2
                
                line_c = ver_Line(RED, 1)
                line_c.rect.x = (SCREEN_WIDTH/10) * i -1
                line_c.rect.y = 1
                
                line_d = ver_Line(RED, 1)
                line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
                line_d.rect.y = 1
                
                all_vertical_list.add(line_c)
                all_vertical_list.add(line_d)
                all_horizontal_list.add(line_a)
                all_horizontal_list.add(line_b)
                all_blocks_list.add(block)
                
            block1 = Coin(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1)
            block1.rect.x = (SCREEN_WIDTH/10) * coin
            block1.rect.y = 1
            
            line_a1 = hor_Line(RED, 1)
            line_a1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_a1.rect.y = 1
            
            line_b1 = hor_Line(RED, 1)
            line_b1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_b1.rect.y = (SCREEN_WIDTH/10) - 2
            
            line_c1 = ver_Line(RED, 1)
            line_c1.rect.x = (SCREEN_WIDTH/10) * coin -1
            line_c1.rect.y = 1
            
            line_d1 = ver_Line(RED, 1)
            line_d1.rect.x = (SCREEN_WIDTH/10) * (coin+1) -2
            line_d1.rect.y = 1
            
            all_coins_list.add(block1)
        else:
            samples = random.sample(range(10),8)
            coin = random.choice(samples)
            samples.remove(coin)
            for i in samples:   
                block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,difficulty)
                block.rect.x = (SCREEN_WIDTH/10) * i
                block.rect.y = 1
                
                line_a = hor_Line(RED, 1)
                line_a.rect.x = (SCREEN_WIDTH/10) * i 
                line_a.rect.y = 1
                
                line_b = hor_Line(RED, 1)
                line_b.rect.x = (SCREEN_WIDTH/10) * i 
                line_b.rect.y = (SCREEN_WIDTH/10) - 2
                
                line_c = ver_Line(RED, 1)
                line_c.rect.x = (SCREEN_WIDTH/10) * i -1
                line_c.rect.y = 1
                
                line_d = ver_Line(RED, 1)
                line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
                line_d.rect.y = 1
                
                all_vertical_list.add(line_c)
                all_vertical_list.add(line_d)
                all_horizontal_list.add(line_a)
                all_horizontal_list.add(line_b)
                all_blocks_list.add(block)
                
            block1 = Coin(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1)
            block1.rect.x = (SCREEN_WIDTH/10) * coin
            block1.rect.y = 1
            
            line_a1 = hor_Line(RED, 1)
            line_a1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_a1.rect.y = 1
            
            line_b1 = hor_Line(RED, 1)
            line_b1.rect.x = (SCREEN_WIDTH/10) * coin 
            line_b1.rect.y = (SCREEN_WIDTH/10) - 2
            
            line_c1 = ver_Line(RED, 1)
            line_c1.rect.x = (SCREEN_WIDTH/10) * coin -1
            line_c1.rect.y = 1
            
            line_d1 = ver_Line(RED, 1)
            line_d1.rect.x = (SCREEN_WIDTH/10) * (coin+1) -2
            line_d1.rect.y = 1
            
            all_coins_list.add(block1)
    
#------------------------------------CLASSES----------------------------------  
    
class Ball(pygame.sprite.Sprite):

    
    def __init__(self, color, width, height,velocity):
        super().__init__()
        self.velocity = velocity
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.kill()




          
class hor_Line(pygame.sprite.Sprite):
     def __init__(self, color,hp):
        super().__init__()
        self.hp = hp
        self.image = pygame.Surface([SCREEN_WIDTH/10 -1, 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, BLACK, [0, 0, SCREEN_WIDTH/10 -1, 2])   
        self.rect = self.image.get_rect()
    
     def update(self):
         self.rect.y += BLOCK_MOVEMENT

             

          
class ver_Line(pygame.sprite.Sprite):
     def __init__(self, color,hp):
        super().__init__()
        self.hp = hp
        self.image = pygame.Surface([2, SCREEN_WIDTH/10 -1])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, BLACK, [0, 0, 2, SCREEN_WIDTH/10 -1])   
        self.rect = self.image.get_rect()
    
     def update(self):
         self.rect.y += BLOCK_MOVEMENT

             


class Block(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height,hp):
        super().__init__()
        self.hp = hp
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        if hp <= 5:
            pygame.draw.rect(self.image, (11, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])                 
        elif hp <= 10:
            pygame.draw.rect(self.image, (115, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 15:
            pygame.draw.rect(self.image, (206, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 20:
            pygame.draw.rect(self.image, (252, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 25:
            pygame.draw.rect(self.image, (252, 211, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 30:
            pygame.draw.rect(self.image, (252, 152, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 35:
            pygame.draw.rect(self.image, (252, 115, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 40:
            pygame.draw.rect(self.image, (252, 86, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 45:
            pygame.draw.rect(self.image, (252, 61, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 50:
            pygame.draw.rect(self.image, (252, 3, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 55:
            pygame.draw.rect(self.image, (163, 5, 5), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 60:
            pygame.draw.rect(self.image, (127, 2, 2), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 65:
            pygame.draw.rect(self.image, (103, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 70:
            pygame.draw.rect(self.image, (83, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp > 70:
            pygame.draw.rect(self.image, (73, 1, 1), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])

        self.rect = self.image.get_rect()
        #self.rect.bottom.
    
    def addHP(self,screen,hp,x,y):
        if hp >50:
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(f'{hp}', True, WHITE) 
            screen.blit(text,(x , y))
        else:
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(f'{hp}', True, BLACK) 
            screen.blit(text,(x , y))
    
    def update(self):
        self.rect.y += BLOCK_MOVEMENT
        if self.hp <=0:
             self.kill()
             
    def update_color_num(self,hp):
        if hp <= 5:
            pygame.draw.rect(self.image, (11, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 10:
            pygame.draw.rect(self.image, (115, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 15:
            pygame.draw.rect(self.image, (206, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 20:
            pygame.draw.rect(self.image, (252, 252, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 25:
            pygame.draw.rect(self.image, (252, 211, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 30:
            pygame.draw.rect(self.image, (252, 152, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 35:
            pygame.draw.rect(self.image, (252, 115, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 40:
            pygame.draw.rect(self.image, (252, 86, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 45:
            pygame.draw.rect(self.image, (252, 61, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 50:
            pygame.draw.rect(self.image, (252, 3, 3), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 55:
            pygame.draw.rect(self.image, (163, 5, 5), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 60:
            pygame.draw.rect(self.image, (127, 2, 2), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 65:
            pygame.draw.rect(self.image, (103, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp <= 70:
            pygame.draw.rect(self.image, (83, 0, 0), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
        elif hp > 70:
            pygame.draw.rect(self.image, (73, 1, 1), [0, 0, SCREEN_WIDTH/10, SCREEN_WIDTH/10])
            
             
class Coin(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
                
        pygame.draw.circle(self.image, (250,250,86), (SCREEN_WIDTH/20, SCREEN_WIDTH/20),32)   
        pygame.draw.circle(self.image, (235,235,86), (SCREEN_WIDTH/20, SCREEN_WIDTH/20),28)                    
        pygame.draw.circle(self.image, (250,250,86), (SCREEN_WIDTH/20, SCREEN_WIDTH/20),25) 
        pygame.draw.circle(self.image, (235,235,86), (SCREEN_WIDTH/20, SCREEN_WIDTH/20),12)                   
       


        self.rect = self.image.get_rect()
        #self.rect.bottom.
    
    
    def update(self):
        self.rect.y += BLOCK_MOVEMENT





mouse_draging = False
all_balls_list = pygame.sprite.Group()
all_blocks_list = pygame.sprite.Group()
all_vertical_list = pygame.sprite.Group()
all_horizontal_list = pygame.sprite.Group()
all_coins_list = pygame.sprite.Group()
destroyed = pygame.sprite.Group()
collision_x = pygame.sprite.Group()
collision_y = pygame.sprite.Group()

Ball_Launch = pygame.mixer.Sound('SOUND/ball_launch.wav')
Ball_Hit = pygame.mixer.Sound("SOUND/ball_hit.wav")
Ball_Launch.set_volume(0.3)
Ball_Hit.set_volume(0.1)

clock = pygame.time.Clock()
 
carryOn= True
while carryOn:
#---------------------------------------INTRODUCTION-----------------------------------------  
    if GAME_TITLE:
        screen.fill(BLACK)      
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    introduction = True
                    introduction1 = False
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    GAME_TITLE = False
                    
        pygame.draw.rect(screen, (252, 115, 3), (0,SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
    
        text_block1= '31'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block1, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (20,SCREEN_WIDTH/10+20)
        screen.blit(img, rect)
        
        
        pygame.draw.rect(screen, (252, 86, 3), (7 * SCREEN_WIDTH/10,SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
    
        text_block6= '36'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block6, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (7*SCREEN_WIDTH/10+17,SCREEN_WIDTH/10+20)
        screen.blit(img, rect)
        pygame.draw.line(screen,WHITE,[0,MENU_BAR_HEIGHT],[SCREEN_WIDTH,MENU_BAR_HEIGHT],2) 
        pygame.draw.rect(screen, (11, 252, 3), (3 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        pygame.draw.rect(screen, MENU_COLOR, (2 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (2.5 * SCREEN_WIDTH/10,2.5*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (4.5 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10-100,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (7.5 * SCREEN_WIDTH/10,3*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (SCREEN_WIDTH/2-10,MENU_BAR_HEIGHT-10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (5.2 * SCREEN_WIDTH/10,3.2*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (6.3 * SCREEN_WIDTH/10,7*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (3.7 * SCREEN_WIDTH/10,5.8*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (1 * SCREEN_WIDTH/10,3*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (1.3 * SCREEN_WIDTH/10,7.8*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (0.2 * SCREEN_WIDTH/10,9*SCREEN_WIDTH/10,20,20))
        
        pygame.draw.rect(screen, MENU_COLOR, (0,250,SCREEN_WIDTH,130))

        
        pygame.draw.line(screen,WHITE,[0,380],[SCREEN_WIDTH,380],2)
        pygame.draw.line(screen,WHITE,[0,250],[SCREEN_WIDTH,250],2) 
        
        text_block2= '5'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block2, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = ((SCREEN_WIDTH/2-10,MENU_BAR_HEIGHT+15))
        screen.blit(img, rect)
        
        text_block2= 'Welcome to'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block2, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (260,SCREEN_HEIGHT/2-95)
        screen.blit(img, rect)
        
        text_block2= 'BLOCK DESTROYER'               
        font = pygame.font.SysFont(None, 90)                
        img = font.render(text_block2, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (50,SCREEN_HEIGHT/2-45)
        screen.blit(img, rect)
        
        
        
        text_block2= '3'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block2, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (3*SCREEN_WIDTH/10+25,SCREEN_WIDTH/10+90)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (206, 252, 3), (4 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block3= '14'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block3, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (4*SCREEN_WIDTH/10+15,20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (206, 252, 3), (5 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block4= '12'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block4, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (5*SCREEN_WIDTH/10+15,20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (11, 252, 3), (2 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '4'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (2*SCREEN_WIDTH/10+25,20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (11, 252, 3), (2 * SCREEN_WIDTH/10,6 * SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '4'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (2*SCREEN_WIDTH/10+25,6 * SCREEN_WIDTH/10 + 20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (73, 1, 1), (7 * SCREEN_WIDTH/10,7 * SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '81'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (7*SCREEN_WIDTH/10+20,7 * SCREEN_WIDTH/10 + 20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (252, 61, 3), (8 * SCREEN_WIDTH/10,6 * SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '43'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (8*SCREEN_WIDTH/10+20,6 * SCREEN_WIDTH/10 + 20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (163, 5, 5), (8 * SCREEN_WIDTH/10,7 * SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '51'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (8*SCREEN_WIDTH/10+20,7 * SCREEN_WIDTH/10 + 20)
        screen.blit(img, rect)
        
        text_blo= "PRESS SPACE TO CONTINUE"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (210,600)
        screen.blit(img, rect)
        
        pygame.display.flip()
        
#---------------------------------INTRO--------------------------------------------        
    if introduction:
        screen.fill(BLACK)      
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    introduction = False
                    introduction1 = True
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    
        pygame.draw.rect(screen, (11, 252, 3), (0,SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
    
        text_block1= '3'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block1, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (25,SCREEN_WIDTH/10+20)
        screen.blit(img, rect)
        
        
        pygame.draw.rect(screen, (11, 252, 3), (7 * SCREEN_WIDTH/10,SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
    
        text_block6= '3'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block6, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (7*SCREEN_WIDTH/10+25,SCREEN_WIDTH/10+20)
        screen.blit(img, rect)
        pygame.draw.line(screen,WHITE,[0,MENU_BAR_HEIGHT-400],[SCREEN_WIDTH,MENU_BAR_HEIGHT-400],2) 
        pygame.draw.rect(screen, (11, 252, 3), (3 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        pygame.draw.rect(screen, MENU_COLOR, (2 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (2.5 * SCREEN_WIDTH/10,2.5*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (4.5 * SCREEN_WIDTH/10,2*SCREEN_WIDTH/10-100,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (7.5 * SCREEN_WIDTH/10,3*SCREEN_WIDTH/10,20,20))
        pygame.draw.rect(screen, MENU_COLOR, (SCREEN_WIDTH/2-10,MENU_BAR_HEIGHT-410,20,20))
        
        text_block2= '5'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block2, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = ((SCREEN_WIDTH/2-10,MENU_BAR_HEIGHT-385))
        screen.blit(img, rect)
        
        text_block2= '1'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block2, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (3*SCREEN_WIDTH/10+25,SCREEN_WIDTH/10+90)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (11, 252, 3), (4 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block3= '4'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block3, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (4*SCREEN_WIDTH/10+25,20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (11, 252, 3), (5 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block4= '4'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block4, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (5*SCREEN_WIDTH/10+25,20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (11, 252, 3), (2 * SCREEN_WIDTH/10,0,SCREEN_WIDTH/10-1,SCREEN_WIDTH/10-1))
        text_block5= '4'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_block5, True, BLACK)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (2*SCREEN_WIDTH/10+25,20)
        screen.blit(img, rect)
        
       
        
        text= '- Use left mouse button to shoot balls into incoming blocks.'              
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,310)
        screen.blit(img, rect)
        
        text_blo= "- Numbers on blocks indicate block's health"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,350)
        screen.blit(img, rect)
        
        text_blo= "- After every ball-block impact block's health is decreased"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,390)
        screen.blit(img, rect)
        
        text_blo= "  by one point. When block's health is 0 it is destroyed."          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,415)
        screen.blit(img, rect)
        
        
        text_blo= "- Number below red square indicates how many balls you"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,455)
        screen.blit(img, rect)
        
        text_blo= "  have left for this round. After this number is equal zero and all"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,480)
        screen.blit(img, rect)
        
        text_blo= "  balls hit the white line the next row of blocks is generated"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,505)
        screen.blit(img, rect)
        
        text_blo= "  with 1 health point more than previous one."          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,530)
        screen.blit(img, rect)
        
        text_blo= "- Game ends when blocks reach the white line."          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,570)
        screen.blit(img, rect)
        
        text_blo= "PRESS SPACE TO CONTINUE"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (210,660)
        screen.blit(img, rect)
        
        pygame.display.flip()
        
        
        
    if introduction1:
            
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    introduction = False
                    introduction1 = False
                    main_menu = True
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                elif event.key == K_ESCAPE:
                    introduction = True
                    introduction1 = False
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    
        pygame.draw.rect(screen, BLACK ,(0,300,SCREEN_WIDTH,400))
       
        
       
        
        text= '- Collecting points gives you more balls for shooting'              
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,310)
        screen.blit(img, rect)
        
        text_blo= "- Balls will bounce off the walls "          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,350)
        screen.blit(img, rect)
        
        text_blo= "- To speed up the ball flow click the button in bottom-right corner."          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,390)
        screen.blit(img, rect)
        
        text_blo= "  You can speed them up as much as you want. The speed will be"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,415)
        screen.blit(img, rect)
        
        
        text_blo= "  set to default after every new row."          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,440)
        screen.blit(img, rect)
        
        text_blo= "- Use mouse to navigate in menu"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,480)
        screen.blit(img, rect)
        
        text_blo= "  "          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,500)
        screen.blit(img, rect)
        
        text_blo= "  "          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,530)
        screen.blit(img, rect)
        
        text_blo= "PRESS ESCAPE TO GO BACK"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (210,620)
        screen.blit(img, rect)
        
        text_blo= "PRESS SPACE TO CONTINUE"          
        font = pygame.font.SysFont(None, 30)                
        img = font.render(text_blo, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (210,660)
        screen.blit(img, rect)
        
        pygame.display.flip()        
        
        
        
        
#-----------------------------MAIN MENU SCREEN----------------------------------------------------       
    if main_menu:
        
        screen.fill(BLACK)  

        if EASY:
            difficulty = 5
            num_of_balls = 4
            NUM_of_balls = 4
        elif MEDIUM :
            difficulty = 8
            num_of_balls = 4
            NUM_of_balls = 4
        elif HARD:
            difficulty = 8
            num_of_balls = 3
            NUM_of_balls = 3
    
    
   
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    introduction = False
                    main_menu = False
                    game_screen = True
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hover_on_button(170,100,380,70):
                    introduction = False
                    main_menu = False
                    game_screen = True
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    set_first_rows = 1
                elif hover_on_button(200,190,325,90): # EASY
                    EASY = True
                    MEDIUM = False
                    HARD = False

                    
                elif hover_on_button(200,300,325,90): #MEDIUM
                    EASY = False
                    MEDIUM = True
                    HARD = False
                    
                    
                    pygame.draw.rect(screen, (50,50,50), (200,190,325,90))
                    
                elif hover_on_button(200,410,325,90): #HARD
                    EASY = False
                    MEDIUM = False
                    HARD = True
                    
                                      
                    
                elif hover_on_button(200,530,325,75): #SCOREBOARD
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    introduction = False
                    scoreboard = True
                    
                    
                elif hover_on_button(200,620,325,65):# EXIT 
                    GAME_TITLE = False
                    introduction = False
                    introduction1 = False
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    end_of_game = True



        if EASY:
                         
            text_continue= 'MAIN MENU'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,SCREEN_HEIGHT/2-330)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (80,80,80), (160,90,400,430))
            pygame.draw.rect(screen, MENU_COLOR, (170,100,380,70))
            text_continue= 'START NEW GAME'               
            font = pygame.font.SysFont(None, 55)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-160,120)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, MENU_COLOR, (200,190,325,90))
    
            text_continue= 'EASY'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, BLACK)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,210)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,300,325,90))
    
            text_continue= 'MEDIUM'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-85,320)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,410,325,90))
    
            text_continue= 'HARD'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,440)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,530,325,75))
            
            text_continue= 'BEST SCORES'               
            font = pygame.font.SysFont(None, 60)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,550)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,620,325,65))
            
            text_continue= 'EXIT'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,630)
            screen.blit(img, rect)
            
        elif MEDIUM:
                         
            text_continue= 'MAIN MENU'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,SCREEN_HEIGHT/2-330)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (80,80,80), (160,90,400,430))
            pygame.draw.rect(screen, MENU_COLOR, (170,100,380,70))
            text_continue= 'START NEW GAME'               
            font = pygame.font.SysFont(None, 55)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-160,120)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,190,325,90))
    
            text_continue= 'EASY'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,210)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, MENU_COLOR, (200,300,325,90))
    
            text_continue= 'MEDIUM'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, BLACK)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-85,320)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,410,325,90))
    
            text_continue= 'HARD'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,440)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,530,325,75))
            
            text_continue= 'BEST SCORES'               
            font = pygame.font.SysFont(None, 60)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,550)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,620,325,65))
            
            text_continue= 'EXIT'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,630)
            screen.blit(img, rect)
            
        elif HARD:
                         
            text_continue= 'MAIN MENU'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,SCREEN_HEIGHT/2-330)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (80,80,80), (160,90,400,430))
            pygame.draw.rect(screen, MENU_COLOR, (170,100,380,70))
            text_continue= 'START NEW GAME'               
            font = pygame.font.SysFont(None, 55)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-160,120)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,190,325,90))
    
            text_continue= 'EASY'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,210)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,300,325,90))
    
            text_continue= 'MEDIUM'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-85,320)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, MENU_COLOR, (200,410,325,90))
    
            text_continue= 'HARD'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, BLACK)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,440)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,530,325,75))
            
            text_continue= 'BEST SCORES'               
            font = pygame.font.SysFont(None, 60)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-130,550)
            screen.blit(img, rect)
            
            pygame.draw.rect(screen, (50,50,50), (200,620,325,65))
            
            text_continue= 'EXIT'               
            font = pygame.font.SysFont(None, 70)                
            img = font.render(text_continue, True, WHITE)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (SCREEN_WIDTH/2-55,630)
            screen.blit(img, rect)
            
        pygame.display.flip()
        
        

        
        
        
        
        
        
        
#-----------------------------GAME PASUED SCREEN---------------------------------------------------                    
  
    if escape_menu:
        screen.fill(BLACK)        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu = False
                    game_screen = True
                    escape_menu = False
                  
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hover_on_button(200,260,325,90):
                    main_menu = False
                    game_screen = True
                    escape_menu = False
                    game_over_screen = False
                    
                elif hover_on_button(200,350,325,90):
                    main_menu = True
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    introduction = False
                    set_first_rows = 0
                    all_balls_list.empty()
                    all_blocks_list.empty()
                    all_vertical_list.empty()
                    all_horizontal_list.empty()
                    all_coins_list.empty()
                    destroyed.empty()
                    collision_x.empty()
                    collision_y.empty()
                    SCORE = 0
                    reload()
                    
                elif hover_on_button(200,460,325,110):
                    GAME_TITLE = False
                    introduction = False
                    introduction1 = False
                    main_menu = False
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    end_of_game = True
 
                                      
        text_game_paused= 'GAME PAUSED'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_paused, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-170,SCREEN_HEIGHT/2-300)
        screen.blit(img, rect)
        
        text_game_paused= f'SCORE: {SCORE}'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_paused, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-105,SCREEN_HEIGHT/2-210)
        screen.blit(img, rect)

        pygame.draw.rect(screen, (50,50,50), (200,240,325,90))

        text_continue= 'CONTINUE'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_continue, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-120,SCREEN_HEIGHT/2-90)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (50,50,50), (200,350,325,90))

        text_continue= 'MAIN MENU'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_continue, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2+20)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (50,50,50), (200,460,325,90))

        text_continue= 'EXIT'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_continue, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-45,SCREEN_HEIGHT/2+135)
        screen.blit(img, rect)
        

        
        pygame.display.flip()
                    
                    
#-----------------------------GAME OVER SCREEN------------------------------------                    
    if game_over_screen:
        screen.fill(BLACK)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    main_menu = True
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hover_on_button(100,350,525,90):
                    introduction = False
                    main_menu = True
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    set_first_rows = 0
                    all_balls_list.empty()
                    all_blocks_list.empty()
                    all_vertical_list.empty()
                    all_horizontal_list.empty()
                    all_coins_list.empty()
                    destroyed.empty()
                    collision_x.empty()
                    collision_y.empty()
                    SCORE = 0
                    reload()
                    
                    
        text_game_over= 'GAME OVER'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-140,SCREEN_HEIGHT/2-300)       
        screen.blit(img, rect)
        
        text_game_over1= f'YOUR SCORE: {SCORE }'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text_game_over1, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-125,SCREEN_HEIGHT/2-220)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (50,50,50), (100,350,525,90))

        text_continue= 'GO TO MAIN MENU'               
        font = pygame.font.SysFont(None, 65)                
        img = font.render(text_continue, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-185,SCREEN_HEIGHT/2+20)
        screen.blit(img, rect)
        
        text_continue= 'NEW HIGHSCORE!'               
        font = pygame.font.SysFont(None, 65)                
        img = font.render(text_continue, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-185,SCREEN_HEIGHT/2-120)
        screen.blit(img, rect)

        
        if EASY:
            if SCORE > int(highscore_easy):
                highscore_easy = SCORE
                f=open("HIGHSCORES.txt","w")
                f.write(f'{SCORE},{highscore_medium},{highscore_hard}')
                f.close()
                
                text_continue= 'NEW HIGHSCORE!'               
                font = pygame.font.SysFont(None, 65)                
                img = font.render(text_continue, True, MENU_COLOR)                
                rect = img.get_rect()
                rect.size=img.get_size()               
                rect.topleft = (SCREEN_WIDTH/2-185,SCREEN_HEIGHT/2-120)
                screen.blit(img, rect)
                
        elif MEDIUM:
            if SCORE > int(highscore_medium):
                highscore_medium = SCORE
                f=open("HIGHSCORES.txt","w")
                f.write(f'{highscore_easy},{SCORE},{highscore_hard}')
                f.close()
                
                text_continue= 'NEW HIGHSCORE!'               
                font = pygame.font.SysFont(None, 65)                
                img = font.render(text_continue, True, MENU_COLOR)                
                rect = img.get_rect()
                rect.size=img.get_size()               
                rect.topleft = (SCREEN_WIDTH/2-185,SCREEN_HEIGHT/2-120)
                screen.blit(img, rect)

                
        elif HARD:
            if SCORE > int(highscore_hard):
                highscore_hard = SCORE
                f=open("HIGHSCORES.txt","w")
                f.write(f'{highscore_easy},{highscore_medium},{SCORE}')
                f.close()

                text_continue= 'NEW HIGHSCORE!'               
                font = pygame.font.SysFont(None, 65)                
                img = font.render(text_continue, True, MENU_COLOR)                
                rect = img.get_rect()
                rect.size=img.get_size()               
                rect.topleft = (SCREEN_WIDTH/2-185,SCREEN_HEIGHT/2-120)
                screen.blit(img, rect)
                
        pygame.display.flip()
        
        
        
        
# ---------------------------------------SCOREBOARD------------------------------------------------
    if scoreboard:
        screen.fill(BLACK)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hover_on_button(195,580,350,80):
                    introduction = False
                    main_menu = True
                    game_screen = False
                    escape_menu = False
                    game_over_screen = False
                    scoreboard = False
                    
        text_game_over= 'HIGHSCORES'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-150,SCREEN_HEIGHT/2-340)
        screen.blit(img, rect)
        
        
        pygame.draw.rect(screen, (50,50,50), (150,80,425,480))
        
        text_game_over= 'EASY'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-60,SCREEN_HEIGHT/2-250)
        screen.blit(img, rect)
        
        text_game_over= f'{highscore_easy}'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-20,SCREEN_HEIGHT/2-190)
        screen.blit(img, rect)
        
        text_game_over= 'MEDIUM'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-90,SCREEN_HEIGHT/2-100)
        screen.blit(img, rect)
        
        text_game_over= f'{highscore_medium}'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-20,SCREEN_HEIGHT/2 -40)
        screen.blit(img, rect)
        
        text_game_over= 'HARD'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-65,SCREEN_HEIGHT/2 + 50)
        screen.blit(img, rect)
        
        text_game_over= f'{highscore_hard}'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-20,SCREEN_HEIGHT/2 + 110)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (50,50,50), (195,580,350,80))
        
        text_game_over= 'MAIN MENU'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (230,600)
        screen.blit(img, rect)
        
        pygame.display.flip()

        

#----------------------------------EXIT SCREEN------------------
    if end_of_game:
        screen.fill(BLACK)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if hover_on_button(195,280,350,80):
                    carryOn = False 

        text_game_over= 'THANK YOU FOR PLAYING'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (35,SCREEN_HEIGHT/2-220)
        screen.blit(img, rect)
        
        pygame.draw.rect(screen, (50,50,50), (195,280,350,80))
        
        text_game_over= 'EXIT GAME'               
        font = pygame.font.SysFont(None, 70)                
        img = font.render(text_game_over, True, WHITE)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (230,300)
        screen.blit(img, rect)
        
        pygame.display.flip()
#-------------------------------STARTING BLOCKS----------------------------------------
    elif set_first_rows:       
        if EASY:
            diff_lvl = 4
        elif MEDIUM:
            diff_lvl = 7
        elif HARD:
            diff_lvl = 7
        row_0 = random.sample(range(10),4)
        row_1 = random.sample(range(10),4)
        row_2 = random.sample(range(10),4)
        row_3 = random.sample(range(10),4)
        
        for i in row_0: 
            block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,diff_lvl-1)
            block.rect.x = (SCREEN_WIDTH/10) * i
            block.rect.y = (SCREEN_WIDTH/10) + 1
            
            line_a = hor_Line(RED, 1)
            line_a.rect.x = (SCREEN_WIDTH/10) * i 
            line_a.rect.y = (SCREEN_WIDTH/10) + 1
            
            line_b = hor_Line(RED, 1)
            line_b.rect.x = (SCREEN_WIDTH/10) * i 
            line_b.rect.y = (SCREEN_WIDTH/10) + (SCREEN_WIDTH/10) - 2
            
            line_c = ver_Line(RED, 1)
            line_c.rect.x = (SCREEN_WIDTH/10) * i -1
            line_c.rect.y = (SCREEN_WIDTH/10) +1
            
            line_d = ver_Line(RED, 1)
            line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
            line_d.rect.y = (SCREEN_WIDTH/10) + 1
            
            all_vertical_list.add(line_c)
            all_vertical_list.add(line_d)
            all_horizontal_list.add(line_a)
            all_horizontal_list.add(line_b)
            all_blocks_list.add(block)
            
        for i in row_1: 
            block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,diff_lvl)
            block.rect.x = (SCREEN_WIDTH/10) * i
            block.rect.y = 1
            
            line_a = hor_Line(RED, 1)
            line_a.rect.x = (SCREEN_WIDTH/10) * i 
            line_a.rect.y = 1
            
            line_b = hor_Line(RED, 1)
            line_b.rect.x = (SCREEN_WIDTH/10) * i 
            line_b.rect.y = (SCREEN_WIDTH/10) - 2
            
            line_c = ver_Line(RED, 1)
            line_c.rect.x = (SCREEN_WIDTH/10) * i -1
            line_c.rect.y = 1
            
            line_d = ver_Line(RED, 1)
            line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
            line_d.rect.y = 1
            
            all_vertical_list.add(line_c)
            all_vertical_list.add(line_d)
            all_horizontal_list.add(line_a)
            all_horizontal_list.add(line_b)
            all_blocks_list.add(block)
        
        for i in row_2: 
            block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,diff_lvl -2)
            block.rect.x = (SCREEN_WIDTH/10) * i
            block.rect.y = 2*(SCREEN_WIDTH/10) + 1
            
            line_a = hor_Line(RED, 1)
            line_a.rect.x = (SCREEN_WIDTH/10) * i 
            line_a.rect.y = 2*(SCREEN_WIDTH/10) + 1
            
            line_b = hor_Line(RED, 1)
            line_b.rect.x = (SCREEN_WIDTH/10) * i 
            line_b.rect.y = 3*(SCREEN_WIDTH/10) - 2
            
            line_c = ver_Line(RED, 1)
            line_c.rect.x = (SCREEN_WIDTH/10) * i -1
            line_c.rect.y = 2*(SCREEN_WIDTH/10) + 1
            
            line_d = ver_Line(RED, 1)
            line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
            line_d.rect.y = 2*(SCREEN_WIDTH/10) +1
            
            all_vertical_list.add(line_c)
            all_vertical_list.add(line_d)
            all_horizontal_list.add(line_a)
            all_horizontal_list.add(line_b)
            all_blocks_list.add(block)
        
        for i in row_3: 
            block = Block(WHITE,(SCREEN_WIDTH/10)-1,(SCREEN_WIDTH/10)-1,diff_lvl -3)
            block.rect.x = (SCREEN_WIDTH/10) * i
            block.rect.y = 3*(SCREEN_WIDTH/10) + 1
            
            line_a = hor_Line(RED, 1)
            line_a.rect.x = (SCREEN_WIDTH/10) * i 
            line_a.rect.y = 3*(SCREEN_WIDTH/10) + 1
            
            line_b = hor_Line(RED, 1)
            line_b.rect.x = (SCREEN_WIDTH/10) * i 
            line_b.rect.y = 4*(SCREEN_WIDTH/10) - 2
            
            line_c = ver_Line(RED, 1)
            line_c.rect.x = (SCREEN_WIDTH/10) * i -1
            line_c.rect.y = 3*(SCREEN_WIDTH/10) + 1
            
            line_d = ver_Line(RED, 1)
            line_d.rect.x = (SCREEN_WIDTH/10) * (i+1) -2
            line_d.rect.y = 3*(SCREEN_WIDTH/10) + 1
            
            all_vertical_list.add(line_c)
            all_vertical_list.add(line_d)
            all_horizontal_list.add(line_a)
            all_horizontal_list.add(line_b)
            all_blocks_list.add(block)
        set_first_rows = 0



#------------------------------------GAME SCREEN------------------------------------    
    elif game_screen:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
                  
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu = False
                    game_screen = False
                    escape_menu = True
                    game_over_screen = False
                    
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: 
                         carryOn=False
                         
                         
            elif event.type == pygame.MOUSEBUTTONUP :
                m_x,m_y = event.pos      
                if m_y > MENU_BAR_HEIGHT and m_x> MENU_BAR_HEIGHT and event.button == 1: 
                    for ball in all_balls_list:
                        ball.velocity = [ball.velocity[0] *1.5,ball.velocity[1] *1.5]
                        
                        
                elif event.button == 1 and shoot ==1:
                    mouse_x, mouse_y = event.pos 
                    mouse_draging = False
                    y[0] = y[0]
                    y[1] = y[1]
                    draw_line = 0
                    coins = len(all_coins_list)
                    if NUM_of_balls > 0:
                        add_ball([mouse_x, mouse_y],SHOOTING_SPEED,starting_point)
                        Ball_Launch.play()
                        NUM_of_balls = NUM_of_balls - 1
                    if NUM_of_balls ==0:
                        shoot= 0 
                        shot_already = 1
                        
                            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    mouse_draging = False
                    y[0] = y[0]
                    y[1] = y[1]
                    draw_line = 0 
                    shoot = 0
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_draging = True
                mouse_x, mouse_y = event.pos
                if mouse_y <MENU_BAR_HEIGHT:          
                    draw_line = 1
                    shoot = 1
    
                                       
            elif event.type == pygame.MOUSEMOTION:
                if mouse_draging:
                    mouse_x, mouse_y = event.pos
                    if mouse_y <MENU_BAR_HEIGHT:   
                        y[0] = mouse_x
                        y[1] = mouse_y
                        draw_line = 1
                    
            
                        
                        

                
            if shot_already == 1 and not all_balls_list:
                all_blocks_list.update()
                all_horizontal_list.update()
                all_vertical_list.update()
                all_coins_list.update()
                NUM_of_balls = num_of_balls
                add_block_line(SCREEN_WIDTH,difficulty)
                difficulty += 1
                SCORE += 1
                shot_already = 0           
                
                
        all_balls_list.update()
        
        
        
        if not all_balls_list and block_update_time ==1: 
            all_blocks_list.update()
            all_horizontal_list.update()
            all_vertical_list.update()
            all_coins_list.update()
        
    
        for obj in all_balls_list:           
            if obj.rect.x>=SCREEN_WIDTH:
                obj.velocity[0] = -obj.velocity[0]
            if obj.rect.x<=0:
                obj.velocity[0] = -obj.velocity[0]
            if obj.rect.y>SCREEN_HEIGHT:
                obj.velocity[1] = -obj.velocity[1]
            if obj.rect.y<0:
                obj.velocity[1] = -obj.velocity[1] 
    
        
        for hit in pygame.sprite.groupcollide(all_balls_list,all_blocks_list,0,0):
            Ball_Hit.play()
            collision_y.add(hit)
            collision_x.add(hit)
            for ball_col in pygame.sprite.groupcollide(collision_y,all_horizontal_list,0,0):
                hit.velocity[1] = - hit.velocity[1]
            for ball_col_ in pygame.sprite.groupcollide(collision_x,all_vertical_list,0,0):
                hit.velocity[0] = - hit.velocity[0]
            collision_x.empty()
            collision_y.empty()
           
            
        for hit in pygame.sprite.groupcollide(all_coins_list,all_balls_list,0,0):
            hit.kill()
            NUM_of_balls += 1
            num_of_balls += 1
            
        for hit in pygame.sprite.groupcollide(all_blocks_list,all_balls_list,0,0):
            hit.hp = hit.hp -1
            if hit.hp <=0:
                destroyed.add(hit)
                for coliding_border in pygame.sprite.groupcollide(all_vertical_list,destroyed,0,0):
                    coliding_border.kill()
                for coliding_border in pygame.sprite.groupcollide(all_horizontal_list,destroyed,0,0):
                    coliding_border.kill()
                    destroyed.empty()
                hit.kill()
            hit.update_color_num(hit.hp)
        
        #---------------------END OF GAME------------------------    
        for i in all_blocks_list:
            bottom = i.rect.bottom
            if bottom > MENU_BAR_HEIGHT:
                main_menu = False
                game_screen = False
                escape_menu = False
                game_over_screen = True
                
            
        screen.fill(BLACK)
        all_vertical_list.draw(screen)
        all_balls_list.draw(screen) 
        all_blocks_list.draw(screen)
        all_horizontal_list.draw(screen)
        all_coins_list.draw(screen)
        
        for i in all_blocks_list:
            i.addHP(screen,i.hp,i.rect.left+27 ,i.rect.top+25)
        pygame.draw.rect(screen, MENU_COLOR, [x[0]-10,x[1]-10,17,17])
            
        text1= f'{NUM_of_balls }'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text1, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (SCREEN_WIDTH/2-10,SCREEN_HEIGHT-50)
        screen.blit(img, rect)
        
        text2= f'SCORE: {SCORE }'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text2, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (10,SCREEN_HEIGHT-40)
        screen.blit(img, rect)
        
        text2= f'HIGHSCORE'               
        font = pygame.font.SysFont(None, 35)                
        img = font.render(text2, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (435,SCREEN_HEIGHT-50)
        screen.blit(img, rect)
        
        if EASY:
            text2= f'{highscore_easy }'               
            font = pygame.font.SysFont(None, 40)                
            img = font.render(text2, True, MENU_COLOR)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (500,SCREEN_HEIGHT-25)
            screen.blit(img, rect)
            
        elif MEDIUM:
            text2= f'{highscore_medium }'               
            font = pygame.font.SysFont(None, 40)                
            img = font.render(text2, True, MENU_COLOR)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (500,SCREEN_HEIGHT-25)
            screen.blit(img, rect)
        
        elif HARD:
            text2= f'{highscore_hard }'               
            font = pygame.font.SysFont(None, 40)                
            img = font.render(text2, True, MENU_COLOR)                
            rect = img.get_rect()
            rect.size=img.get_size()               
            rect.topleft = (500,SCREEN_HEIGHT-25)
            screen.blit(img, rect)
    
    

        pygame.draw.line(screen,WHITE,[0,MENU_BAR_HEIGHT],[SCREEN_WIDTH,MENU_BAR_HEIGHT],2)
        
        
        #fast-forward - button
        
        pygame.draw.rect(screen, MENU_COLOR, (SCREEN_WIDTH-(SCREEN_HEIGHT - MENU_BAR_HEIGHT),MENU_BAR_HEIGHT+4,menu_height-4,menu_height-8))
        pygame.draw.line(screen,BLACK,[655,666],[655,700],6)
        pygame.draw.line(screen,BLACK,[653,666],[690,683],6)
        pygame.draw.line(screen,BLACK,[653,700],[690,683],6)
        pygame.display.flip()
        
#-------------------------------------
        
    elif game_on ==0:
        
        screen.fill(BLACK)
        text2= f'GAME OVER SCORE:{SCORE}'               
        font = pygame.font.SysFont(None, 50)                
        img = font.render(text2, True, MENU_COLOR)                
        rect = img.get_rect()
        rect.size=img.get_size()               
        rect.topleft = (0,0)
        screen.blit(img, rect)
        pygame.display.flip()
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False 
            elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1: 
                         game_on_ = 1
        if game_on_ ==1:
            game_on =1            
clock.tick(120)
 

pygame.quit()