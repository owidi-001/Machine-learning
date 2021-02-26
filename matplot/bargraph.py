from matplotlib import pyplot as plt,style
style.use('ggplot')

plt.bar([23,43,54,64,75],[53,2,34,65,22],label='First data')

plt.bar([53,2,54,65,22],[23,43,54,64,75],label='Second data',color='k')

plt.title("Test variables")
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()
plt.show()
