#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:51:21 2019

@author: shoichi
"""

import numpy as np
import sklearn.datasets
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout#,advanced_activations
from sklearn.metrics import confusion_matrix
import time

np.random.seed(0)
X,y=sklearn.datasets.make_moons(200,noise=0.20)
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
np_epoch = 2000

model = Sequential()
model.add(Dense(output_dim=6, input_dim=2))
model.add(Activation('tanh'))#keras.layers.PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=None)
model.add(Dense(output_dim=2))
model.compile(optimizer='Adam',loss='mse')#Optimizer 勾配更新方法

x_train = X
y_train = keras.utils.np_utils.to_categorical(y,2)#y_train = keras.utils.np_utils.to_categorical(y, nb_classes=2)より訂正
start=time.time()
result = model.fit(x=x_train, y=y_train, nb_epoch=np_epoch)
end=time.time()-start

def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

def predict(model, x_data):
    y = model.predict(x_data)
    return np.argmax(y.data, axis=1) # 最大値となるインデックスを取得

def plot_error_propagation():
    plt.figure()
    plt.plot(range(1, np_epoch+1), result.history['loss'], label="loss")
    plt.ylim([0,1.5])
    plt.xlabel('Epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.show()



plot_decision_boundary(lambda x: predict(model, x))
plot_error_propagation()
y_pre = predict(model, X)
CM = confusion_matrix(y,y_pre)
print(confusion_matrix(y,y_pre))
print('TN')
print(CM[0][0])
TN = CM[0][0]
print('FP')
print(CM[0][1])
FP = CM[0][1]
print('FN')
print(CM[1][0])
FN = CM[1][0]
print('TP')
print(CM[1][1])
TP = CM[1][1]
#精度（Accuracy）: (TN+TP)/(TN+FN+FP+TP)
print('精度')
print((TN+TP)/(TN+FN+FP+TP))
#適合率（Precision）： TP/(TP+FP)
print('適合率')
print((TP/(TP+FP)))
#再現率（Recall）：TP/(TP+FN)
print('再現率')
print((TP/(TP+FN)))
print('処理時間')
print(end)

