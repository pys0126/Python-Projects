name = input('你的名字：')
name1 = input('她/他的名字：')
str1 = ' ' + name + 'Love' + name1
print('\n'.join([''.join([(str1[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
