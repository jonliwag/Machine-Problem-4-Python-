# libraries to be used
import math as math
import numpy as np
import matplotlib.pyplot as plt

# setting the inputs of user
iHeight = float(input('Please input initial height in meters: '))
iVel = float(input('Please input initial velocity in m/s: '))
dAngle = float(input('Please input the angle in degrees: '))
xAcc = float(input('Please input the acceleration x-component in m/s: '))
yAcc = float(input('Please input the acceleration y-component in m/s: '))

# since 0 vertical acceleration is zero 
if yAcc == 0:
    print('error!')
    quit()
    
dAngle = math.radians(dAngle)

# formulas for velocity in x and y 
xVel = iVel*math.cos(dAngle)
yVel = iVel*math.sin(dAngle)

# since  y = 1/2(ay)(t)^2 + vy(t)
eq1 = [yAcc/2, yVel, iHeight]

# getting the roots (time)
# use 'max' to use the larger number which is the positive one 
# since there is no negative time
time = max(np.roots(eq1))

interval = np.arange(0, time, 0.1)
x = np.zeros((len(interval), 1))
y = np.zeros((len(interval), 1))

ti = 0.1

y[0, 0] = iHeight

n = np.arange(0, len(interval), 1)

#using for loop
for i in n:    
#using formula for displacement in x and y   
    xDisp = (xAcc * (ti**2)) / 2 + (xVel * ti)
    yDisp = (yAcc*(ti**2)) / 2 + (yVel*ti + iHeight)
    x[i, 0] = xDisp
    y[i, 0] = yDisp
    ti = ti + 0.1

plt.grid(True)
plt.xlabel('distance in x')
plt.ylabel('height above ground')    
fig = plt.plot(x,y, 'r')


