# Self Driving Car

import numpy as np
import math
from random import random, randint
import matplotlib.pyplot as plt
import time
import pygame
import tkinter as tk
from tkinter import messagebox

from ai import Dqn

brain = Dqn(5, 3, 0.9)

class carMove(object):

    def __init__(self):
        self.velocity = 8
        self.deltaTime = 1
        self.distance = self.deltaTime * self.velocity
        self.angleDeltaChoice = [0, -20, 20]
        self.angleDelta = 0
        self.angleHoriz = 0
        self.cord_x = 640
        self.cord_y = 360
        self.old_cord_x = 640
        self.old_cord_y = 360
        self.bigBrain101_choice = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Checks for the clicking of the close button.
                raise SystemExit   # This handles the closing of window.

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] == 1:
                    self.angleDelta = self.angleDeltaChoice[0]

                elif keys[pygame.K_RIGHT]:
                    self.angleDelta = self.angleDeltaChoice[2]

                elif keys[pygame.K_LEFT]:
                    self.angleDelta = self.angleDeltaChoice[1]

                else:
                    self.angleDelta = self.angleDeltaChoice[0]

        # Makes sure angle is within the range -180 to 180
        self.angleHoriz += self.angleDelta
        if self.angleHoriz >= 180:  # Ensure angle stays within the range of less than 180.
            self.angleHoriz = -180
        elif self.angleHoriz <= -180:   # Ensure angle stays within the range of more than -180.
            self.angleHoriz = 180

        self.displacement_x = int(self.distance * math.cos(math.radians(self.angleHoriz)))
        self.displacement_y = int(self.distance * math.sin(math.radians(self.angleHoriz)))

        # Prevent the car from going out of screen
        if self.cord_x <= 10:
            self.cord_x = 11
        elif self.cord_x >= 1270:
            self.cord_x = 1269
        elif self.cord_y <= 10:
            self.cord_y = 11
        elif self.cord_y >= 710:
            self.cord_y = 709

        # Proceed as normal if the car is not going out of screen
        else:
            self.cord_x += self.displacement_x
            self.cord_y += self.displacement_y

        # print(f"self.displacement_x: {self.displacement_x}")  # For troubleshooting
        # print(f"self.displacement_y: {self.displacement_y}")  # For troubleshooting
        # print(f"self.angleHoriz: {self.angleHoriz}")  # For troubleshooting
        # print(f"self.cord_x: {self.cord_x}")  # For troubleshooting
        # print(f"self.cord_y: {self.cord_y}")  # For troubleshooting

    def move_2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Checks for the clicking of the close button.
                raise SystemExit   # This handles the closing of window.

        self.angleDelta  = self.angleDeltaChoice[self.bigBrain101_choice]

        # Makes sure angle is within the range -180 to 180
        self.angleHoriz += self.angleDelta
        if self.angleHoriz >= 180:  # Ensure angle stays within the range of less than 180.
            self.angleHoriz = -180
        elif self.angleHoriz <= -180:   # Ensure angle stays within the range of more than -180.
            self.angleHoriz = 180

        self.displacement_x = int(self.distance * math.cos(math.radians(self.angleHoriz)))
        self.displacement_y = int(self.distance * math.sin(math.radians(self.angleHoriz)))

        # Prevent the car from going out of screen
        if self.cord_x <= 10:
            self.cord_x = 11
        elif self.cord_x >= 1270:
            self.cord_x = 1269
        elif self.cord_y <= 10:
            self.cord_y = 11
        elif self.cord_y >= 710:
            self.cord_y = 709

        # Proceed as normal if the car is not going out of screen
        else:
            self.cord_x += self.displacement_x
            self.cord_y += self.displacement_y

    def history(self):
        self.old_cord_x = self.cord_x
        self.old_cord_y = self.cord_y


