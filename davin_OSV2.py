import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DAVIN OS v3.5 - Setup & DuckDuckGo Edition")
clock = pygame.time.Clock()

WIN_SETUP_BG = (24, 34, 56)
MAC_BLUE = (52, 152, 219)
DARK_GRAY = (44, 62, 80)
LIGHT_GRAY = (235, 238, 242)
WHITE = (255, 255, 255)
RED_BUTTON = (231, 76, 60)
DDG_ORANGE = (222, 94, 49)
DDG_DARK = (48, 48, 48)
DDG_GREEN = (63, 138, 62)
BTN_BLUE = (0, 120, 215)

font = pygame.font.SysFont("Arial", 16)
bold_font = pygame.font.SysFont("Arial", 16, bold=True)
large_font = pygame.font.SysFont("Arial", 22, bold=True)

system_state = "setup"
key_input = ""
key_box_active = True
setup_error = ""
is_activated = False

browser_open = True
search_query = "Search privately..."
search_active = False
current_view = "home"
fire_flashing = 0

setup_box_rect = pygame.Rect(150, 110, 500, 380)
key_input_rect = pygame.Rect(190, 260, 420, 36)
activate_btn_rect = pygame.Rect(470, 420, 140, 36)
skip_btn_rect = pygame.Rect(190, 420, 210, 36)

browser_rect = pygame.Rect(100, 80, 600, 440)
desktop_icon_rect = pygame.Rect(30, 50, 80, 80)

results = [
    {"title": "Welcome to DuckDuckGo", "url": "https://duckduckgo.com", "snippet": "The internet privacy company that empowers you to control your data."},
    {"title": "ASUS Chromebook CX15 Specs", "url": "https://asus.com", "snippet": "Lightweight laptop running ChromeOS with efficiency processors."},
    {"title": "Pygame Project Hub", "url": "https://pygame.org", "snippet": "A free and open-source Python library for coding desktop operating system mocks!"}
]

VALID_KEYS = ["DAVIN-2026", "DUCK-OS", "1234-5678"]

