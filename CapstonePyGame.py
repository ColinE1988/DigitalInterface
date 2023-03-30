#######
# ERRORS
#######

"""

"""

import pygame
import tkinter as tk
from tkinter import filedialog
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import random
import spidev

pygame.mixer.init()

GPIO.setwarnings(False)

# Initialize Pygame
pygame.init()

# Create a Tkinter root window (this is necessary for the file dialog to work)
root = tk.Tk()
root.withdraw()

# Set the size of the window and load the image
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))
grid_image = pygame.transform.scale(pygame.image.load("grid.png").convert_alpha(), (screen_width, screen_height))

# Set drawing size and color
drawing_color = (0, 0, 0)
drawing_size = 5

# Setting GPIO Pins
GPIO.setmode(GPIO.BCM)

#LEDs
white_led_pin = 18  # BCM pin 17
red_led_pin = 17  # BCM pin 18
green_led_pin = 19  # BCM pin 19
blue_led_pin = 20  # BCM pin 20

"""
GPIO.setup(white_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)
"""

# Initialize the RFID reader
reader = SimpleMFRC522()

# RFID Tags
TAG_ID = 584198792796

# User text variables
base_font = pygame.font.Font(None, 32)
user_text = ''


# Medium token variables
number_medium_tokens = 0
medium_token_images = []
medium_token_rects = []
medium_tokens_dragging = []
medium_token_names = []
medium_token_initiative = []

# Large token variables
number_large_tokens = 0
large_token_images = []
large_token_rects = []
large_tokens_dragging = []
large_token_names = []
large_token_initiative = []

# Huge token variables
number_huge_tokens = 0
huge_token_images = []
huge_token_rects = []
huge_tokens_dragging = []
huge_token_names = []
huge_token_initiative = []

# Objects page variables
trees_button_selected = False
rocks_button_selected = False
boxes_button_selected = False
barrels_button_selected = False

# Initiative page variables
start_button_selected = False
next_button_selected = False
previous_button_selected = False
end_button_selected = False
collect_initiative = True
initiative_running = False

# Lighting page variables
white_light_button_selected = False