class sensor(object):

    def __init__(self, x, y, refangle):
        self.cockx = x
        self.cocky = y
        self.ref_Angle = refangle

    # Draw the sensor with respect to the car
    def draw_3_sensor(self, surface):
        self.x_sen_1 = (int((self.cockx) + (16 * (math.cos(math.radians((self.ref_Angle - 45)))))), int((self.cocky) + (16 * (math.sin(math.radians((self.ref_Angle - 45)))))))
        self.actual_1x = self.x_sen_1[0]
        self.actual_1y = self.x_sen_1[1]
        self.sig_1 = (np.sum(sand[self.actual_1x - 10: self.actual_1x + 10, self.actual_1y - 10: self.actual_1y + 10]) / 400)
        if self.actual_1x >= 1270 or self.actual_1x <= 10 or self.actual_1y <= 10 or self.actual_1y >= 710:
            self.sig_1 = 1
        self.signal_1 = int(self.sig_1 * 255)
        self.sensor_1 = pygame.draw.circle(surface, (255 - self.signal_1, 0, 255), self.x_sen_1, 6)   # Draw sensor to the left of the car. And using the signal obtained, we will change the color according to the signal value.
        # print(f"signal_1: {self.signal_1}") # Check that the signal is within range and that the sensor is scanning at the correct location.

        self.x_sen_2 = (int((self.cockx) + (16 * (math.cos(math.radians((self.ref_Angle)))))), int((self.cocky) + (16 * (math.sin(math.radians((self.ref_Angle)))))))
        self.actual_2x = self.x_sen_2[0]
        self.actual_2y = self.x_sen_2[1]
        self.sig_2 = (np.sum(sand[self.actual_2x - 10: self.actual_2x + 10, self.actual_2y - 10: self.actual_2y + 10]) / 400)
        if self.actual_2x >= 1270 or self.actual_2x <= 10 or self.actual_2y <= 10 or self.actual_2y >= 710:
            self.sig_2 = 1
        self.signal_2 = int(self.sig_2 * 255)
        self.sensor_2 = pygame.draw.circle(surface, (0, 255, 255 - self.signal_2), self.x_sen_2, 6)   # Draw sensor directly in front of the car. And using the signal obtained, we will change the color according to the signal value.
        # print(f"signal_2: {self.signal_2}")  # Check that the signal is within range and that the sensor is scanning at the correct location.

        self.x_sen_3 = (int((self.cockx) + (16 * (math.cos(math.radians((self.ref_Angle + 45)))))), int((self.cocky) + (16 * (math.sin(math.radians((self.ref_Angle + 45)))))))
        self.actual_3x = self.x_sen_3[0]
        self.actual_3y = self.x_sen_3[1]
        self.sig_3 = (np.sum(sand[self.actual_3x - 10: self.actual_3x + 10, self.actual_3y - 10: self.actual_3y + 10]) / 400)
        if self.actual_3x >= 1270 or self.actual_3x <= 10 or self.actual_3y <= 10 or self.actual_3y >= 710:
            self.sig_3 = 1
        self.signal_3 = int(self.sig_3 * 255)
        self.sensor_3 = pygame.draw.circle(surface, (255, 255 - self.signal_3, 0), self.x_sen_3, 6)   # Draw sensor to the right of the car. And using the signal obtained, we will change the color according to the signal value.
        # print(f"signal_3: {self.signal_3}")  # Check that the signal is within range and that the sensor is scanning at the correct location.

# For the drawing of sand
def draw_cursor(screen):
    global Nigga_coordinates, list_click_clear_canvas, list_click_save, list_click_load, override   # Nigga_coordinates is where all the road coordinates will be stored in.
    pos = pygame.mouse.get_pos()
    mouse_down = pygame.mouse.get_pressed()[0]
    x = pos[0]
    y = pos[1]
    cursorclickXY = [x + 12, y - 48]
    if mouse_down:
        screen.blit(Cursor_Clicked, (x, y - 48))
        for i1 in range(1, 10):
            for i2 in range(1, 10):
                Nigga_coordinates.add((x + 12 + i1, y - 48 + i2))

        for ii in list_click_override:
            if cursorclickXY == ii:
                override = not(override)

        for iii in list_click_clear_canvas:
            # print(cursorclickXY) # For Checking
            # print(iii)  # For Checking
            if cursorclickXY == iii:
                clear_canvas()
                break

        for iiii in list_click_save:
            # print(cursorclickXY)    # For Checking
            # print(iiii) # For Checking
            if cursorclickXY == iiii:
                save()
                break

        for iiiii in list_click_load:
            # print(cursorclickXY)    # For Checking
            # print(iiiii)    # For Checking
            if cursorclickXY == iiiii:
                load()
                break
    else:
        screen.blit(Cursor, (x, y - 48))

