import numpy as np

####################activation functions#######################
def relu(x,derivative=False):
    if derivative: return 1*(x>0)
    return x*(x>0)


def sigmoid(x,derivative=False):
    if derivative:
        s = 1./(1.+np.exp(-x))
        return s*(1-s)
    return 1./(1.+np.exp(-x))

def linear(x,derivative=False):
    if derivative: return 1
    return x
###############################################################


#####################metrics###################################
def binary_crossentropy(y_predicted,y_actual,eps=.0001):
    return -1/y_actual.shape[0] * np.sum(y_actual*np.log(y_predicted+eps) +(1-y_actual)*np.log(1-y_predicted+eps))

def sparse_categorical_crossentropy(y,actual):
    return -np.sum(actual*np.log(y))

def RMSE(y,actual):
    return sum(math.sqrt(((y-actual)**2)/y.shape[0]))

def MSE(y,actual):
    return sum(((y-actual)**2)/y.shape[0])

def nMSE(n,y,actual):
    return sum((((y-actual)**2)/y.shape[0])**(1./n))
#################################################################


###################Initialization################################

def init_shapes(layers):
	#returns list of shapes: [(2,3),(1,2)]
	#layers = [...(count_of_units,activation)...]
	to_ret = []
	for i in range(len(layers)-1):
		to_ret += [(layers[i+1][0],layers[i][0])]
	return to_ret

def init_activations(layers):
	#returns list of activations for each layer
	return [el[1] for el in layers]

def init_weights(shapes):
	#returns list of np.arrays with random weights
	# shapes = list of shapes
	#example 
	#shapes = [(2,3),(1,2)]
	return [np.random.randn(*shapes[i]) for i in range(len(shapes))]
#################################################################


def forward_propagation(Input,weights,activations):
	a = Input
	z_cached = []
	a_cached = []
	for current in range(len(weights)):
		z = weights[current]@a
		a = activations[current](z)
		z_cached += [z]
		a_cached += [a]
	return a,z_cached,a_cached


def backward_propagation(weights,activations,error,z_cached,lr=.0001):
	if type(error) not in (np.array,np.ndarray):
		error =np.array(error).reshape(1,1)
	layer_error = error
	for i in range(len(weights)):
		delta = layer_error*activations[-i](z_cached[-i],derivative=True)
		layer_error = delta@weights[-i-1]
		weights[-i] -= delta*lr
	return weights



if __name__ == "__main__":
	layers = [(3,linear),(2,relu),(1,sigmoid)]
	shapes = init_shapes(layers)
	activations = init_activations(layers)
	weights = init_weights(shapes)
	X = np.array([1.,1.,1.]).reshape(-1,1)
	y = np.array([[1.]])
	for i in range(100):
		y_pred,z_cached,a_cached = forward_propagation(X,weights,activations)
		err = binary_crossentropy(y_pred,y)
		weights = backward_propagation(weights,activations,err,z_cached)
		print(err)
