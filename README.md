# 2D_Self_Driving_Car_Python_3

Warning: This application is far from perfect and have some issues that has yet to be solved... 
- Do not use the Override function when you are training the AI.
- The Cosine Rule sometimes return a domain error.
- Insufficient amount of data given to the car for it to optimize for the best route. Thus it will ignore the road and instead just crash onto it... 
- Sometimes suicide and crash into the sand which is attributed to finding new approach to finish each epoch.
- The reward function is not optimized for the car to find the shortest path... Leading to the car commiting weird acts to reach its goal. 

This is a Deep Reinforcement Learning application specifically Deep Q-Learning. 
Ensure that your python interpreter is 3.7 or later. 
There are many python libraries required to run this application: numpy, math, matplotlib, pygame, os, random, pytorch.
To execute the application, just run the "map.py" file. 
If your IDE is unable to run it, go to CMD, cd to that project directory, and then enter the command: python map.py
To use the Override function, click on it and you can use your keyboard to control the car.

All icons are obtained from flaticon. 

