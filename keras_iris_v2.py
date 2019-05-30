#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:20:40 2019

@author: shoichi
"""


import numpy as np
import matplotlib.pyplot as plt
#plt.use('Agg')  #CentOS
import pandas as pld
import mglearn

from sklearn import datasets
from sklearn.model_selection import train_test_split
import keras.backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from pandas.plotting import scatter_matrix
import time

def build_multilayer_perceptron():
    """多層パーセプトロンモデルを構築"""
    model = Sequential()
    model.add(Dense(16, input_shape=(4, )))
    model.add(Activation('relu'))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    return model

#precision
def P(y_true, y_pred):
    true_positives = K.sum(K.cast(K.greater(K.clip(y_true * y_pred, 0, 1), 0.20), 'float32'))
    pred_positives = K.sum(K.cast(K.greater(K.clip(y_pred, 0, 1), 0.20), 'float32'))

    precision = true_positives / (pred_positives + K.epsilon())
    return precision

#recall
def R(y_true, y_pred):
    true_positives = K.sum(K.cast(K.greater(K.clip(y_true * y_pred, 0, 1), 0.20), 'float32'))
    poss_positives = K.sum(K.cast(K.greater(K.clip(y_true, 0, 1), 0.20), 'float32'))

    recall = true_positives / (poss_positives + K.epsilon())
    return recall

#f-measure
def F(y_true, y_pred):
    p_val = P(y_true, y_pred)
    r_val = R(y_true, y_pred)
    f_val = 2*p_val*r_val / (p_val + r_val)

    return f_val


def plot_loss():
    plt.figure()
    plt.plot(range(1, nb_epoch+1), result.history["loss"], label="loss")
    #plt.ylim([0,1.5])
    plt.xlabel('Epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.savefig('iris_loss.png')
    
def plot_acc():
    plt.figure()
    plt.plot(range(1, nb_epoch+1), result.history["acc"], label="acc")
    #plt.ylim([0,1.5])
    plt.xlabel('Epochs')
    plt.ylabel('acc')
    plt.legend()
    plt.savefig('iris_acc.png')
    

if __name__ == "__main__":
    # Irisデータをロード
    nb_epoch=50
    iris = datasets.load_iris()
    X = iris.data
    Y_tag = iris.target
    print(Y_tag)
    # データの標準化
    X = preprocessing.scale(X)

    # ラベルをone-hot-encoding形式に変換
    # 0 => [1, 0, 0]
    # 1 => [0, 1, 0]
    # 2 => [0, 0, 1]
    Y = np_utils.to_categorical(Y_tag)

    # 訓練データとテストデータに分割
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y,train_size=0.6)
    print(train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

    # モデル構築
    model = build_multilayer_perceptron()
    model.compile(optimizer='adam',
                  loss='mse',#categorical_crossentropy
                  metrics=['accuracy',P,R,F])

    # モデル訓練
    start = time.time()
    result = model.fit(train_X, train_Y, nb_epoch=nb_epoch,batch_size=1,verbose=1)
    end=time.time() - start
    print('処理時間')
    print(end)
    # モデル評価
    plot_loss()
    plot_acc()
    loss, accuracy,Precision,Recall,F = model.evaluate(test_X,test_Y,verbose=0)
    iris_dataframe = pld.DataFrame(train_X, columns=iris.feature_names)
    grr = scatter_matrix(iris_dataframe, c=train_Y, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
    plt.savefig('iris_plot.png')
    print("Accuracy = {:.2f}".format(accuracy))
    pred = model.predict(X)
    
    pred = np.argmax(pred, axis=1)
    Y = np.argmax(Y,axis=1)
    
    print(confusion_matrix(Y,pred))
