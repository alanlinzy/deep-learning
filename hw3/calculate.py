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
'''
'''
exp1 = np.exp(-0.25*0.63)
print(exp1)
y1 = 1/(1+exp1)
print(y1)
exp2 = np.exp(0.11*y1)
print(exp2)
y2 = 1/(1+exp2)
print(y2)
exp3 = np.exp(-0.78*y2)
print(exp3)
y3 =  1/(1+exp3)
print(y3)
print()
ls = - 1/y3 
print(ls)
dexp3 = exp3/(1+exp3)**2
dw3 = ls*dexp3*y2
print(dw3)
dexp2 = exp2/(1+exp2)**2
dw2 = ls*dexp3*0.78*dexp2*y1
print(dw2)
dexp1 = exp1/(1+exp1)**2
dw1 = ls*dexp3*0.78*dexp2*(-0.11)*dexp1*0.63
print(dw1)
print("-----------")

exp01 = np.exp(-0.25*0.63)
print(exp01)
y01 = 1/(1+exp01)
print(y01)
exp02 = np.exp(0.11*y01)
print(exp2)
y02 = 1/(1+exp02)
print(y2)
y03 =  0.78*y02
print(y03)
print()
ls0 = -2*(1-y03)
print(ls0)
dw03 = ls0*y02
print(dw03)
dexp02 = exp02/(1+exp02)**2
dw02 = ls0*0.78*dexp02*y01
print(dw02)
dexp01 = exp01/(1+exp01)**2
dw01 = ls0*0.78*dexp02*(-0.11)*dexp01*0.63
print(dw01)
print("3------------")
ls1 = -2*(128-y03)
print(ls1)
dw13 = ls1*y02
print(dw13)
dexp12 = exp02/(1+exp02)**2
dw12 = ls1*0.78*dexp12*y01
print(dw12)
dexp11 = exp01/(1+exp01)**2
dw11 = ls1*0.78*dexp12*(-0.11)*dexp11*0.63
print(dw11)
'''

