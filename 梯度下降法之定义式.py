import numpy as np

x = 0.1*np.array([[1, 2, 3]])
w1 = 0.1*np.array([[2, 3, 1],
               [1, 2, 2],
               [3, 2, 1]])

w2 = 0.1*np.array([[1, 2],
               [1, 3],
               [2, 1]])
d = [[2, 3]]
def foreward(x, w):
    x = x.dot(w)
    return x

def MSE(y, d):
    return 0.5*((y - d)**2)

def dout(x, w1, w2, d):
    h = 1e-4  # 0.0001
    w1_height, w1_width = w1.shape
    w2_height, w2_width = w2.shape
    for i in range(w1_height):
        for j in range(w1_width):
            temp = w1[i, j]
            w1[i, j] = temp + h
            y1 = MSE(foreward(foreward(x, w1), w2), d)
            w1[i, j] = temp - h
            y2 = MSE(foreward(foreward(x, w1), w2), d)
            grad = (y1 - y2) / (2*h)
            grad = np.sum(grad)
            #print(grad[0, 1])
            w1[i, j] = temp - 0.01*grad
            #w1[i, j] = temp - 0.01*grad[0, 1]
    for k in range(w2_height):
        for l in range(w2_width):
            temp = w2[k, l]
            w2[k, l] = temp + h
            y1 = MSE(foreward(foreward(x, w1), w2), d)
            w2[k, l] = temp - h
            y2 = MSE(foreward(foreward(x, w1), w2), d)
            grad = (y1 - y2) / (2*h)
            grad = np.sum(grad)
            w2[k, l] = temp - 0.01*grad
            #w2[k, l] = temp - 0.01 * grad[0, 1]
'''
for i in range(1000):
    dout(x, w1, w2, d)

print(foreward(foreward(x, w1), w2))
'''
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
c = np.array([4, 5, 6])
print(np.r_[a, c])
print(a)
print(a.shape)
print(b)
print(b.shape)