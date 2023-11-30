import pygame

pygame.init()

Screen_Width = 900
Screen_Height = 500

screen = pygame.display.set_mode((Screen_Width, Screen_Height))

player = pygame.Rect((300,250,50,50))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        screen.fill((255,255,255))

        pygame.draw.rect(screen, (255, 0, 0), player)

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            player.move_ip(-10, 0)
        elif key[pygame.K_d] == True:
            player.move_ip(10, 0)
        elif key[pygame.K_w] == True:
            player.move_ip(0, -10)
        elif key[pygame.K_s] == True:
            player.move_ip(0,10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
main()