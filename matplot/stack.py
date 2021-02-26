from matplotlib import pyplot as plt,style
style.use('ggplot')

days=[1,2,3,4]

sleep=[12,3,5,6]
eat=[5,10,4,7]
work=[9,4,5,2]
play=[1,4,0,7]

plt.plot([],[],label='sleep',linewidth=4)
plt.plot([],[],label='eat',linewidth=4)
plt.plot([],[],label='work',linewidth=4)
plt.plot([],[],label='play',linewidth=4)

plt.stackplot(days,sleep,eat,work,play)

plt.show()