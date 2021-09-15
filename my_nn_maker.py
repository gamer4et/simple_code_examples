import numpy as np
import math

def net_init(layers_count,layers_shapes):#return weights and biases
    w =  [np.random.randn(layers_shapes[i]).reshape((layers_shapes[i],1)) for i in range(layers_count)]
    b = np.zeros((layers_count,1))
    return w

def sigmoid(x):
    return np.float64(1)/(np.float64(1)+np.exp(-x))

def relu(x):
    return x*(x>0)

def linear(x): return x

def derivative(f,x,dx):# return function derivative at point x
    return (f(x+dx)-f(x-dx))/(2.*dx)

def forward_prop(w,b,x,activation=sigmoid,activations=[]):
    # z = w[1:].T@x[sample] + w[0]
    # y_pred = a = sigmoid(z)
    # L(a,y) = -(ylog(a)+(1-y)log(1-a))
    if activations:
        pass
    a = x
    z_cached = []
    a_cached = []

    for layer in range(len(w)):
        z = w[layer].T@a + b[layer]#w.T@x + b
        z_cached += [z]
        a = activation(z)
        a_cached += [a]
    return a,z_cached,a_cached

def backward_prop(y_actual,y_predicted,w,b,activations,z_cached,a_cached):
    a = y_actual
    dz = a-y_predicted
    m = y_actual.shape[1] #num of examples
    dw = np.zeros(len(w))
    db = np.zeros(b.shape)
    for i in range(len(w)):
        dw[-i] = 1/m*dz@a_cached[-(i+1)].T
        db[-i] = 1/m*np.sum(dz,axis=0,keepdims=True)
        w[-i] += dw[-i]
        b += db

    return w,b

#some cost functions
def binary_crossentropy(y,actual):
    return -1./y.shape[0] * np.sum(actual*np.log(y)+(1-actual)*np.log(1-y))

def sparse_categorical_crossentropy(y,actual):
    return -np.sum(actual*np.log(y))

def RMSE(y,actual):
    return sum(math.sqrt(((y-actual)**2)/y.shape[0]))

def MSE(y,actual):
    return sum(((y-actual)**2)/y.shape[0])

def nMSE(n,y,actual):
    return sum((((y-actual)**2)/y.shape[0])**(1./n))
