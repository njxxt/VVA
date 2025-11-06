import pygame
import sys
import os
import glob
import time

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
shir, hit = info.current_w - 500 , info.current_h - 200
scrin = pygame.display.set_mode((shir, hit))



class funcmain:
    def __init__(self):

        self.fil = "4503373.mp3"

        self.sound_now = False

        self.images = self.downo_im("ajrnb")

        self.chang_im = 0

        self.count_time = 0
        self.autocl = 1.5
        self.blokclik = False
        self.count = 0

        self.timer = 0
        self.interv = 2.4

        self.block_m = False

        self.tex = pygame.font.SysFont(name='Colibri', size=36)

    def downo_im(self, anyy):
        images = []



        for i in ['*.png', '*.jpg']:
            for file_path in glob.glob(os.path.join(anyy, i)):
                image = pygame.image.load(file_path)
                images.append(image)


        return images

    def sound_pl(self):
        if not self.sound_now:
            pygame.mixer.Sound(self.fil).play()
            self.sound_now = True

    def im_pl(self):
        if self.images:
            self.chang_im = (self.chang_im + 1) % len(self.images)

    def block_cl(self):

        if self.block_m:
            return

        real_time = time.time()
        different_cl = real_time - self.count_time

        if different_cl < self.autocl:
            self.count += 1

            if self.count >= 2 and not self.blokclik:

                self.blokclik = True
                self.timer = real_time

                self.block_m = True

                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)



        else:
            self.count = 0

        self.count_time = real_time

        if not self.blokclik:
            if not self.sound_now:
                self.sound_pl()
            else:
                self.im_pl()

    def auto_im(self):
        if self.blokclik:
            real_t = time.time()
            if real_t - self.timer >= self.interv:
                self.im_pl()
                self.timer = real_t

    def end_block(self):
        if self.blokclik:
            current_time = time.time()
            if current_time - self.count_time > 30.0:
                self.blokclik = False
                self.count = 0

                self.block_m = False
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)

    def change_im(self):

        im_real = self.images[self.chang_im]

        fix_s_im, fix_h_im = im_real.get_size()


        mn = min((shir - 100) / fix_s_im, (hit - 100) / fix_h_im)
        return pygame.transform.smoothscale(im_real, (int(fix_s_im * mn), int(fix_h_im * mn)))



    def draw(self, screen):
        black = (0, 0, 0)
        red = (255, 50, 50)


        screen.fill(black)

        current_image = self.change_im()
        if current_image:
            img_rect = current_image.get_rect()
            img_rect.center = (shir // 2, hit // 2)
            screen.blit(current_image, img_rect)

        if self.blokclik:
            t = self.tex.render("U clik very ofen!", True, red)

            x = t.get_rect()
            x.centerx = shir // 2
            x.bottom = hit -10


            screen.blit(t, x)


def main():
    blok_re = pygame.time.Clock()
    user = funcmain()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    user.block_cl()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        user.auto_im()
        user.end_block()
        user.draw(scrin)
        pygame.display.flip()
        blok_re.tick(60)


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()