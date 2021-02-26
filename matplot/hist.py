from matplotlib import pyplot as plt,style
style.use('ggplot')

bins=[0,1,2,3,4,5]

x_values=[10,23,32,16,15,17,9,10]

plt.hist(x_values,bins,histtype='bars',rwidth=0.8,label='Something label',color='k')

plt.Xlabel='X AXIS'
plt.Ylabel='Y AXIS'

plt.legend()

plt.show()
