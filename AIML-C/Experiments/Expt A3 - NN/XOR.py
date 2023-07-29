import numpy as np

def step_func(x):
    if x >= 0:
       return 1
    else:
       return 0

def lin_func(x, w, b):
    t = np.dot(x, w) + b
    y = step_func(t)
    return y

def and_func(x):
    w = np.array([1, 1])
    b = -1.5
    return lin_func(x, w, b)

def or_func(x):
    w = np.array([1, 1])
    b = -0.5
    return lin_func(x, w, b)

def not_func(x):
    w = -1
    b = 0.5
    return lin_func(x, w, b) 

def xor_func(x):
    y1 = and_func([x[0], not_func(x[1])])
    y2 = and_func([not_func(x[0]), x[1]])
    y = or_func([y1,y2]) 
    return y

test1 = xor_func([0, 0])
test2 = xor_func([0, 1])
test3 = xor_func([1, 0])
test4 = xor_func([1, 1])

print('xor output of [0, 0] = ', test1)
print('xor output of [0, 1] = ', test2)
print('xor output of [1, 0] = ', test3)
print('xor output of [1, 1] = ', test4)


