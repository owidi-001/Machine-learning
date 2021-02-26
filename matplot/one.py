from matplotlib import pyplot as plt,style

style.use('ggplot')


x=[23,43,54,64,75]
y=[53,2,534,65,22]

y2=[23,43,54,64,75]
x2=[53,2,534,65,22]

plt.plot(x,y,label="First line",marker='X')
# plt.plot(x2,y2,label='Second line',linewidth=5,marker='o')

plt.title("Test variables")
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()

plt.show()