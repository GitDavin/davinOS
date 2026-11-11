import pygame
import sys

# 1. Initialize Graphical Engine Canvas
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DAVIN OS v3.0 - DuckDuckGo Edition")
clock = pygame.time.Clock()

# Color Palettes (DuckDuckGo Theme)
MAC_BLUE = (52, 152, 219)
DARK_GRAY = (44, 62, 80)
LIGHT_GRAY = (235, 238, 242)
WHITE = (255, 255, 255)
RED_BUTTON = (231, 76, 60)
DDG_ORANGE = (222, 94, 49)      
DDG_DARK = (48, 48, 48)          
DDG_GREEN = (63, 138, 62)        

# System Fonts
font = pygame.font.SysFont("Arial", 16)
bold_font = pygame.font.SysFont("Arial", 16, bold=True)
large_font = pygame.font.SysFont("Arial", 22, bold=True)

# 2. Simplified App State Switches (Zero Tuple Math)
browser_open = True
search_query = "Search privately..."
search_active = False
current_view = "home"
fire_flashing = 0

# Fixed Application Borders
browser_rect = pygame.Rect(100, 80, 600, 440)
desktop_icon_rect = pygame.Rect(30, 50, 80, 80)

# Mock Data for Search Queries
results = [
    {"title": "Welcome to DuckDuckGo", "url": "https://duckduckgo.com", "snippet": "The internet privacy company that empowers you to control your data."},
    {"title": "ASUS Chromebook CX15 Specs", "url": "https://asus.com", "snippet": "Lightweight laptop running ChromeOS with efficiency processors."},
    {"title": "Pygame Project Hub", "url": "https://pygame.org", "snippet": "A free and open-source Python library for coding desktop operating system mocks!"}
]