def reward(xxx, yyy):
    global last_reward, sand, distance, car_1, font, win

    if sand[xxx, yyy] > 0:  # Hitting the sand will be prioritized with most penalty
        car_1.distance = 2
        last_reward = -1
    else:
        car_1.distance = 8
        if distance < last_distance:  # This will check if car is getting closer to the goal.
            last_reward = 0.1
        else:   # This is when you get further away from the goal or living penalty.
            last_reward = -0.2

    if xxx <= 15 or xxx >= 1265:    # Hitting against the edge of the screen will be prioritized with most penalty
        last_reward = -1
    elif yyy <= 15 or yyy >= 705:   # Hitting against the edge of the screen will be prioritized with most penalty
        last_reward = -1

    Last_Reward_1 = font.render("Last Reward : " + str(last_reward), True, (0, 255, 0))
    win.blit(Last_Reward_1, (10, 5))

    # if distance < 100:
        # last_reward = 1

    # print(last_reward)  # For testing, please check for the following, reward of 0.1 when going closer to reward, -0.2 for getting further, 1 for reaching goal, -1 for hitting sand or edge of screen.

def goal(corddx, corddy):
    global goal_x, goal_y, distance
    distance = np.sqrt((corddx - goal_x) ** 2 + (corddy - goal_y) ** 2)
    if distance < 100:
        if goal_x == 30:
            goal_x = goal_list[2]
            goal_y = goal_list[3]
            # print("YAY YOU REACH YOUR GOAL!") # To check if it works
        else:
            goal_x = goal_list[0]
            goal_y = goal_list[1]
            # print("YAY YOU REACH YOUR GOAL!") # To check if it works

def draw_4_Buttons(screen):
    clearCanvas = pygame.draw.rect(screen, (0, 0, 255), (1180, 0, 100, 50))
    saVe = pygame.draw.rect(screen, (0, 255, 0), (1070, 0, 100, 50))
    loAd = pygame.draw.rect(screen, (255, 0, 0), (960, 0, 100, 50))
    overRide = pygame.draw.rect(screen, (0, 150, 174), (850, 0, 100, 50))

def clear_canvas(): # clear button
    global sand, Nigga_coordinates
    print("Making Screen_Nigga...")
    Nigga_coordinates.clear()
    sand = np.zeros((width, height))

def save(): # save button
    print("Saving BenjaBrain...")
    brain.save()
    plt.plot(scores)
    plt.show()

def load():  # load button
    print("Loading Last Saved BenjaBrain...")
    brain.load()

def muda_function(xc1, list_of_crap):
    for ii in range(0, 51):
        for ii1 in range(xc1, xc1 + 101):
            list_of_crap.append([ii1, ii])

