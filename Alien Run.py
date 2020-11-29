import pygame 
import random
import os
import time

pygame.init()
pygame.mixer.init()


display=pygame.display.set_mode((1000,800))
start_ticks=pygame.time.get_ticks()

# text function
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])

def start():
    display=pygame.display.set_mode((1000,800))
    running=True
    #Background Image
    bgimg = pygame.image.load("start.jpg")
    bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
    display.blit(bgimg, (0, 0))
    pygame.display.update()
    # Color
    green=(255,255,255)
    pygame.display.set_caption("game2 | start")
    text_screen("Welcome to Alien Run", green, 300, 300)
    text_screen("Press Space Bar To Play", green, 270, 370)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        mainloop()
                        running=False
running=True
def mainloop():
    start=1200
    pygame.display.set_caption("Aline Run")
# gun positions
    gun_position_y=200
    gun_position_x=20
    gun_v_y=0
# bull positions
    bull_position_x=105
    bull_v_x=0
# boll_position
    boll_position_y=790
    boll_v_y=15
# range
    range1=9
# Color
    green=(0,255,0)
    red=(255,0,0)
# mainloop
    global score
    global hiscore
    score=0
    hiscore=0
    live=3
    pygame.display.update()
    boll_position_x=random.randint(200,700)
    boll=True
    bull=False
    clock=pygame.time.Clock()
    while boll:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()
                elif event.key==pygame.K_a:
                    pygame.mixer.music.load('gun2.mp3')
                    pygame.mixer.music.play()
                    bull=True
                elif event.key==pygame.K_F1 :
                    range1=90
                    pygame.display.update()
                elif event.key==pygame.K_DELETE :
                    score+=10
                    pygame.display.update()
                elif event.key==pygame.K_F2 :
                    range1=10
                    bull_position_x=105
                    pygame.mixer.music.load('Beefy.mp3')
                    pygame.mixer.music.play()
                    pygame.display.update()
                elif event.key==pygame.K_UP:
                    gun_v_y=-20
                elif event.key==pygame.K_DOWN:
                    gun_v_y=20
            elif gun_position_y<1000:
                gun_v_y=0
            elif gun_position_y==0:
                gun_v_y=0
        if bull==True:
            for i in range(range1):
                if range1==90:
                    pygame.mixer.music.load('Beefy.mp3')
                    pygame.mixer.music.play()
                pygame.draw.circle(display, red, [bull_position_x,gun_position_y+42],5,5)
                bull_v_x=20
                pygame.display.update()

                bull_position_x=bull_position_x+bull_v_x

                if bull_position_x>1000:
                    bull_v_x=0
                    bull=False
                    bull_position_x=105 

        if boll_position_y<23:
            boll_position_x=random.randint(200,700)
            live-=1
            pygame.mixer.music.load('livelost.mp3')
            pygame.mixer.music.play()
            boll_position_y=790
            time.sleep(3)
            pygame.display.update()
        if live==0:
            boll=False
            with open("hiscroe.txt","w") as f:
                f.write(str(score))
            gameover()
            f.close()
        if  (bull_position_x-boll_position_x)>0 and abs(gun_position_y-boll_position_y)<60:
            boll_position_y=800
            boll_position_x=random.randint(200,700)
            score+=1
            pygame.mixer.music.load('beep.mp3')
            pygame.mixer.music.play()
        bgimg = pygame.image.load("mainbg.jpg")
        bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
        display.blit(bgimg, (0, 0))
        text_screen(f"Score:{score}", green, 0, 5)
        text_screen(f"Time:{start}ms", green, 230, 5)
        text_screen(f"lives:{live}", green, 520, 5)
        start-=1
        if start==0:
            time_out()
        clock.tick(20)

        bgimg2 = pygame.image.load('klipartz.com.png')
        bgimg2 = pygame.transform.scale(bgimg2, (120, 80)).convert_alpha()
        display.blit(bgimg2, (gun_position_x,gun_position_y))

        bgimg2 = pygame.image.load('hiclipart.com.png')
        bgimg2 = pygame.transform.scale(bgimg2, (90, 70)).convert_alpha()
        display.blit(bgimg2, (boll_position_x,boll_position_y))

        boll_position_y=boll_position_y-boll_v_y
        gun_position_y=gun_position_y+gun_v_y
        pygame.display.update()

def time_out():
    running=True
    red=(255,0,0)
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    quit()
                elif event.key==pygame.K_RETURN:
                    running=False
                    mainloop()
        pygame.display.set_mode((1000,800))
        bgimg = pygame.image.load("timeover.jpg")
        bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
        display.blit(bgimg, (0, 0))
        pygame.display.set_caption("game2 | start")
        text_screen("Time Out!!!", red, 410, 270)
        text_screen(f"Your Score is:{score}", red, 360, 330)
        text_screen("Press Enter Bar To Play", red, 285, 390)
        pygame.display.update()
        


def gameover():
    running=True
    red=(255,0,0)
    display=pygame.display.set_mode((1000,800))
    pygame.display.set_caption("game2 | Game_Over")
    bgimg = pygame.image.load("gameover.jpg")
    bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
    display.blit(bgimg, (0, 0))
    text_screen("GameOver", red, 390, 330)
    text_screen("Press Enter To Play Again", red, 250, 400)
    text_screen(f"Your scroe {score}", red, 375, 470)
    pygame.display.update()
    while running:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    mainloop()
            elif score<10:
                pygame.mixer.music.load('noob.mp3')
                pygame.mixer.music.play()
            elif score>10:
                pygame.mixer.music.load('app-19.mp3')
                pygame.mixer.music.play()
        pygame.display.update()
    
            
            
if __name__ == "__main__":

    start()
