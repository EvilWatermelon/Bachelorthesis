import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import BatchNormalization
import keras
import matplotlib.pyplot as plt
import tensorboard
from time import time

np.random.seed(42)

#train_samples
fFloat = open("Your\\Path\\To\\Trainingsdata","r")
X = np.loadtxt(fFloat, delimiter=",", dtype=float); fFloat.close()
#train_labels
fFloat = open("Your\\Path\\To\\Training\\Positions","r")
Y = np.loadtxt(fFloat, delimiter=",", dtype=float); fFloat.close()

yMin = Y.min(axis=0); yMax = Y.max(axis=0)
Y = (Y - yMin) / (yMax - yMin)

TrainSet = np.random.choice(X.shape[0],int(X.shape[0]*0.80), replace=False)
XTrain = X[TrainSet,:]
YTrain = Y[TrainSet]
TestSet = np.delete(np.arange(0, len(Y) ), TrainSet)
XTest = X[TestSet,:]
YTest = Y[TestSet]

myANN = Sequential()

myANN.add(Dense(8, input_dim=8, kernel_initializer='normal'))
myANN.add(Dense(8, kernel_initializer='normal', activation='sigmoid', use_bias=True))
myANN.add(BatchNormalization())
myANN.add(Dense(3, kernel_initializer='normal', activation='sigmoid', use_bias=True))
myANN.compile(loss='mean_squared_error', optimizer='adam')

history = myANN.fit(XTrain, YTrain, epochs=1000, verbose=False)
print(history)
yp = myANN.predict(XTest)
yp = yp.reshape(yp.shape[0], -1)
errorT = (yMax - yMin) * (yp - YTest)
#print(np.mean(np.abs(errorT)))
for i in range(len(XTest)):
    print(str(XTest[i]) + ";" + str(yp[i]))

print("Error: " + str(np.mean(np.abs(errorT))))

train_loss=history.history['loss']
xc=range(1000)

plt.figure(1, figsize=(7,5))
plt.plot(xc, train_loss)
plt.xlabel('num of Epochs')
plt.ylabel('loss')
plt.title('train_loss')
plt.grid(True)
plt.legend(['train_loss'])
plt.style.use(['classic'])
plt.show()
