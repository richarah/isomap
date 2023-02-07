import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size and title
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Isometric Tiles")

# Define some colors
FILL_COLOR = (0, 128, 0)
OUTLINE_COLOR = (0, 92, 0)

# Base cube size
cube_size = 100

# Camera
camera_x = 0
camera_y = 0
zoom = 1

# Define a function to convert 3D coordinates to 2D coordinates
def iso_3d_to_2d(x, y, z):
    screen_x = x - y
    screen_y = (x + y) / 2 - z
    return (screen_x, screen_y)

# Define a function to draw a cube
def draw_cube(screen, x, y, z, size, FILL_COLOR):
    # Define the vertices of the cube
    vertices = [
        (x, y, z),
        (x + size, y, z),
        (x + size, y + size, z),
        (x, y + size, z),
    ]

    # Convert the vertices from 3D to 2D coordinates
    vertices = [iso_3d_to_2d(v[0], v[1], v[2]) for v in vertices]

    # Draw the top face of the cube
    pygame.draw.polygon(screen, FILL_COLOR, vertices)
    pygame.draw.polygon(screen, OUTLINE_COLOR, vertices, 1)

# Generate the island of cubes
def generate_island(cube_size, zoom):
    island = []
    for i in range(-10, 10):
        for j in range(-10, 10):
            x = i * cube_size * zoom
            y = j * cube_size * zoom
            z = 0
            island.append((x, y, z))
    return island
    

# Initialize the island of cubes
island = generate_island(cube_size, zoom)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_PLUS]:
        zoom *= 1.1
    elif keys[pygame.K_MINUS]:
        zoom *= 0.9
    elif keys[pygame.K_UP]:
        camera_x += 10
        camera_y += 10
    elif keys[pygame.K_DOWN]:
        camera_x -= 10
        camera_y -= 10
    elif keys[pygame.K_LEFT]:
        camera_x += 10
        camera_y -= 10
    elif keys[pygame.K_RIGHT]:
        camera_x -= 10
        camera_y += 10

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a "grid" of cubes
    for i in range(-10, 10):
        for j in range(-10, 10):
            x = i * cube_size * zoom
            y = j * cube_size * zoom
            draw_cube(screen, x + camera_x, y + camera_y, 0, cube_size * zoom, FILL_COLOR)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()

# Quit Pygame
pygame.quit()

