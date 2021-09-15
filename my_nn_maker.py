import numpy as np
import math

def net_init(layers_count,layers_shapes,include_bias = True):#return weights and biases
    w =  [np.random.randn(layers_shapes[i]).reshape((layers_shapes[i],1)) for i in range(layers_count)]
    b = np.zeros((layers_count,1))
    if include_bias:
        return w,b
    return w

def sigmoid(x):
    return np.float64(1)/(np.float64(1)+np.exp(-x))

def relu(x):
    return x*(x>0)

def linear(x): return x

def compute_derivative(f,x,dx=10**(-8)):# return function derivative at point x
    return (f(x+dx)-f(x-dx))/(2.*dx)

def forwpropagation(w,b,x,activation=sigmoid,activations=[]):
    # z = w[1:].T@x[sample] + w[0]
    # y_pred = a = sigmoid(z)
    # L(a,y) = -(ylog(a)+(1-y)log(1-a))

    a = x
    z_cached = []
    a_cached = []
    if activations:
        for layer in range(len(w)):
            z = w[layer].T@a + b[layer]
            z_cached += [z]
            a = activations[layer](z)
            a_cached += [a]
        return a,z_cached,a_cached

    for layer in range(len(w)):
        z = w[layer].T@a + b[layer]#w.T@x + b
        z_cached += [z]
        a = activation(z)
        a_cached += [a]
    return a,z_cached,a_cached

def backpropagation(w,b,z_cached,activations,error,lr=0.001,m = 1):
	#backpropagation(Weights,biases,Z's,activations on layers,error,learning rate,num of examples)
	#return None - changing parameters
    dw = [None for _ in range(len(w))]
    db = [None for _ in range(len(b))]#suppose len(b) == len(w)
    for i in range(len(w)):
        dw[-i] = 1/m * np.sum(error*compute_derivative(activations[-i],z_cached),axis=1)
        db[-i] = dw[-i]
        error = df[-i].dot(w[-i-1])
        w[-i] = w[-i] - lr*dw[-i]
        b[-i] = b[-i] - lr*d

#some cost functions and metrics
def binary_crossentropy(y,actual):
    return -1./y.shape[1] * np.sum(actual*np.log(y)+(1-actual)*np.log(1-y))

def sparse_categorical_crossentropy(y,actual):
    return -np.sum(actual*np.log(y))

def RMSE(y,actual):
    return sum(math.sqrt(((y-actual)**2)/y.shape[0]))

def MSE(y,actual):
    return sum(((y-actual)**2)/y.shape[0])

def nMSE(n,y,actual):
    return sum((((y-actual)**2)/y.shape[0])**(1./n))

def l2_regularization(w,l,m):
    #w - weights matrix
    #l - lambda (regularization rate)
    #m - count of examples
    return l/(2*m) * np.sum([x**2 for x in w])


def acc(y_actual,y_pred):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for i in range(y_pred.shape[1]):
        if y_actual[i] == 0:
            if y_pred[i] == 0:
                TN += 1
            else:
                FP +=1

        else:
            if y_pred[i] == 1:
                TP += 1
            else:
                FN += 1
    return (TP+TN)/(TP+FP+FN+TN)

