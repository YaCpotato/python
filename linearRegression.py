import numpy as np
import matplotlib.pyplot as plt

# データを生成
n=10
x_data = np.random.rand(n).astype(np.float32)
y_data = x_data*4 + 5 
plt.figure()
plt.scatter(x_data,y_data)
plt.show()
# 　ノイズを加える
y_data = y_data + 0.4 * np.random.randn(n)
# ノイズ付きデータを描画
plt.figure()
plt.scatter(x_data,y_data)
plt.show()

import tensorflow as tf

W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
loss_array = []
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

def predict(x):
    return W_val * x + b_val


for step in range(101):
    loss_val = sess.run(loss)
    loss_array.append(loss_val)
    W_val = sess.run(W)
    b_val = sess.run(b)
    print('Step: %03d,   Loss: %5.4f,   W: %f,   b: %f' % (step,loss_val,W_val,b_val))
    sess.run(train)
    if step %10 == 0:
      fig = plt.figure()
      subplot = fig.add_subplot(1,1,1)

      plt.scatter(x_data,y_data)
      linex = np.linspace(0,1,2)
      liney = predict(linex)
      subplot.plot(linex,liney)
      plt.show()

fig = plt.figure()
subplot = fig.add_subplot(1,1,1)

plt.scatter(x_data,y_data)
linex = np.linspace(0,1,2)
liney = predict(linex)
subplot.plot(linex,liney)
plt.show()


plt.plot(loss_array)
plt.show()
