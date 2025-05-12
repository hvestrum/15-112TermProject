The modules needed to run the program are:
cmu_graphics
(pip install cmu_graphics)
google and google.generativeai
API key was removed from the code (SproutCoffee.py line 11)
(pip install google-generativeai)
opencv and mediapipe
(import cv2
import os
import mediapipe as mp)
threading
(import threading
import time)

The dependencies that we used for this project are CMU Graphics and Google 
Gemini API. CMU Graphics were used as the base of the project to build the game
which included rendering visuals and interactive components and Google Gemini 
API was integrated to generate customers' orders and reactions through
AI-generated prompts.

Sprout Coffee is a point-and-click game where the user plays as a barista
serving customers and their orders. The goal is to correctly prepare each
customer's coffee order, make the right drink and they'll be satisified, get it
wrong and you might have a grumpy customer! 
The game is over when the barista makes an incorrect order. 
The game repeats when the barista makes a correct order.

Use the SproutCoffee.py file to run the game.

