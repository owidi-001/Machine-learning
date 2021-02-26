try:
    lines=open('sample4.csv','r').read().split('\n')
    

except IOError:
    print('file not read')