while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if system_state == "setup":
            if event.type == pygame.MOUSEBUTTONDOWN:
                key_box_active = key_input_rect.collidepoint(mx, my)
                if activate_btn_rect.collidepoint(mx, my):
                    if key_input.strip().upper() in VALID_KEYS:
                        is_activated = True
                        system_state = "desktop"
                    else:
                        setup_error = "Invalid key! Try DAVIN-2026 or skip below."
                if skip_btn_rect.collidepoint(mx, my):
                    is_activated = False
                    system_state = "desktop"
            elif event.type == pygame.KEYDOWN and key_box_active:
                if event.key == pygame.K_RETURN:
                    if key_input.strip().upper() in VALID_KEYS:
                        is_activated = True
                        system_state = "desktop"
                    else:
                        setup_error = "Invalid key! Try DAVIN-2026 or skip below."
                elif event.key == pygame.K_BACKSPACE:
                    key_input = key_input[:-1]
                    setup_error = ""
                else:
                    if len(key_input) < 20:
                        key_input += event.unicode.upper()
                        setup_error = ""
        elif system_state == "desktop":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if desktop_icon_rect.collidepoint(mx, my):
                    browser_open = True
                if browser_open:
                    if 102 <= mx <= 114 and 80 <= my <= 92:
                        browser_open = False
                    elif 185 <= mx <= 575 and 114 <= my <= 138:
                        search_active = True
                        if search_query == "Search privately...":
                            search_query = ""
                    else:
                        search_active = False
                    if 585 <= mx <= 611 and 113 <= my <= 139:
                        fire_flashing = 12
                        search_query = "Search privately..."
                        current_view = "home"
            elif event.type == pygame.KEYDOWN and search_active:
                if event.key == pygame.K_RETURN:
                    search_active = False
                    if search_query.strip() != "":
                        current_view = "results"
                elif event.key == pygame.K_BACKSPACE:
                    search_query = search_query[:-1]
                else:
                    search_query += event.unicode

    if system_state == "setup":
        screen.fill(WIN_SETUP_BG)
        pygame.draw.rect(screen, WHITE, setup_box_rect, border_radius=8)
        pygame.draw.rect(screen, BTN_BLUE, (setup_box_rect.x, setup_box_rect.y, setup_box_rect.width, 40), border_top_left_radius=8, border_top_right_radius=8)
        screen.blit(bold_font.render("  DavinOS Setup", True, WHITE), (setup_box_rect.x + 12, setup_box_rect.y + 10))
        screen.blit(large_font.render("Activate DavinOS", True, DDG_DARK), (190, 175))
        screen.blit(font.render("Enter your product key to unlock full system personalization.", True, (90, 90, 90)), (190, 215))
        border_col = BTN_BLUE if key_box_active else (180, 180, 180)
        pygame.draw.rect(screen, (248, 249, 250), key_input_rect, border_radius=4)
        pygame.draw.rect(screen, border_col, key_input_rect, width=2, border_radius=4)
        display_key = key_input if key_input != "" else "XXXXX-XXXXX"
        key_col = (0, 0, 0) if key_input != "" else (160, 160, 160)
        screen.blit(bold_font.render(display_key, True, key_col), (key_input_rect.x + 12, key_input_rect.y + 8))
        if setup_error != "":
            screen.blit(font.render(setup_error, True, RED_BUTTON), (190, 310))
        pygame.draw.rect(screen, LIGHT_GRAY, skip_btn_rect, border_radius=4)
        screen.blit(font.render("I don't have a product key", True, DDG_DARK), (skip_btn_rect.x + 16, skip_btn_rect.y + 9))
        pygame.draw.rect(screen, BTN_BLUE, activate_btn_rect, border_radius=4)
        screen.blit(bold_font.render("Activate", True, WHITE), (activate_btn_rect.x + 40, activate_btn_rect.y + 9))
    elif system_state == "desktop":
        screen.fill(MAC_BLUE)
        pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, 26))
        pygame.draw.line(screen, (160, 160, 160), (0, 26), (SCREEN_WIDTH, 26))
        screen.blit(font.render("  DavinOS  File  Edit  View  Go  Privacy  Help", True, (0, 0, 0)), (5, 4))
        screen.blit(font.render("12:00 PM  ", True, (0, 0, 0)), (SCREEN_WIDTH - 75, 4))
        pygame.draw.rect(screen, (255, 255, 255, 100), desktop_icon_rect, border_radius=12)
        pygame.draw.rect(screen, WHITE, desktop_icon_rect, width=1, border_radius=12)
        screen.blit(font.render("DuckOS", True, WHITE), (desktop_icon_rect.x + 14, desktop_icon_rect.y + 30))
        if browser_open:
            pygame.draw.rect(screen, LIGHT_GRAY, browser_rect, border_radius=6)
            pygame.draw.rect(screen, WHITE, (browser_rect.x, browser_rect.y, browser_rect.width, 24), border_top_left_radius=6, border_top_right_radius=6)
            pygame.draw.line(screen, (200, 200, 200), (browser_rect.x, browser_rect.y + 24), (browser_rect.x + browser_rect.width, browser_rect.y + 24))
            pygame.draw.circle(screen, RED_BUTTON, (108, 86), 6)
            screen.blit(font.render("DuckDuckGo Privacy Browser", True, DDG_DARK), (browser_rect.x + 26, browser_rect.y + 4))
            pygame.draw.rect(screen, WHITE, (browser_rect.x, browser_rect.y + 25, browser_rect.width, 42))
            pygame.draw.line(screen, (210, 210, 210), (browser_rect.x, browser_rect.y + 67), (browser_rect.x + browser_rect.width, browser_rect.y + 67))
            screen.blit(font.render(" <   > ", True, (120, 120, 120)), (browser_rect.x + 12, browser_rect.y + 36))
            input_bg = (255, 255, 240) if search_active else (245, 246, 248)
            pygame.draw.rect(screen, input_bg, (185, 114, 390, 24), border_radius=12)
            pygame.draw.rect(screen, (200, 200, 200), (185, 114, 390, 24), width=1, border_radius=12)
            query_surface = font.render(search_query, True, (0, 0, 0) if search_query != "Search privately..." else (140, 140, 140))
            screen.blit(query_surface, (199, 117))
            btn_color = DDG_ORANGE if fire_flashing == 0 or fire_flashing % 4 < 2 else WHITE
            pygame.draw.circle(screen, btn_color, (598, 126), 13)
            screen.blit(bold_font.render("F", True, WHITE), (594, 117))
            fire_flashing = max(0, fire_flashing - 1)
            web_area = pygame.Rect(browser_rect.x + 10, browser_rect.y + 76, browser_rect.width - 20, browser_rect.height - 86)
            pygame.draw.rect(screen, WHITE, web_area, border_radius=4)
            if current_view == "home":
                logo_x = web_area.x + (web_area.width // 2)
                logo_y = web_area.y + 80
                pygame.draw.circle(screen, DDG_ORANGE, (logo_x, logo_y), 30)
                screen.blit(large_font.render("DDG", True, WHITE), (logo_x - 24, logo_y - 12))
                screen.blit(large_font.render("DuckDuckGo", True, DDG_DARK), (logo_x - 65, logo_y + 40))
                screen.blit(font.render("The internet privacy company that doesn't track you.", True, (100, 100, 100)), (logo_x - 165, logo_y + 75))
            elif current_view == "results":
                y_offset = web_area.y + 15
                screen.blit(bold_font.render(f"Privacy Search Results for: '{search_query}'", True, DDG_DARK), (web_area.x + 15, y_offset))
                y_offset += 30
                for res in results:
                    screen.blit(bold_font.render(res["title"], True, DDG_ORANGE), (web_area.x + 15, y_offset))
                    screen.blit(font.render(res["url"], True, DDG_GREEN), (web_area.x + 15, y_offset + 18))
                    screen.blit(font.render(res["snippet"], True, DARK_GRAY), (web_area.x + 15, y_offset + 34))
                    y_offset += 65
        if not is_activated:
            screen.blit(bold_font.render("Activate DavinOS", True, (235, 245, 255)), (SCREEN_WIDTH - 245, SCREEN_HEIGHT - 50))
            screen.blit(font.render("Go to Settings to activate DavinOS.", True, (235, 245, 255)), (SCREEN_WIDTH - 245, SCREEN_HEIGHT - 30))

    pygame.display.flip()
    clock.tick(60)
