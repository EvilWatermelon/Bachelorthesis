from matplotlib import pyplot as plt
#from array_split import array_split, shape_split
import numpy as np
import sys
import array as arr

#sits - lies - empty
dataset = []
cstm_pred = []

# activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

def train():
    with open("values.txt") as f:
        dataset = [[int(x) for x in line.split(",")] for line in f]
        print(dataset)
    
    #random init of weights
    w1, w2, w3 = np.random.randn(), np.random.randn(), np.random.randn()
    w4, w5, w6 = np.random.randn(), np.random.randn(), np.random.randn()
    w7, w8, w9 = np.random.randn(), np.random.randn(), np.random.randn()
    #biases
    b1, b2, b3 = np.random.randn(), np.random.randn(), np.random.randn()
    
    iterations = 10000
    learning_rate = 0.1
    costs = [] # keep costs during training, see if they go down
    
    for i in range(iterations):
        # get a random point
        ri = np.random.randint(len(dataset))
        point = dataset[ri]
        
        x = point[0] * w1 + point[1] * w2 + point[2] * w3 + b1
        y = point[0] * w4 + point[1] * w5 + point[2] * w6 + b2
        z = point[0] * w7 + point[1] * w8 + point[2] * w9 + b3
        pred1 = sigmoid(x) # networks prediction
        pred2 = sigmoid(y)
        pred3 = sigmoid(z)
        
        target1 = point[3]
        target2 = point[4]
        target3 = point[5]
        
        # cost for current random point
        cost1 = np.square(pred1 - target1)
        cost2 = np.square(pred2 - target2)
        cost3 = np.square(pred3 - target3)
        # print the cost over all data points every 1k iters
        if i % 100 == 0:
            c1 = 0
            c2 = 0
            c3 = 0
            for j in range(len(dataset)):
                p = dataset[j]
                p_pred1 = sigmoid(w1 * p[0] + w2 * p[1] + w3 * p[2] + b1)
                p_pred2 = sigmoid(p[0] * w4 + p[1] * w5 + p[2] * w6 + b2)
                p_pred3 = sigmoid(p[0] * w7 + p[1] * w8 + p[2] * w9 + b3)
                c1 += np.square(p_pred1 - p[3])
                c2 += np.square(p_pred2 - p[4])
                c3 += np.square(p_pred3 - p[5])
            costs.append(c1)
            costs.append(c2)
            costs.append(c3)
            
        dcost_dpred1 = 2 * (pred1 - target1)
        dcost_dpred2 = 2 * (pred2 - target2)
        dcost_dpred3 = 2 * (pred3 - target3)
        
        dpred_dz1 = sigmoid_p(x)
        dpred_dz2 = sigmoid_p(y)
        dpred_dz3 = sigmoid_p(z)
        
        dz_dw1 = point[0]
        dz_dw2 = point[1]
        dz_dw3 = point[2]
        dz_db = 1
        
        dcost_dz1 = dcost_dpred1 * dpred_dz1
        dcost_dz2 = dcost_dpred2 * dpred_dz2
        dcost_dz3 = dcost_dpred3 * dpred_dz3
        
        dcost_dw1 = dcost_dz1 * dz_dw1
        dcost_dw2 = dcost_dz2 * dz_dw2
        dcost_dw3 = dcost_dz3 * dz_dw3
        dcost_db1 = dcost_dz1 * dz_db
        dcost_db2 = dcost_dz2 * dz_db
        dcost_db3 = dcost_dz3 * dz_db
        
        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        w3 = w3 - learning_rate * dcost_dw3
        
        w4 = w4 - learning_rate * dcost_dw1
        w5 = w5 - learning_rate * dcost_dw2
        w6 = w6 - learning_rate * dcost_dw3
        
        w7 = w7 - learning_rate * dcost_dw1
        w8 = w8 - learning_rate * dcost_dw2
        w9 = w9 - learning_rate * dcost_dw3
        b1 = b1 - learning_rate * dcost_db1
        b2 = b2 - learning_rate * dcost_db2
        b3 = b3 - learning_rate * dcost_db3
         
    return costs, w1, w2, w3, w4, w5, w6, w7, w8, w9, b1, b2, b3

var0 = int(input("Please enter number 1: "))
cstm_pred.append(var0)
print("You added: ", var0)

var1 = int(input("Please enter number 2: "))
cstm_pred.append(var1)
print("You added: ", var1)

var2 = int(input("Please enter number 3: "))
cstm_pred.append(var2)
print("You added: ", var2)

print(cstm_pred)

costs, w1, w2, w3, w4, w5, w6, w7, w8, w9, b1, b2, b3 = train()

x = cstm_pred[0] * w1 + cstm_pred[1] * w2 + cstm_pred[2] * w3 + b1
y = cstm_pred[0] * w4 + cstm_pred[1] * w5 + cstm_pred[2] * w6 + b2
z = cstm_pred[0] * w7 + cstm_pred[1] * w8 + cstm_pred[2] * w9 + b3

pred1 = sigmoid(x)
pred2 = sigmoid(y)
pred3 = sigmoid(z)

print("pred1: ", pred1, "sitzen")
print("pred2: ", pred2, "liegen")
print("pred3: ", pred3, "leer")

var = input("Please enter yes or no: ")
print("You entered: " + var)

if var == "yes":
    file2write=open("values.txt",'a')
    file2write.write(str(pred1) + "," + str(pred2) + "," + str(pred3) + "\n")
    file2write.close()
elif var == "no":
    print("Prediction was not correct!")