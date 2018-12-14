
#Hydrometer - by Alex Bishop 2018-12-08

#Code adapted from:
#http://www.toptechboy.com/tutorial/python-with-arduino-lesson-11-plotting-and-graphing-live-data-from-arduino-with-matplotlib/


import serial as ps # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import drawnow
import datetime as dt
import time as time
import numpy as np

plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

#turn on our serial port
S = ps.Serial('COM6', baudrate=115200)
S.inWaiting()
S.isOpen()
stop = 'go'
D = []
xdat = []



def makeFig():                                       #Create a function that makes our desired plot
    #plt.ylim(0,300)                                 #Set y min and max values
    plt.title('Specific Gravity vs. Time')           #Plot the title
    plt.grid(True)                                   #Turn the grid on
    plt.ylabel('Specific Gravity')                           #Set ylabels
    plt.plot(xdat, D, 'ro-', label='mm')             #plot the temperature
    plt.legend(loc='upper left')                     #plot the legend
    #plt.autofmt_xdate()
  

#for i in range(5): #for debugging, change to the While when not broken
while stop == 'go':

#this is the section on data collection
    S.reset_input_buffer() #start with a flush
        #print(i) # for debugging w/evan
        # Read a line from the Serial data object stored in 'S' 
    serialdata = S.readline() 
        #print(serialdata) #for debugging
    c = str(serialdata) #serial data was read as byte data .: need to convert to str
        #print("c=", c) #for debugging

# these try block will eliminate erroneous numbers, out of range numbers will be reproted as int(0)   
    try:
        a = float(c[2:5]) #str needs to be converted to a int
    except ValueError:
        try: 
            a = float(c[2:4])
        except:
            a = float(c[2:3])
    except: 
        pass

    #conversion to Specific Gravity
    sg = (a - 746) / -520
#record data of a into the array
    D.append(sg)
    
#Time stuff
    t = dt.datetime.now() 
        #now = d.strftime("%H:%M:%S")
        #xdat.append([now])
    xdat.append([t])
    time.sleep(1)
    np.savez('distdata',D=D,xdat=xdat)

    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    plt.savefig('demo graph.jpg', bbox_inches = 'tight')
    cnt=cnt+1

S.close()

