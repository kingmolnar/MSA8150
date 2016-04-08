
# coding: utf-8

# In[69]:

import numpy


# In[70]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt


# In[71]:

def plot_matrix(M):
    plt.imshow(M, interpolation="none", cmap="Greys_r") ## "Greys" or "Greys_r"
    plt.colorbar()


# In[51]:

get_ipython().magic('pinfo plt.imshow')


# In[72]:

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if e < 0.001:
            break
    return P, Q.T


# In[ ]:

R = [
         [5,3,0,1],
         [4,0,0,1],
         [1,1,0,5],
         [1,0,0,4],
         [0,1,5,4],
        ]

R = numpy.array(R)


# In[57]:

plot_matrix(R)


# In[25]:

N = len(R)
M = len(R[0])
K = 3

P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)


# In[41]:

plot_matrix(P)


# In[26]:

P


# In[42]:

plot_matrix(Q)


# In[27]:

Q


# In[ ]:




# In[ ]:




# In[46]:

nP, nQ = matrix_factorization(R, P, Q, K, steps=50000)


# In[29]:

nP


# In[30]:

nQ


# In[47]:

nR = numpy.dot(nP, nQ.T)


# In[48]:

plt.subplot(1,2,1)
plot_matrix(R)
plt.subplot(1,2,2)
plot_matrix(nR)


# In[32]:

sum(sum(abs(R - nR)))


# In[78]:

N = 20
M = 20
K = [3, 7, 12]

R = numpy.random.randint(0,5,(N,M))

plt.subplot(1,len(K)+1,1)
plot_matrix(R)


for k in range(len(K)):
    
    P = numpy.random.rand(N,K[k])
    Q = numpy.random.rand(M,K[k])


    nP, nQ = matrix_factorization(R, P, Q, K[k], steps=5000)

    nR = numpy.dot(nP, nQ.T)

    plt.subplot(1,len(K)+1, k+2)
    plot_matrix(nR)
    


# In[93]:

R = [
        [5, 0, 0, 3, 1, 0, 0], #1
        [5, 0, 0, 3, 1, 0, 0], #2
        [0, 0, 5, 0, 1, 0, 6], #3
        [0, 0, 5, 0, 1, 0, 6], #4
        [0, 0, 5, 0, 1, 0, 6], #5
        [0, 0, 5, 0, 1, 0, 6], #6
        [0, 5, 0, 5, 0, 0, 0], #7
        [5, 0, 0, 3, 1, 0, 0], #8
        [0, 5, 0, 5, 0, 0, 0], #9
        [0, 5, 0, 5, 0, 0, 0]  #10
    ]

K = 3
N = len(R)
M = len(R[0])
P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)
nP, nQ = matrix_factorization(R, P, Q, K, steps=5000)


# In[94]:

plot_matrix(numpy.dot(P, P.T))


# In[97]:

P.dot(P.T).diagonal()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



