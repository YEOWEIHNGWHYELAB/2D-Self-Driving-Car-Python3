# 2D_Self_Driving_Car_Python_3

This is my first Python project, it isn't perfect and have a few issues. I have learnt this from the course Artificial Intelligence A-Z™: Learn How To Build An AI. Its a very good course. Check them out at the link below. My ai.py code is referenced from them.

This application is not perfect and there are several things that will be added and fixed in the future.
- Do not use the Override function when you are training the AI.
- The Cosine Rule function sometimes return a domain error.
- Insufficient amount of data given to the car for it to optimize for the best route. Thus it will ignore the road and instead just crash onto it... 
- Sometimes suicide and crash into the sand which is attributed to finding new approach to finish each epoch.
- The reward function is not optimized for the car to find the shortest path... Leading to the car commiting weird acts to reach its goal. 
- The buttons on screen is not reliable. 
- The erase button has not been added. 

This is a Deep Reinforcement Learning application specifically Deep Q-Learning. 
Ensure that your python interpreter is 3.7 or later. 
There are many python libraries required to run this application: numpy, math, matplotlib, pygame, os, random, pytorch.
Ensure you install the correct version of pytorch, for instance if your machine does have CUDA, then you should intall the version with CUDA to accelerate the AI process. Otherwise it will pin your CPU to death. 
To execute the application, just run the "map.py" file. 
If your IDE is unable to run it, go to CMD, cd to that project directory, and then enter the command: python map.py.
To use the Override function, click on it and you can use your keyboard's left and right arrow to control the car.
Use your cursor to draw the road.
If you want to erase part of your road, you must clear everything...
If you give the AI enough training time, the AI will actually do quite well in the environments that you have made. 
To think about: Is it really a requirement to pass in 2 orientation values to the AI one is a negative of the other to the AI? Removing one of it doesn't really change anything in my opinion since both are practically the same with just a additive inverse. 

Udemy Site: https://www.udemy.com/course/artificial-intelligence-az/

All icons are obtained from flaticon.  
Check them out: https://www.flaticon.com/
