import math
import numpy as np
'''
print(1/(math.e**(-100)+1))
print(1/(math.e**(100)+1))
print(1/(math.e**(-10)+1))
print(1/(math.e**(10)+1))
print()
print(math.e**(-100)/(math.e**(-100)+1)**2)
print(math.e**(100)/(math.e**(100)+1)**2)
print(math.e**(-10)/(math.e**(-10)+1)**2)
print(math.e**(10)/(math.e**(10)+1)**2)
print()

result1 = 0
result2 = 0 
listp = [1,6,12,5,2,8,12,4]
listq = [1,3,6,8,15,10,5,2]
for i in range(len(listp)):
    result1 += listp[i]/50*math.log(listp[i]/listq[i])
    result2 += listq[i]/50*math.log(listq[i]/listp[i])

print(result2)
'''
x = np.array([-15,22,-44,56])
y = [0,0,1]
w = [[0.01,-0.05,0.1,0.05],
     [0.7,0.2,0.05,0.16],
     [0.0,-0.45,-0.2,0.03]]
b = [0.0,0.2,-0.3]
y0 = np.dot(w,x.T) + b
print(y0)
resultSoftmax =0
resultSVM =0
s = 0 
for i in range(len(y)):
    s += math.e**y0[i]
    if y[i] ==1:
        target = i
for i in range(len(y)):
    resultSoftmax += y[i]*math.log(s/math.e**y0[i])
    if i != target:
        resultSVM += max(0,y0[i]-y0[target]+1)
print(resultSoftmax)
print(resultSVM)
