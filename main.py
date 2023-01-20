import pygame
pygame.init()
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Foor Georg-Johann Seeder")
screen.fill
([0, 0, 0])
pygame.draw.circle(screen, [255, 255, 0],  [150, 60], 10, 0)
pygame.draw.circle(screen, [255, 0, 0], [150, 30], 10, 0)
pygame.draw.circle(screen, [0, 255, 0], [150, 90], 10, 0)
pygame.draw.rect(screen, [128, 128, 128], [135, 15, 30, 90], 2)
pygame.draw.line(screen, [192,192,192], [115,250], [145,220], 2)
pygame.draw.line(screen, [192,192,192], [155,220], [185,250], 2)
pygame.draw.line(screen, [192,192,192], [115,250], [185,250], 2)
pygame.draw.line(screen, [192,192,192], [155,220], [155,105], 2)
pygame.draw.line(screen, [192,192,192], [145,220], [145,105], 2)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()