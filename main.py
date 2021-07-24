from classes import *

player1 = Player(0, 512)
enemy1 = Enemy()
# player2 = Player(200, 300)


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    player1.get_keys()
    player1.draw()
    # player1.check_enemy(enemy1)
    enemy1.draw()
    pygame.display.flip()

pygame.quit()
