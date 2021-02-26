from matplotlib import pyplot as plt,style
style.use('ggplot')


x=[23,43,54,64,75]
y=[53,2,34,65,22]

y2=[23,43,54,64,75]
x2=[53,2,54,65,22]

plt.scatter(x,y,marker='X',label='First data',color='k')
plt.scatter(x2,y2,marker='o',label='Second data',color='g')

plt.title("Test variables")
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()
plt.show()
