import matplotlib.pyplot as plt

working = [9,6,9,6]
sleeping = [8,8,8,8,]
free_time = [7,10,7,10]
x = ['Sunday','Monday','Tuesday','Wednesday']
plt.stackplot(x,working,sleeping,free_time,colors = ['b','r','m'])
plt.plot([],[],label = 'Working',color ='b',linewidth = 5)
plt.plot([],[],label = 'Sleeping',color ='r',linewidth = 5)
plt.plot([],[],label = 'Free Time',color ='m',linewidth = 5)
plt.xlabel('x Axis')
plt.ylabel('y Axis')
plt.legend()
plt.show()

