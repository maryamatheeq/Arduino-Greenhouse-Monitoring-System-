from engi1020.arduino.api import*
from math import log
from time import sleep
import matplotlib.pyplot as plt
import numpy as np


f=100
X_values_l = []
X_values_i = []

f_temp = open("temp.txt", "w")
f_temp.write("Temp: \n")
f_temp.close()

f_light = open("light.txt","w")
f_light.write("Light: \n")
f_light.close()

#Opening and writing the values of temperature and light in 2 seperate text files

for i in range(0, 50, 1):
    f_temp = open("temp.txt", "a")
    temp= pressure_get_temp()
    print(temp)
    f_temp.write(str(temp) + '\n')
    X_values_l.append(temp)
    f_temp.close()
    
    
    f_light = open("light.txt", "a")
    light=analog_read(6)
    print(light)
    f_light.write(str(light) + '\n')
    X_values_i.append(light)
    f_light.close()
    
    
    click=digital_read(6)
    
    rgb_lcd_print('light:'+str (light), 0,0)
    rgb_lcd_print('temp:'+str (temp) [:5],1,0)
    #Printing values of temperature and light on RGB LCD screen
    
    
    if light>500:
        #rgb_lcd_print('HIGH LIGHT LEVEL')
        digital_write(4,True)
        #led turns on
        digital_write(7,False)
        digital_write(2,False)
        servo_set_angle (3,120)
        #servo motor moves 120 degrees
        
    elif light<200:
        #rgb_lcd_print('LOW LIGHT LEVEL')
        servo_set_angle (3,10)
        #led turns off
        digital_write(4,False)
     #servo motor moves 10 degrees
        
        
    if light>200 and light<500 and temp<=27:
        rgb_lcd_colour(100,100,100)
        #white
    elif light<200 and temp<=27:
            rgb_lcd_colour(0,50,100)
        #blue
    elif light>500 and temp<=27:
            rgb_lcd_colour(0,250,100)
        #cyan
    elif light>500 and temp<=27:
            rgb_lcd_colour(0,100,250)
        #light blue
    elif light<200 and temp>27:
            rgb_lcd_colour(0,50,250)
        #blue(intense)
    else:
            rgb_lcd_colour(0,250,250)
        #bright blue

    #Temp and Light influenced part 
    if light<200 or temp>27 and click==False:
            buzzer_note(5,f,1)
            if f<800:
                f=f+25
    elif click==True:
            buzzer_stop(5)
            f=100
    sleep(1)
    rgb_lcd_clear()

for i in range(0, len(X_values_l), 1):
    Y = np.array(X_values_l[i])
    X = np.array(i)
    plt.scatter(X, Y)

plt.plot(X_values_l, 'r--')
plt.xlabel('Order of Values')
plt.ylabel('Temperature Value')
plt.show()

for i in range(0, len(X_values_i), 1):
    Y = np.array(X_values_i[i])
    X = np.array(i)
    plt.scatter(X, Y)
        
plt.plot(X_values_i, 'g--')
plt.xlabel('Order of Values')
plt.ylabel('Light Value')
plt.show()

#Plotting graphs of temperature and light based on the data 
    



    
    
    
    
