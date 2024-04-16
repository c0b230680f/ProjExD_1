import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    koka_img = pg.image.load("fig/3.png") #練習２
    koka_img = pg.transform.flip(koka_img, True, False)
    koka_rect = koka_img.get_rect()
    koka_rect.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            koka_rect.move_ip([0,-1])
        if key_lst[pg.K_DOWN]:
            koka_rect.move_ip([0,1])
        if key_lst[pg.K_RIGHT]:
            koka_rect.move_ip([1,0])
        if key_lst[pg.K_LEFT]:
            koka_rect.move_ip([-1,0])
        screen.blit(bg_img, [-tmr, 0]) #練習７
        screen.blit(bg2_img, [-tmr+1600, 0]) #練習７
        screen.blit(bg_img, [-tmr+3200, 0])
        screen.blit(koka_img,koka_rect)
        pg.display.update()
        tmr += 1        
        if tmr % 3200 == 0:
            tmr = 0
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()