import pygame


# Initialize Pygame
pygame.init()


# Display image
screen = pygame.display.set_mode((800,800))

# Load image
image = pygame.image.load("./data/assets/Dungeon_Tileset_at.png").convert_alpha()
screen.blit(image, (0, 0))

# Recolor image
pixels = pygame.PixelArray(image)
color = (255, 255, 255) # red
alpha = 120 # semi-transparent
pixels.replace((37, 19, 26, 255), (*color, alpha))
del pixels
screen.blit(image, (0, 400))

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
