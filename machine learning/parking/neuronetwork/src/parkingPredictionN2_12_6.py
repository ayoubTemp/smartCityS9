'''
Created on Dec 15, 2016

@author: lusha
'''


import numpy as np

inputSize = 12
alphas = [0.001,0.01,0.1,1,10,100]
hiddenSize1 = 12
hiddenSize2 = 6

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
    
X = np.array([[0,0,1,8,1,0,1,2,1,1,1,2],
            [0,1,1,9,0,0,4,6,1,0,1,2],
            [1,0,1,6,0,0,1,1,0,2,3,1],
            [1,1,1,5,0,0,1,1,0,4,1,1]])
                
y = np.array([[0],
            [0.8],
            [0.95],
            [0.2]])

for alpha in alphas:
    print "\nTraining With Alpha:" + str(alpha)
    np.random.seed(1)

    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((inputSize,hiddenSize1)) - 1
    synapse_1 = 2*np.random.random((hiddenSize1,hiddenSize2)) - 1
    synapse_2 = 2*np.random.random((hiddenSize2,1))-1

    for j in xrange(60000):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0,synapse_0))
        layer_2 = sigmoid(np.dot(layer_1,synapse_1))
        layer_3 = sigmoid(np.dot(layer_2,synapse_2))

        # how much did we miss the target value?
        layer_3_error = layer_3 - y
        

        if (j% 10000) == 0:
            print "Error after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_3_error)))

        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        
        layer_3_delta = layer_3_error*sigmoid_output_to_derivative(layer_3)
        
        layer_2_error = layer_3_delta.dot(synapse_2.T)
        
        layer_2_delta = layer_2_error*sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_2 -= alpha * (layer_2.T.dot(layer_3_delta))
        synapse_1 -= alpha * (layer_1.T.dot(layer_2_delta))
        synapse_0 -= alpha * (layer_0.T.dot(layer_1_delta))
        
    print "Output After Training:"
    print layer_3
