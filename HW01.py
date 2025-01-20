import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 255, 255))

    # RENDER YOUR GAME HERE

    # ภูเขา
    pygame.draw.circle(screen, (34, 139, 34), (50, 400), 250)
    pygame.draw.circle(screen, (34, 139, 34), (400, 400), 250)
    pygame.draw.circle(screen, (34, 139, 34), (800, 400), 250)
    pygame.draw.circle(screen, (34, 139, 34), (1200, 400), 250)
    
    # พื้นดิน
    pygame.draw.rect(screen, (101, 67, 33), (0, 300, 1280, 450))

    # ดวงอาทิตย์
    pygame.draw.circle(screen, (255, 255, 0), (1000, 100), 60)
    
    # บ้าน
    pygame.draw.rect(screen, (255, 255, 255), (300, 370, 400, 300)) 
    pygame.draw.polygon(screen, (255, 0, 0), [(300, 370), (700, 370), (500, 220)])  
    pygame.draw.rect(screen, (255, 140, 0), (300, 370, 200, 300)) 
    pygame.draw.rect(screen, (218, 165, 32), (325, 470, 150, 200)) 
    pygame.draw.rect(screen, (139, 0, 0), (525, 420, 150, 100))  
    pygame.draw.rect(screen, (139, 0, 0), (525, 550, 150, 100)) 
    pygame.draw.circle(screen, (255, 0, 0), (350, 570), 10)  

    # แม่น้ำ
    pygame.draw.rect(screen, (0, 0, 255), (800, 300, 430, 200))  
    pygame.draw.ellipse(screen, (0, 0, 255), (800, 450, 430, 100)) 

    # เมฆ
    pygame.draw.ellipse(screen, (255, 255, 255), (100, 50, 150, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (150, 30, 150, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (200, 50, 150, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (500, 70, 150, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (550, 50, 150, 80))
    pygame.draw.ellipse(screen, (255, 255, 255), (600, 70, 150, 80))

    # ต้นไม้
    pygame.draw.rect(screen, (139, 69, 19), (100, 440, 30, 100)) 
    pygame.draw.circle(screen, (34, 139, 34), (115, 400), 50) 
    pygame.draw.circle(screen, (34, 139, 34), (75, 375), 20) 
    pygame.draw.circle(screen, (34, 139, 34), (160, 375), 20)  
    pygame.draw.circle(screen, (34, 139, 34), (120, 340), 20)  
    pygame.draw.circle(screen, (34, 139, 34), (160, 420), 20)  
    pygame.draw.circle(screen, (34, 139, 34), (60, 420), 20)  

    pygame.draw.rect(screen, (139, 69, 19), (1150, 500, 30, 100))  
    pygame.draw.circle(screen, (34, 139, 34), (1165, 460), 50) 
    pygame.draw.rect(screen, (139, 69, 19), (900, 550, 30, 100)) 
    pygame.draw.circle(screen, (34, 139, 34), (915, 510), 50)  
    pygame.draw.rect(screen, (139, 69, 19), (1050, 580, 30, 100))  
    pygame.draw.circle(screen, (34, 139, 34), (1065, 540), 50)  


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()