# 3. Core Processing Loop Engine
while True:
    # Get direct pixel integers to prevent coordinate tuple bugs
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Rock-solid click routing handlers
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Click 1: Desktop application shortcut box
            if desktop_icon_rect.collidepoint(mx, my):
                browser_open = True
                
            if browser_open:
                # Click 2: Close circle coordinates 
                if mx >= 102 and mx <= 114 and my >= 80 and my <= 92:
                    browser_open = False
                    
                # Click 3: Inside Address Input bar
                elif mx >= 185 and mx <= 575 and my >= 114 and my <= 138:
                    search_active = True
                    if search_query == "Search privately...":
                        search_query = ""
                else:
                    search_active = False

                # Click 4: 🔥 DuckDuckGo Flame "Fire Button"
                if mx >= 585 and mx <= 611 and my >= 113 and my <= 139:
                    fire_flashing = 12
                    search_query = "Search privately..."
                    current_view = "home"

        # Safe keyboard input loops
        elif event.type == pygame.KEYDOWN and search_active:
            if event.key == pygame.K_RETURN:
                search_active = False
                if search_query.strip() != "":
                    current_view = "results"
            elif event.key == pygame.K_BACKSPACE:
                search_query = search_query[:-1]
            else:
                search_query += event.unicode

    # 4. DRAW GRAPHICS LAYERS
    screen.fill(MAC_BLUE) 

    # Draw Global Top Apple Menu Bar
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, 26))
    pygame.draw.line(screen, (160, 160, 160), (0, 26), (SCREEN_WIDTH, 26))
    menu_surface = font.render("   DavinOS  File  Edit  View  Go  Privacy  Help", True, (0, 0, 0))
    screen.blit(menu_surface, (5, 4))
    clock_surface = font.render("12:00 PM  ", True, (0, 0, 0))
    screen.blit(clock_surface, (SCREEN_WIDTH - 75, 4))

    # Draw Desktop Shortcut Icon Widget
    pygame.draw.rect(screen, (255, 255, 255, 100), desktop_icon_rect, border_radius=12)
    pygame.draw.rect(screen, WHITE, desktop_icon_rect, width=1, border_radius=12)
    icon_txt = font.render("🦆 DuckOS", True, WHITE)
    screen.blit(icon_txt, (desktop_icon_rect.x + 8, desktop_icon_rect.y + 30))

    # Draw Browser Frame Window Component
    if browser_open:
        pygame.draw.rect(screen, LIGHT_GRAY, browser_rect, border_radius=6)
        pygame.draw.rect(screen, WHITE, (browser_rect.x, browser_rect.y, browser_rect.width, 24), border_top_left_radius=6, border_top_right_radius=6)
        pygame.draw.line(screen, (200, 200, 200), (browser_rect.x, browser_rect.y + 24), (browser_rect.x + browser_rect.width, browser_rect.y + 24))

        # Close button circle
        pygame.draw.circle(screen, RED_BUTTON, (108, 86), 6)
        title_lbl = font.render("DuckDuckGo Privacy Browser", True, DDG_DARK)
        screen.blit(title_lbl, (browser_rect.x + 26, browser_rect.y + 4))

        # Navigation Header rows
        pygame.draw.rect(screen, WHITE, (browser_rect.x, browser_rect.y + 25, browser_rect.width, 42))
        pygame.draw.line(screen, (210, 210, 210), (browser_rect.x, browser_rect.y + 67), (browser_rect.x + browser_rect.width, browser_rect.y + 67))
        nav_arrows = font.render(" ◀   ▶ ", True, (120, 120, 120))
        screen.blit(nav_arrows, (browser_rect.x + 12, browser_rect.y + 36))

        # Input text address field
        input_bg = (255, 255, 240) if search_active else (245, 246, 248)
        pygame.draw.rect(screen, input_bg, (185, 114, 390, 24), border_radius=12)
        pygame.draw.rect(screen, (200, 200, 200), (185, 114, 390, 24), width=1, border_radius=12)
        query_surface = font.render(search_query, True, (0, 0, 0) if search_query != "Search privately..." else (140, 140, 140))
        screen.blit(query_surface, (199, 117))

        # 🔥 Flame Fire Button
        btn_color = DDG_ORANGE if fire_flashing == 0 or fire_flashing % 4 < 2 else WHITE
        pygame.draw.circle(screen, btn_color, (598, 126), 13)
        flame_icon = font.render("🔥", True, WHITE)
        screen.blit(flame_icon, (589, 115))
        if fire_flashing > 0:
            fire_flashing -= 1

        # Render website main window sheets
        web_area = pygame.Rect(browser_rect.x + 10, browser_rect.y + 76, browser_rect.width - 20, browser_rect.height - 86)
        pygame.draw.rect(screen, WHITE, web_area, border_radius=4)

        if current_view == "home":
            # 🌟 SPLIT THE MATH SO IT NEVER CAUSES A TUPLE ERROR AGAIN! 🌟
            logo_x = web_area.x + (web_area.width // 2)
            logo_y = web_area.y + 80
            
            pygame.draw.circle(screen, DDG_ORANGE, (logo_x, logo_y), 30)
            logo_txt = large_font.render("🦆", True, WHITE)
            screen.blit(logo_txt, (logo_x - 14, logo_y - 16))
            
            brand_lbl = large_font.render("DuckDuckGo", True, DDG_DARK)
            screen.blit(brand_lbl, (logo_x - 65, logo_y + 40))
            
            sub_lbl = font.render("The internet privacy company that doesn't track you.", True, (100, 100, 100))
            screen.blit(sub_lbl, (logo_x - 165, logo_y + 75))

        elif current_view == "results":
            y_offset = web_area.y + 15
            header_lbl = bold_font.render(f"Privacy Search Results for: '{search_query}'", True, DDG_DARK)
            screen.blit(header_lbl, (web_area.x + 15, y_offset))
            y_offset += 30

            for res in results:
                res_title = bold_font.render(res["title"], True, DDG_ORANGE)
                screen.blit(res_title, (web_area.x + 15, y_offset))
                res_url = font.render(res["url"], True, DDG_GREEN)
                screen.blit(res_url, (web_area.x + 15, y_offset + 18))
                res_snip = font.render(res["snippet"], True, DARK_GRAY)
                screen.blit(res_snip, (web_area.x + 15, y_offset + 34))
                y_offset += 65

    pygame.display.flip()
    clock.tick(60)