# Set up the font and create a text object to display instructions
font = pygame.font.SysFont(None, 30)
text = font.render("Click the draw button to start drawing on the grid", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width // 2, 20))

# Set up the drawing surface and the draw button
drawing_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
draw_button_rect = pygame.Rect(10, 10, 50, 50)
draw_button_color = (0, 255, 0)
draw_button_selected = False

# Set up the Tokens button
tokens_button_rect = pygame.Rect(10, 70, 50, 50)
tokens_button_color = (255, 0, 0)
tokens_button_selected = False

# Set up the Objects button
objects_button_rect = pygame.Rect(10, 130, 50, 50)
objects_button_color = (255, 0, 0)
objects_button_selected = False

# Set up the Initiative button
initiative_button_rect = pygame.Rect(10, 200, 50, 50)
initiative_button_color = (255, 0, 0)
initiative_button_selected = False

# Set up the Media button
media_button_rect = pygame.Rect(10, 270, 50, 50)
media_button_color = (255, 0, 0)
media_button_selected = False

# Set up the Lighting button
lighting_button_rect = pygame.Rect(10, 350, 50, 50)
lighting_button_color = (255, 0, 0)
lighting_button_selected = False

# Set up the Save button
save_button_rect = pygame.Rect(10, 430, 50, 50)
save_button_color = (255, 0, 0)
save_button_selected = False

# Set up the Load button
load_button_rect = pygame.Rect(10, 510, 50, 50)
load_button_color = (255, 0, 0)
load_button_selected = False

# Set up the exit button
exit_button_rect = pygame.Rect(screen_width - 60, 10, 50, 50)
exit_button_color = (255, 0, 0)

#################################
# DRAW PAGE BUTTONS
#################################

# Set up the black button
black_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
black_button_color = (0, 0, 0)

# Set up the red button
red_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
red_button_color = (255, 0, 0)

# Set up the green button
green_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
green_button_color = (0, 255, 0)

# Set up the blue button
blue_button_rect = pygame.Rect(screen_width - 60, 250, 50, 50)
blue_button_color = (0, 0, 255)

# Set up the Five Pt button
FivePT_button_rect = pygame.Rect(screen_width - 60, 310, 50, 50)
FivePT_button_color = (0, 0, 255)

# Set up the Ten Pt button
TenPT_button_rect = pygame.Rect(screen_width - 60, 370, 50, 50)
TenPT_button_color = (0, 0, 255)

# Set up the Fifteen Pt button
FifteenPT_button_rect = pygame.Rect(screen_width - 60, 430, 50, 50)
FifteenPT_button_color = (0, 0, 255)

########################
# TOKEN PAGE BUTTONS
########################

# Set up Medium button
medium_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
medium_button_color = (0, 0, 255)

# Set up Large button
large_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
large_button_color = (0, 0, 255)

# Set up Huge button
huge_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
huge_button_color = (0, 0, 255)

########################
# OBJECTS PAGE BUTTONS
########################

# Set up Trees button
trees_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
trees_button_color = (0, 0, 255)

# Set up Rocks button
rocks_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
rocks_button_color = (0, 0, 255)

# Set up Boxes button
boxes_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
boxes_button_color = (0, 0, 255)

# Set up Barrels button
barrels_button_rect = pygame.Rect(screen_width - 60, 250, 50, 50)
barrels_button_color = (0, 0, 255)

########################
# INITIATIVE PAGE BUTTONS
########################

# Set up Start button
start_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
start_button_color = (0, 0, 255)

# Set up Next button
next_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
next_button_color = (0, 0, 255)

# Set up Previous button
previous_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
previous_button_color = (0, 0, 255)

# Set up End button
end_button_rect = pygame.Rect(screen_width - 60, 250, 50, 50)
end_button_color = (0, 0, 255)

########################
# MEDIA PAGE BUTTONS
########################

# Set up Load Media button
load_media_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
load_media_button_color = (0, 0, 255)

# Set up Play Media button
play_media_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
play_media_button_color = (0, 0, 255)

# Set up Pause Media button
pause_media_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
pause_media_button_color = (0, 0, 255)

########################
# LIGHTING PAGE BUTTONS
########################

# Set up the White Light button
white_light_button_rect = pygame.Rect(screen_width - 60, 70, 50, 50)
white_light_button_color = (0, 0, 0)

# Set up the Red Light button
red_light_button_rect = pygame.Rect(screen_width - 60, 130, 50, 50)
red_light_button_color = (255, 0, 0)

# Set up the Green Light button
green_light_button_rect = pygame.Rect(screen_width - 60, 190, 50, 50)
green_light_button_color = (0, 255, 0)

# Set up the Blue Light button
blue_light_button_rect = pygame.Rect(screen_width - 60, 250, 50, 50)
blue_light_button_color = (0, 0, 255)

##############
# FUNCTIONS
##############

# Get token names
def get_token_name():
    name = ""
    input_box_rect = pygame.Rect(0, 0, 200, 30)
    input_box_rect.center = screen.get_rect().center
    input_text = None
    input_text_width = input_box_rect.w
    font = pygame.font.Font(None, 24)
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # If the user presses Enter, return the name
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    # If the user presses Backspace, remove the last character from the name
                    name = name[:-1]
                else:
                    # Otherwise, add the character to the name
                    name += event.unicode
                # Render the input text to a surface and get its width
                input_text = font.render(name, True, pygame.Color("white"), pygame.Color("black"))
                input_text_width = input_text.get_width()
        
        # Draw the input box and text
        screen.fill(pygame.Color("black"), input_box_rect)
        if not name:
            prompt_text = font.render("Please enter the name of your token", True, pygame.Color("black"))
            prompt_text_rect = prompt_text.get_rect(center=(input_box_rect.centerx, input_box_rect.top - 20))
            screen.blit(prompt_text, prompt_text_rect)
        pygame.draw.rect(screen, pygame.Color("white"), input_box_rect, 2)
        if input_text:
            input_box_rect.w = max(200, input_text_width + 10)
            input_box_rect.center = screen.get_rect().center
            screen.blit(input_text, (input_box_rect.x + 5, input_box_rect.y + 5))
        pygame.display.flip()


# Get token initiative
def get_initiative_value(token_name):
    global collect_initiative
    collect_initiative = False
    value = ""
    input_box_rect = pygame.Rect(0, 0, 200, 30)
    input_box_rect.center = screen.get_rect().center
    input_text = None
    input_text_width = input_box_rect.w
    font = pygame.font.Font(None, 24)
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if value:
                        # If the user presses Enter and there is a value, return the initiative value
                        return int(value)
                elif event.key == pygame.K_BACKSPACE:
                    # If the user presses Backspace, remove the last character from the value
                    value = value[:-1]
                elif event.unicode.isnumeric():
                    # If the character is a number, add it to the value
                    value += event.unicode
                # Render the input text to a surface and get its width
                input_text = font.render(value, True, pygame.Color("white"), pygame.Color("black"))
                input_text_width = input_text.get_width()

        # Fill the entire screen with black
        screen.fill((0, 0, 0))
        
        # Draw the input box and text
        prompt_text = font.render(f"Please enter the initiative for {token_name}", True, pygame.Color("white"))
        prompt_text_rect = prompt_text.get_rect(center=(input_box_rect.centerx, input_box_rect.top - 20))
        screen.blit(prompt_text, prompt_text_rect)
        pygame.draw.rect(screen, pygame.Color("white"), input_box_rect, 2)
        if input_text:
            input_box_rect.w = max(200, input_text_width + 10)
            input_box_rect.center = screen.get_rect().center
            screen.blit(input_text, (input_box_rect.x + 5, input_box_rect.y + 5))
        pygame.display.flip()


# Display initiatives
def display_initiatives(initiatives):
    # Sort the initiatives from highest to lowest, along with their token names
    initiatives_sorted = sorted(initiatives.items(), key=lambda x: x[1], reverse=True)
    
    # Display the sorted initiatives on the screen
    font = pygame.font.Font(None, 24)
    x, y = screen.get_width() // 2, screen.get_height() // 2  # Set the initial position to the center of the screen
    padding = 10  # additional space between initiatives
    for i, (token_name, initiative) in enumerate(initiatives_sorted):
        text = font.render(f"{i+1}. {token_name}: {initiative}", True, pygame.Color("black"))
        text_width, text_height = text.get_size()
        screen.blit(text, (x - text_width // 2, y - (i+1)*(text_height + padding) - text_height // 2))
    
# Function to display the roll result on the screen
def display_roll_result(roll):
    screen.fill((0, 0, 0))  # Clear the screen

    font = pygame.font.Font(None, 36)
    text = font.render(f"You rolled a {roll}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.blit(text, text_rect)
    pygame.display.flip()


##############
# START LOOP
##############

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            

        # Draw on the drawing surface when the left mouse button is pressed and dragged and draw button is selected
        if event.type == pygame.MOUSEMOTION and event.buttons[0] and draw_button_selected:
            if grid_image.get_rect().collidepoint(event.pos):
                pygame.draw.circle(drawing_surface, drawing_color, event.pos, drawing_size)
                
        # Check if the Save button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if save_button_rect.collidepoint(event.pos):
                file_name = "saved_map.png"
                pygame.image.save(drawing_surface, file_name)

        # Check if the Load button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if load_button_rect.collidepoint(event.pos):
                file_name = "saved_map.png"
                loaded_image = pygame.image.load(file_name)
                drawing_surface.blit(loaded_image, (0, 0))

        # Check if the draw button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if draw_button_rect.collidepoint(event.pos):
                draw_button_selected = not draw_button_selected
                
        # Check if the tokens button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if tokens_button_rect.collidepoint(event.pos):
                tokens_button_selected = not tokens_button_selected
                
        # Check if the objects button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if objects_button_rect.collidepoint(event.pos):
                objects_button_selected = not objects_button_selected
           
        # Check if the initiative button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if initiative_button_rect.collidepoint(event.pos):
                initiative_button_selected = not initiative_button_selected
                 
                
           
        # Check if the media button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if media_button_rect.collidepoint(event.pos):
                media_button_selected = not media_button_selected
                
        # Check if the lighting button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if lighting_button_rect.collidepoint(event.pos):
                lighting_button_selected = not lighting_button_selected 
           
        # Check if the exit button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                quit()
    
########################
# CHECKING FOR DIE ROLLS
########################

    # Check for RFID tag
    id, _ = reader.read_no_block()
    if id == TAG_ID:
        roll = random.randint(1, 20)
        display_roll_result(roll)
        pygame.time.delay(2000)  # Display the result for 2 seconds

########################
# CHECKING FOR MOVING TOKENS
########################

    # MEDIUM
       
    for i in range(number_medium_tokens):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if medium_token_rects[i].collidepoint(event.pos):
                medium_tokens_dragging[i] = True
                offset = (event.pos[0] - medium_token_rects[i].x, event.pos[1] - medium_token_rects[i].y)
    
    for i in range(number_medium_tokens):
        if medium_tokens_dragging[i]:
            medium_token_rects[i].x = pygame.mouse.get_pos()[0] - offset[0]
            medium_token_rects[i].y = pygame.mouse.get_pos()[1] - offset[1]
            
    for i in range(number_medium_tokens):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            medium_tokens_dragging[i] = False
            
    # LARGE
    
    for i in range(number_large_tokens):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if large_token_rects[i].collidepoint(event.pos):
                large_tokens_dragging[i] = True
                offset = (event.pos[0] - large_token_rects[i].x, event.pos[1] - large_token_rects[i].y)
    
    for i in range(number_large_tokens):
        if large_tokens_dragging[i]:
            large_token_rects[i].x = pygame.mouse.get_pos()[0] - offset[0]
            large_token_rects[i].y = pygame.mouse.get_pos()[1] - offset[1]
            
    for i in range(number_large_tokens):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            large_tokens_dragging[i] = False
            
    # HUGE
    
    for i in range(number_huge_tokens):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if huge_token_rects[i].collidepoint(event.pos):
                huge_tokens_dragging[i] = True
                offset = (event.pos[0] - huge_token_rects[i].x, event.pos[1] - huge_token_rects[i].y)
    
    for i in range(number_huge_tokens):
        if huge_tokens_dragging[i]:
            huge_token_rects[i].x = pygame.mouse.get_pos()[0] - offset[0]
            huge_token_rects[i].y = pygame.mouse.get_pos()[1] - offset[1]
            
    for i in range(number_huge_tokens):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            huge_tokens_dragging[i] = False
     
    
    # Draw the grid image and the drawing surface onto the screen
    screen.blit(grid_image, (0, 0))
    screen.blit(drawing_surface, (0, 0))
    
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (100, 100))
    
    # Draw all medium tokens
    for i in range(number_medium_tokens):
        screen.blit(medium_token_images[i], medium_token_rects[i]) 
    
    #Draw all large tokens
    for i in range(number_large_tokens):
        screen.blit(large_token_images[i], large_token_rects[i])
        
    #Draw all huge tokens
    for i in range(number_huge_tokens):
        screen.blit(huge_token_images[i], huge_token_rects[i]) 
        

    ################
    # DRAW MAIN PAGE BUTTONS
    ################
    
    # Draw the draw button
    pygame.draw.rect(screen, draw_button_color if draw_button_selected else (0, 0, 0), draw_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Draw", True, (0, 0, 0))
    text_rect = text.get_rect(center=draw_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the tokens button
    pygame.draw.rect(screen, tokens_button_color if tokens_button_selected else (0, 0, 0), tokens_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Tokens", True, (0, 0, 0))
    text_rect = text.get_rect(center=tokens_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the objects button
    pygame.draw.rect(screen, objects_button_color if objects_button_selected else (0, 0, 0), objects_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Objects", True, (0, 0, 0))
    text_rect = text.get_rect(center=objects_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the initiative button
    pygame.draw.rect(screen, initiative_button_color if initiative_button_selected else (0, 0, 0), initiative_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Initiative", True, (0, 0, 0))
    text_rect = text.get_rect(center=initiative_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the media button
    pygame.draw.rect(screen, media_button_color if media_button_selected else (0, 0, 0), media_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Media", True, (0, 0, 0))
    text_rect = text.get_rect(center=media_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the lighting button
    pygame.draw.rect(screen, lighting_button_color if lighting_button_selected else (0, 0, 0), lighting_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Lighting", True, (0, 0, 0))
    text_rect = text.get_rect(center=lighting_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the Save button
    pygame.draw.rect(screen, save_button_color if save_button_selected else (0, 0, 0), save_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Save", True, (0, 0, 0))
    text_rect = text.get_rect(center=save_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the Load button
    pygame.draw.rect(screen, load_button_color if load_button_selected else (0, 0, 0), load_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Load", True, (0, 0, 0))
    text_rect = text.get_rect(center=load_button_rect.center)
    screen.blit(text, text_rect)
    
    # Draw the exit button
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    font = pygame.font.SysFont(None, 30)
    text = font.render("X", True, (255, 255, 255))
    text_rect = text.get_rect(center=exit_button_rect.center)
    screen.blit(text, text_rect)
    
    ###############
    # DRAW PAGE BUTTONS
    ###############
    
    if draw_button_selected == True:
        
        # Draw the black button
        pygame.draw.rect(screen, black_button_color, black_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=black_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the red button
        pygame.draw.rect(screen, red_button_color, red_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=red_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the green button
        pygame.draw.rect(screen, green_button_color, green_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=green_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the blue button
        pygame.draw.rect(screen, blue_button_color, blue_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=blue_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the Five Pt button
        pygame.draw.rect(screen, FivePT_button_color, FivePT_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("5Pt", True, (255, 255, 255))
        text_rect = text.get_rect(center=FivePT_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Ten Pt button
        pygame.draw.rect(screen, TenPT_button_color, TenPT_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("10Pt", True, (255, 255, 255))
        text_rect = text.get_rect(center=TenPT_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Fifteen Pt button
        pygame.draw.rect(screen, FifteenPT_button_color, FifteenPT_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("15Pt", True, (255, 255, 255))
        text_rect = text.get_rect(center=FifteenPT_button_rect.center)
        screen.blit(text, text_rect)
        
        # Check if the black button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if black_button_rect.collidepoint(event.pos):
                drawing_color = (0, 0, 0)
                
        # Check if the red button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if red_button_rect.collidepoint(event.pos):
                drawing_color = (255, 0, 0)
                
        # Check if the green button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if green_button_rect.collidepoint(event.pos):
                drawing_color = (0, 255, 0)
                
        # Check if the blue button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if blue_button_rect.collidepoint(event.pos):
                drawing_color = (0, 0, 255)
                
        # Check if the Five Pt button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if FivePT_button_rect.collidepoint(event.pos):
                drawing_size = 5
                
        # Check if the Ten Pt button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if TenPT_button_rect.collidepoint(event.pos):
                drawing_size = 10
                
        # Check if the Fifteen Pt button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if FifteenPT_button_rect.collidepoint(event.pos):
                drawing_size = 15
    
    ####################
    # TOKEN PAGE BUTTONS
    ####################
    
    
    if tokens_button_selected == True:
        
        # Draw the Medium button
        pygame.draw.rect(screen, medium_button_color, medium_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Medium", True, (255, 255, 255))
        text_rect = text.get_rect(center=medium_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Large button
        pygame.draw.rect(screen, large_button_color, large_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Large", True, (255, 255, 255))
        text_rect = text.get_rect(center=large_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Huge button
        pygame.draw.rect(screen, huge_button_color, huge_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Huge", True, (255, 255, 255))
        text_rect = text.get_rect(center=huge_button_rect.center)
        screen.blit(text, text_rect)
        
        # Check if the Medium button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if medium_button_rect.collidepoint(event.pos):
                
                # Prompt the user for a name for the token
                token_name = get_token_name()
                
                # Show a file dialog and let the user select an image file
                file_path = filedialog.askopenfilename()
                
                # Load the object image and create a Rect object for it
                medium_token_image = pygame.image.load(file_path).convert_alpha()
                medium_token_image = pygame.transform.scale(medium_token_image, (50, 50))
                medium_token_images.append(medium_token_image)
                medium_token_rect = medium_token_image.get_rect()
                medium_token_rect.center = (screen_width // 2, screen_height // 2)
                medium_token_rects.append(medium_token_rect)
                medium_tokens_dragging.append(False)
                medium_token_names.append(token_name)
                number_medium_tokens += 1             
                
        # Check if the Large button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if large_button_rect.collidepoint(event.pos):
                
                # Prompt the user for a name for the token
                token_name = get_token_name()
                
                # Show a file dialog and let the user select an image file
                file_path = filedialog.askopenfilename()

                # Load the object image and create a Rect object for it
                large_token_image = pygame.image.load(file_path).convert_alpha()
                large_token_image = pygame.transform.scale(large_token_image, (150, 150))
                large_token_images.append(large_token_image)
                large_token_rect = large_token_image.get_rect()
                large_token_rect.center = (screen_width // 2, screen_height // 2)
                large_token_rects.append(large_token_rect)
                large_tokens_dragging.append(False)
                large_token_names.append(token_name)
                number_large_tokens += 1
                
        # Check if the Huge button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if huge_button_rect.collidepoint(event.pos):
                
                # Prompt the user for a name for the token
                token_name = get_token_name()
                
                # Show a file dialog and let the user select an image file
                file_path = filedialog.askopenfilename()

                # Load the object image and create a Rect object for it
                huge_token_image = pygame.image.load(file_path).convert_alpha()
                huge_token_image = pygame.transform.scale(huge_token_image, (250, 250))
                huge_token_images.append(huge_token_image)
                huge_token_rect = huge_token_image.get_rect()
                huge_token_rect.center = (screen_width // 2, screen_height // 2)
                huge_token_rects.append(huge_token_rect)
                huge_tokens_dragging.append(False)
                huge_token_names.append(token_name)
                number_huge_tokens += 1
                
    ################
    # OBJECTS PAGE BUTTONS
    ################
    
    if objects_button_selected == True:
        
                
        # If buttons are clicked
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if trees_button_rect.collidepoint(event.pos):
                trees_button_selected = not trees_button_selected
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rocks_button_rect.collidepoint(event.pos):
                rocks_button_selected = not rocks_button_selected
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if boxes_button_rect.collidepoint(event.pos):
                boxes_button_selected = not boxes_button_selected
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if barrels_button_rect.collidepoint(event.pos):
                barrels_button_selected = not barrels_button_selected
        
        # Draw the Trees button
        pygame.draw.rect(screen, trees_button_color if trees_button_selected else (0, 0, 0), trees_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Trees", True, (255, 255, 255))
        text_rect = text.get_rect(center=trees_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Rocks button
        pygame.draw.rect(screen, rocks_button_color if rocks_button_selected else (0, 0, 0), rocks_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Rocks", True, (255, 255, 255))
        text_rect = text.get_rect(center=rocks_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Boxes button
        pygame.draw.rect(screen, boxes_button_color if boxes_button_selected else (0, 0, 0), boxes_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Boxes", True, (255, 255, 255))
        text_rect = text.get_rect(center=boxes_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Barrels button
        pygame.draw.rect(screen, barrels_button_color if barrels_button_selected else (0, 0, 0), barrels_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Barrels", True, (255, 255, 255))
        text_rect = text.get_rect(center=barrels_button_rect.center)
        screen.blit(text, text_rect)
        
    #################
    # INITIATIVE PAGE BUTTONS
    #################
    
    if initiative_running:
        print("Displaying initiatives")
        display_initiatives(initiatives)
        
    
    
    
    if initiative_button_selected == True:
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button_rect.collidepoint(event.pos):
                #collect_initiative = True
                start_button_selected = not start_button_selected
                initiatives = {}
                if collect_initiative:
                    for i in range(len(medium_token_names)):
                        medium_token_name = medium_token_names[i]
                        m_token_initiative = get_initiative_value(medium_token_name)
                        initiatives[medium_token_name] = m_token_initiative
                    for i in range(len(large_token_names)):
                        large_token_name = large_token_names[i]
                        l_token_initiative = get_initiative_value(large_token_name)
                        initiatives[large_token_name] = l_token_initiative
                    for i in range(len(huge_token_names)):
                        huge_token_name = huge_token_names[i]
                        h_token_initiative = get_initiative_value(huge_token_name)
                        initiatives[huge_token_name] = h_token_initiative
                    initiative_running = True
                        
                            
                
        # Draw the Start button
        pygame.draw.rect(screen, start_button_color if start_button_selected else (0, 0, 0), start_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=start_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Next button
        pygame.draw.rect(screen, next_button_color if next_button_selected else (0, 0, 0), next_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Next", True, (255, 255, 255))
        text_rect = text.get_rect(center=next_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Previous button
        pygame.draw.rect(screen, previous_button_color if previous_button_selected else (0, 0, 0), previous_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Previous", True, (255, 255, 255))
        text_rect = text.get_rect(center=previous_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the End button
        pygame.draw.rect(screen, end_button_color if end_button_selected else (0, 0, 0), end_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("End", True, (255, 255, 255))
        text_rect = text.get_rect(center=end_button_rect.center)
        screen.blit(text, text_rect)
        
        
    #################
    # MEDIA PAGE BUTTONS
    #################
    
    if media_button_selected == True:
        
        # Draw the Load Media button
        pygame.draw.rect(screen, load_media_button_color, load_media_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Load", True, (255, 255, 255))
        text_rect = text.get_rect(center=load_media_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Play Media button
        pygame.draw.rect(screen, play_media_button_color, play_media_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Play", True, (255, 255, 255))
        text_rect = text.get_rect(center=play_media_button_rect.center)
        screen.blit(text, text_rect)
        
        # Draw the Pause Media button
        pygame.draw.rect(screen, pause_media_button_color, pause_media_button_rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Pause", True, (255, 255, 255))
        text_rect = text.get_rect(center=pause_media_button_rect.center)
        screen.blit(text, text_rect)
        
        # Check if the Load Media button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if load_media_button_rect.collidepoint(event.pos):
                
                # Show a file dialog and let the user select a media file
                media_file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])

                # Load the media file and play it
                pygame.mixer.music.load(media_file_path)
                pygame.mixer.music.play()
                
        # Check if the Play Media button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_media_button_rect.collidepoint(event.pos):

                # Play Media
                pygame.mixer.music.unpause()
                
        # Check if the Pause Media button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause_media_button_rect.collidepoint(event.pos):

                # Play Media
                pygame.mixer.music.pause()
    
    #################
    # LIGHTING PAGE BUTTONS
    #################
    
    if lighting_button_selected == True:
        
        # Draw the White Light button
        pygame.draw.rect(screen, white_light_button_color, white_light_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=black_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the Red Light button
        pygame.draw.rect(screen, red_light_button_color, red_light_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=red_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the Green Light button
        pygame.draw.rect(screen, green_light_button_color, green_light_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=green_button_rect.center)
        #screen.blit(text, text_rect)
        
        # Draw the Blue Light button
        pygame.draw.rect(screen, blue_light_button_color, blue_light_button_rect)
        font = pygame.font.SysFont(None, 30)
        #text = font.render(" ", True, (255, 255, 255))
        #text_rect = text.get_rect(center=blue_button_rect.center)
        #screen.blit(text, text_rect)
        
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if white_light_button_rect.collidepoint(event.pos):
                white_light_button_selected = not white_light_button_selected
                # Turn on the white LEDs
                GPIO.output(white_led_pin, 1)
        """
        
    # Display the instructions
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()