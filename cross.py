import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import seaborn as sns
import numpy.random as rd

m = 10
s = 3

min_x = m-4*s
max_x = m+4*s

x = np.linspace(min_x, max_x, 201)
y = (1/np.sqrt(2*np.pi*s**2))*np.exp(-0.5*(x-m)**2/s**2)

plt.figure(figsize=(8,5))
plt.xlim(min_x, max_x)
plt.ylim(0,1.1*np.max(y))
plt.plot(x,y)
plt.show()



plt.figure(figsize=(8,2))
rd.seed(7)
data = rd.normal(10, 3, 10, )
plt.scatter(data, np.zeros_like(data), c="r", s=50)

max_m = 0
cor_m = 0
cor_s = 0
l_list =list(range(1))
l_list2 = [[0 for i in range(10)] for j in range(10)]
for m in range(1,10):
    for s in range(1,10):
        min_x = m-4*s
        max_x = m+4*s
        def norm_dens(val):
            return (1/np.sqrt(2*np.pi*s**2))*np.exp(-0.5*(val-m)**2/s**2)
        
        x = np.linspace(min_x, max_x, 201)
        y = norm_dens(x)
        
        L = np.prod([norm_dens(x_i) for x_i in data])
        l = np.log(L)
        
        plt.figure(figsize=(8,5))
        plt.xlim(min_x, 16)
        plt.ylim(-0.01,np.max(y)*1.1)
        
        # 正規分布の密度関数の描画
        plt.plot(x,y)
        
        # データ点の描画
        plt.scatter(data, np.zeros_like(data), c="r", s=50)
        for d in data:
            plt.plot([d, d], [0, norm_dens(d)], "k--", lw=1)
        
        plt.title("Likelihood:{0:.5f}, log Likelihood:{1:.5f}".format(L, l))
        print(m,s)
        l_list.append(l)
        l_list2[m][s]=l
        plt.show()
    
print(l_list)
plt.figure()
x=np.arange(0,82,1)
plt.plot(x,l_list)

l_list_max = 0
for i in range(10):
    for j in range(10):
        if l_list_max < l_list2[i][j]:
            l_list_max = l_list2[i][j]
            print(l_list_max)




