import pygame
import math

def run_doom_game():
    # Inicializa o Pygame
    pygame.init()

    # --- Configurações do Jogo ---
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Doom")

    # Cores
    WALL_COLOR = (200, 200, 200) # Cinza claro para as paredes
    FLOOR_COLOR = (100, 100, 100) # Cinza escuro para o chão
    CEILING_COLOR = (50, 50, 50) # Cinza muito escuro para o teto

    # --- Posição e Movimentação do Jogador ---
    player_x, player_y = 1.5, 1.5 # Posição inicial (em coordenadas do mapa)
    player_angle = 0 # Ângulo inicial de visão (em radianos)
    fov = math.pi / 3 # Campo de visão (60 graus)
    move_speed = 0.05
    rotation_speed = 0.03

    # --- Mapa do Jogo ---
    game_map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    map_size = len(game_map)

    # --- Loop Principal do Jogo ---
    running = True
    while running:
        # --- Eventos do Jogo ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        
        # --- Lógica de Movimentação do Jogador ---
        keys = pygame.key.get_pressed()
        
        # Frente/Trás
        if keys[pygame.K_w]:
            player_x += move_speed * math.cos(player_angle)
            player_y += move_speed * math.sin(player_angle)
        if keys[pygame.K_s]:
            player_x -= move_speed * math.cos(player_angle)
            player_y -= move_speed * math.sin(player_angle)
            
        # Rotação
        if keys[pygame.K_a]:
            player_angle -= rotation_speed
        if keys[pygame.K_d]:
            player_angle += rotation_speed
        
        # --- Limpeza da Tela (Desenha o céu e o chão) ---
        screen.fill(CEILING_COLOR)
        pygame.draw.rect(screen, FLOOR_COLOR, (0, screen_height // 2, screen_width, screen_height // 2))

        # --- Algoritmo de Ray-Casting ---
        for col in range(screen_width):
            ray_angle = (player_angle - fov / 2) + (col / screen_width) * fov
            
            # Posição inicial do raio
            ray_x, ray_y = player_x, player_y
            
            # Direção do raio
            cos_angle = math.cos(ray_angle)
            sin_angle = math.sin(ray_angle)
            
            # Encontrar a parede
            hit_wall = False
            distance = 0
            while not hit_wall and distance < 20: # Limite de distância para evitar loops infinitos
                distance += 0.01
                test_x = int(player_x + distance * cos_angle)
                test_y = int(player_y + distance * sin_angle)
                
                if 0 <= test_x < map_size and 0 <= test_y < map_size:
                    if game_map[test_y][test_x] == 1:
                        hit_wall = True

            # --- Renderização da Parede ---
            if hit_wall:
                # Corrigir o "fisheye" (olho de peixe)
                distance_to_wall = distance * math.cos(player_angle - ray_angle)
                
                # Calcular a altura da fatia da parede
                wall_height = screen_height / (distance_to_wall + 0.001) 
                
                # Determinar onde desenhar a fatia
                wall_top = screen_height / 2 - wall_height / 2
                wall_bottom = screen_height / 2 + wall_height / 2
                
                # Desenhar a fatia da parede
                pygame.draw.line(screen, WALL_COLOR, (col, wall_top), (col, wall_bottom), 1)

        # --- Atualizar a Tela ---
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run_doom_game()