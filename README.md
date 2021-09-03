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

The reason which I have to make this project is that the original code provided by the course doesn't work and uses deprecated Python2. 
It was also quite an experience to have to build this project up from scratch. 
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

## Training Environment
![github-small](https://github.com/YEOWEIHNGWHYELAB/2D-Self-Driving-Car-Python3/blob/master/Images/EnvironmentWithObstacles.png)

## Performance diagnostics
![github-small](https://github.com/YEOWEIHNGWHYELAB/2D-Self-Driving-Car-Python3/blob/master/Images/PerformanceDiagnostics.png)

The reward is getting better overtime but due to the limitation of the parameters feed into the AI, it is rather difficult for the AI to even be able to make out how to navigate through the obstacles. Moreover, there is no Computer Vision used at all. It is just able to sense the obstacle in front of it. Thus the AI is probably unable to see long term consequences for taking a particular action. But nevertheless, its a very good beginners project. A lot of trial and error is required in order to be able to ensure that the AI is learning correctly and doing the right things. The AI is generally ok at driving around most of the obstacles shapes but however, there are cases where tweaks to the obstacle is needed to correct the AI for example: making obstacle thicker in order to maximize the severity of the punishment so that the AI is not committing the same infraction. Because there are times when the AI just refuses to avoid an obstacle because the reward is still in the long run high enough that it isn't significant to trigger the AI to avoid crashing into certain obstacle.   

Udemy Site: https://www.udemy.com/course/artificial-intelligence-az/

All icons are obtained from flaticon.  
Check them out: https://www.flaticon.com/
