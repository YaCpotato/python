#etc/usr/bin/env python3
# -*- coding: utf-8 -*-
#参考：Pythonで動かして学ぶ、あたらしい機械学習の教科書

import numpy as np
import matplotlib.pyplot as plt


#線の表示
def show_line(w,x,y):
	xb = np.linspace(x,y,100)
	y = w[0] * xb + w[1]
	plt.plot(xb,y,color=(.5,.5,.5), linewidth=4)

def dmse_line(x,t,w):
	y = w[0] * x + w[1]
	d_w0 = 2 * np.mean((y-t)*x)
	d_w1 = 2 * np.mean(y-t)
	return d_w0,d_w1

def mse_line(x,t,w):
	y = w[0] * x + w[1]
	mse = np.mean((y-t)**2)
	return mse

def fit_line(x,t):
	mx=np.mean(x)
	mt=np.mean(t)
	mtx=np.mean(t*x)
	mxx=np.mean(x*x)
	w0=(mtx-mt*mx)/(mxx-mx**2)
	w1 = mt-w0*mx
	return np.array([w0,w1])




def fit_line_num(x,t):
	w_init = [10.0,165.0]
	alpha = 0.001
	i_max = 100000
	eps = 0.1
	w_i = np.zeros([i_max,2])
	w_i[0, :] = w_init
	
	for i in range(1,i_max):
		dmse = dmse_line(x,t,w_i[i-1])
		w_i[i,0] = w_i[i-1,0] - alpha*dmse[0]
		w_i[i,1] = w_i[i-1,0] - alpha*dmse[1]
		if max(np.absolute(dmse)) < eps:
			break
	w0 = w_i[i,0]
	w1 = w_i[i,1]
	w_i = w_i[:i, :]
	return w0,w1,dmse,w_i



#データを生成する
#np.random.seed(seed=1)
X_min = 4
X_max = 30
X_n = 16
X = 5+25*np.random.rand(X_n)
Prm_c = [170,108,0.2]
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2]*X) + 4 * np.random.rand(X_n)
np.savez('ch5_data.npz',X=X,X_min=X_min,X_max=X_max,X_n=X_n,T=T)

W0, W1, dMSE, W_history = fit_line_num(X,T)
	
plt.figure(figsize=(4,4))
W = fit_line(X,T)
mse = mse_line(X,T,W)
print("w0={0:.3f},w1={1:.3f}".format(W0,W1))
print("SD={0:.3f} cm".format(np.short(mse)))
show_line(W,X_min,X_max)
plt.plot(X,T,marker='o',linestyle='None',markeredgecolor='black',color='cornflowerblue')
plt.xlim(X_min,X_max)
plt.grid(True)
plt.savefig('senkei2.png')

