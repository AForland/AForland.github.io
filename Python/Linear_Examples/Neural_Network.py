# -*- coding: utf-8 -*-
import numpy as np
import scipy.special
import matplotlib.pyplot
from PIL import Image

#########input#################
L = 6 # vector to try letter
##############################

# neural network class definition
class neuralNetwork:

    # initialise the neural nwtwork
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, and output layers
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from niode i to node j in the next layer.
        self.wih = np.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who = np.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))

        # learning rate
        self.lr = learningrate

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # train the neural network
    def train(self, inputs_list , targets_list):

        # convert inputs list to a 2d array
        inputs = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T

        # calculate singles into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)

        # calculate the singnals emerging for the hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate singals into final output layer
        final_inputs = np.dot(self.who,hidden_outputs)

        # calculate singals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        #output layer error is the (target - actual)
        output_errors = targets - final_outputs

        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = np.dot(self.who.T,output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

        pass

    def matrix_collect(self):
        np.savetxt('/home/adam/Desktop/wih.csv',self.wih)
        np.savetxt('/home/adam/Desktop/who.csv',self.who)
        pass

# number of input, hidden and output nodes
input_nodes = 784 # 28X28 the size of each character
hidden_nodes = 100 # number of hidden nodes (higher the better)
output_nodes = 10 # [0,1,2,3,4,5,6,7,8,9] (.01 = 0 and 0.99 = 1)

# learning rate
learning_rate = 0.1

# create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load the training data into a list
training_data_file = open("/home/adam/Desktop/mnist_train.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# train the neural network

epochs = 5

for e in range(epochs):
    # go through all records in the training data set
    for record in training_data_list:
        # split the record by the ',' commas
        all_values = record.split(',')
        # scale and shift the inputs
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        targets = np.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass

n.matrix_collect()
