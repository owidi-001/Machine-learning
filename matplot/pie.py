from matplotlib import pyplot as plt,style
style.use('ggplot')

slices=[2,7,8,4,12]
activities=['run','sleep','eat','work','fun']

plt.pie(slices,labels=activities,startangle=90,autopct='%0.1f%%',explode=(0.2,0.1,0.1,0.1,0.1))

plt.show()