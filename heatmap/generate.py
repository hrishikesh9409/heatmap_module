import random
import time
import numpy as np

a = []
b = []

random.seed(time.time())

N = 1002  # no of samples
x = range(N)
y = str([random.uniform(0,1000) for i in x])
list_d = ''.join(y)
myarray = []
item = 2
for item in list_d.split(','): # comma, or other
    myarray.append(item)

i = 0
for i in xrange (N):
	if(i % 2 == 0):
		a.append(myarray[i])
	else:
		b.append(myarray[i])

c = []
d = []

index = 1
while(index < len(a) - 1):
	c.append(float(a[index]))
	d.append(float(b[index]))
	index = index + 1

# index = 0
# while(index < len(c)):
# 	print str(int(c[index])) + "\t" + str(int(d[index]))
# 	index = index + 1

file = open("list.csv", "w")
index = 0
while(index < len(c)):
    file.write(str(int(c[index])) + "\t" + str(int(d[index])) + "\n")
    index = index + 1
file.close()