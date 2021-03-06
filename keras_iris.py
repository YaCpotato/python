#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:12:16 2019

@author: shoichi
"""

import numpy as np
import matplotlib as plt
import pandas as pld
import mglearn

from sklearn import datasets
from sklearn.model_selection import train_test_split

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


if __name__ == "__main__":
    # Irisデータをロード
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    
    
    # データの標準化
    X = preprocessing.scale(X)

    # ラベルをone-hot-encoding形式に変換
    # 0 => [1, 0, 0]
    # 1 => [0, 1, 0]
    # 2 => [0, 0, 1]
    Y = np_utils.to_categorical(Y)

    # 訓練データとテストデータに分割
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.8)
    print(train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

    # モデル構築
    model = build_multilayer_perceptron()
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # モデル訓練
    start = time.time()
    model.fit(train_X, train_Y, nb_epoch=100, batch_size=1, verbose=1)
    end=time.time() - start
    print('処理時間')
    print(end)
    # モデル評価
    loss, accuracy = model.evaluate(test_X, test_Y, verbose=0)
    print("Accuracy = {:.2f}".format(accuracy))
    
    iris_dataframe = pld.DataFrame(train_X, columns=iris.feature_names)
    grr = scatter_matrix(iris_dataframe, c=train_Y, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
    plt.show()
    