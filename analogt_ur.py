import pygame
import datetime
import math

# Screen size
screen_width = 800
screen_height = 800

# Make sure the clock is in the window
if screen_width <= screen_height:
    frame_size = screen_width
if screen_width >= screen_height:
    frame_size = screen_height

radius = (frame_size / 2) * 0.875
start_position = (screen_width / 2, screen_height / 2) # Middle of the screen

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((screen_width, screen_height)) # Create a window
screen.fill((0, 255, 0)) # Fill the screen with green

pygame.draw.circle(screen, (255, 255, 255), start_position, radius) # Fill the inside of the clock with white
pygame.draw.circle(screen, (0, 0, 0), start_position, radius, width = 8) # Frame of the clock


# Create the hour pins
for angle in range(0, 360, 30):
    end_offset = [(radius - 7) * math.cos(math.radians(angle)), (radius - 7) * math.sin(math.radians(angle))] # Create an offset between the hour pins
    end_position = (start_position[0] + end_offset[0], start_position[1] + end_offset[1]) # Creat the end position of the hour pins
    start_offset = [(radius * 0.85) * math.cos(math.radians(angle)), (radius * 0.85) * math.sin(math.radians(angle))] # Create a new start to the hour pins
    hour_position = (start_position[0]+start_offset[0], start_position[1]+start_offset[1]) # Create the new position of the hour pins 
    pygame.draw.line(screen, (0,0,0), hour_position, end_position, 7) # Draw the hour pins

# Create the minute pins
for angle in range(0, 360, 6):
    end_offset = [(radius - 2) * math.cos(math.radians(angle)), (radius - 2) * math.sin(math.radians(angle))] # Create an offset between the minute pins
    end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1]) # Creat the end position of the minute pins
    start_offset = [(radius * 0.90) * math.cos(math.radians(angle)), (radius * 0.90) * math.sin(math.radians(angle))] # Create a new start to the minute pins 
    hour_position = (start_position[0]+start_offset[0], start_position[1]+start_offset[1]) # Create the new position of the minute pins 
    pygame.draw.line(screen, (0,0,0), hour_position, end_position, 2) # Draw the minute pins

# The dials
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Make sure the window stays open until the user closes it
            run_flag = False 
    pygame.display.flip() # Refresh the screen so drawing appears
    pygame.draw.circle(screen, (255, 255, 255), start_position, radius * 0.85) # Fill the inside of the clock with white each time it gets updated
    pygame.draw.circle(screen, (0, 0, 0), start_position, radius * 0.02) # MAke a small dot in the middle

    time = datetime.datetime.now() # Using real time

    # Create the hour pin
    angle_hour = math.radians(((time.hour % 12 + time.minute / 60) * 30 - 90)) # Calculates angel of the hour pin
    lenght_hour = radius * 0.55 # Lenght of the hour pin
    end_hour_x = start_position[0] + lenght_hour * math.cos(angle_hour)
    end_hour_y = start_position[1] + lenght_hour * math.sin(angle_hour)
    pygame.draw.line(screen, (0, 0, 0), start_position, (end_hour_x, end_hour_y), width=5) # Draws the hour pin

    # Create the minute pin
    angle_minute = math.radians((time.minute + time.second / 60) * 6 - 90) # Calculates angel of the minute pin
    lenght_minute = radius * 0.65 # Lenght of the minute pin
    end_minute_x = start_position[0] + lenght_minute * math.cos(angle_minute)
    end_minute_y = start_position[1] + lenght_minute * math.sin(angle_minute) 
    pygame.draw.line(screen, (0, 0, 0), start_position, (end_minute_x, end_minute_y), width=8) # Draws the minute pin

    # Create the second pin
    angle_second = math.radians((time.second) * 6 - 90) # Calculates angel of the second pin
    lenght_second = radius * 0.7 # Lenght of the second pin
    end_second_x = start_position[0] + lenght_second * math.cos(angle_second) 
    end_second_y = start_position[1] + lenght_second * math.sin(angle_second)
    pygame.draw.line(screen, (255, 0, 0), start_position, (end_second_x, end_second_y), width=2) # Draws the second pin