def main():
    global Nigga_coordinates, Cursor, Cursor_Clicked, goal_x, goal_y, distance, last_distance, goal_list, Finishing_Flag, last_reward, sand, car_1, list_click_override, list_click_clear_canvas, list_click_save, list_click_load, width, height, override, scores, font, win
    pygame.init()   # Initialize all imported pygame modules, if not your font cannot be initialized.
    width = 1280  # Width for screen
    height = 720  # Height for screen
    override = True
    last_reward = 0
    goal_list = [30, 30, 1250, 690]
    sand = np.zeros((width, height))  # numpy.zeros(shape, dtype=float, order='C')
    goal_x = 30
    goal_y = 30
    Cursor = pygame.image.load('Middle_Finger.png')
    Cursor_Clicked = pygame.image.load('Cursor_Clicked.png')
    Finishing_Flag = pygame.image.load('Finishing_Flag.png')
    win = pygame.display.set_mode((width, height))  # Set the screen.
    pygame.display.set_caption("WannaCry?")
    clock = pygame.time.Clock()
    car_1 = carMove()
    Nigga_coordinates = {(-10, -10)}    # Have to initialize the set with a set first...
    Nigga_coordinates.clear()   # Then clear that set to removed the initialized set...
    last_distance = 0
    scores = []  # Initializing the mean score curve... (Sliding window of the rewards) with respect to time
    list_click_override = []
    list_click_clear_canvas = []
    list_click_save = []
    list_click_load = []
    muda_function(850, list_click_override)
    muda_function(960, list_click_clear_canvas)
    muda_function(1070, list_click_save)
    muda_function(1180, list_click_load)
    font = pygame.font.Font('freesansbold.ttf', 16, )    # create a new Font object from a file
    ovveride_text = font.render("Override", True, (255, 255, 255))
    clear_text = font.render("Clear", True, (255, 255, 255))
    save_text = font.render("Save", True, (255, 255, 255))
    load_text = font.render("Load", True, (255, 255, 255))
    # print(list_click_clear_canvas)
    # print(list_click_save)
    # print(list_click_load)

    while True:
        pygame.time.delay(50)  # Delay in millisecond
        clock.tick(1000)
        win.fill((0, 0, 0)) # This is the background and is NIGGA!
        if override == True:
            car_1.move_2()
        else:
            car_1.move()
        goal(car_1.cord_x, car_1.cord_y)  # call the function goal(), and this have to be called before we can even call the sensor() class as we have to define distance variable which is defined in this goal() function and this sensor() class has dependency on distance variable, if we were to put this line of code after the sensor class() you will get an error of distance not defined...
        # win.blit(carImg2, (0 - 16, 0 - 8)) # For testing...
        pygame.draw.circle(win, (0, 0, 255), (car_1.old_cord_x, car_1.old_cord_y), 4)
        pygame.draw.circle(win, (0, 0, 255), (car_1.cord_x, car_1.cord_y), 4)   # This is the reference point, and we shall use this as the car!
        draw_4_Buttons(win) # This function must be executed before the drawing of the cursor to prevent it from being on top of the cursor.
        win.blit(ovveride_text, (860, 10))
        win.blit(clear_text, (970, 10))
        win.blit(save_text, (1080, 10))
        win.blit(load_text, (1190, 10))
        pygame.mouse.set_visible(0)
        draw_cursor(win)    # Draw the cursor
        win.blit(Finishing_Flag, (goal_x, goal_y))  # Draw the Finishing_Flag
        for x, y in Nigga_coordinates:
            pygame.draw.circle(win, (255, 255, 255), (x , y), 1)
        for xx, yy in Nigga_coordinates:
            sand[xx, yy] = 1
            # print(sand) # For testing. Not recommended...
        # print(Nigga_coordinates) # Check and make sure that it is indeed being cleared when the clear button is depressed.
        reward(car_1.cord_x, car_1.cord_y)
        sensor_new = sensor(car_1.cord_x, car_1.cord_y, car_1.angleHoriz)
        sensor_new.draw_3_sensor(win)

        a = np.sqrt(((car_1.cord_x - goal_x) ** 2) + ((car_1.cord_y - goal_y) ** 2))
        b = np.sqrt(((car_1.cord_x - car_1.old_cord_x) ** 2) + ((car_1.cord_y - car_1.old_cord_y) ** 2))
        c = np.sqrt(((goal_x - car_1.old_cord_x) ** 2) + ((goal_y - car_1.old_cord_y) ** 2))

        orientation = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * b * c))

        fuck_you_math_1 = int(math.degrees(orientation)) # For testing...
        # print(fuck_you_math_1) # For testing if the Math works or not...

        orientation_print = font.render("Orientation : " + str(fuck_you_math_1), True, (255, 0, 0))
        win.blit(orientation_print, (180, 5))

        Signal_1_Display = font.render("Signal 1 : " + str(sensor_new.sig_1), True, (75, 175, 255))
        win.blit(Signal_1_Display, (340, 5))

        Signal_2_Display = font.render("Signal 2 : " + str(sensor_new.sig_2), True, (75, 175, 255))
        win.blit(Signal_2_Display, (480, 5))

        Signal_3_Display = font.render("Signal 3 : " + str(sensor_new.sig_3), True, (75, 175, 255))
        win.blit(Signal_3_Display, (620, 5))

        pygame.display.update()

        # print(f"Previous Distance: {last_distance}, Current Distance: {distance}")    # To make sure that the last_distance is one step behind distance. And also this line must be executed during the transient period before when we equate the distance and last_distance.

        last_signal = [sensor_new.sig_1, sensor_new.sig_2, sensor_new.sig_3, orientation, -orientation]
        action = brain.update(last_reward, last_signal)
        scores.append(brain.score())
        car_1.bigBrain101_choice = action

        last_distance = distance
        car_1.history()

if __name__ == '__main__':
    main()