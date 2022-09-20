#!/usr/bin/env python
# coding: utf-8

# In[6]:


from matplotlib.image import imread
from numpy import *
import matplotlib.pyplot as set1 


# In[7]:


set1.rcParams['figure.figsize'] = [16, 16]
set1.rcParams.update({'font.size': 15})

naruto = r'C:\Users\xxlab\Task1Folder\DATA\naruto.jpg' ##convert to grayscale image
A = imread(naruto,3)
B = mean(A, -1); 

fig,axs = set1.subplots(1,3)

img = axs[0].imshow(B)
img.set_cmap('gray') ## Plot image
axs[0].axis('off')

Cshift = zeros_like(B,dtype='complex_') ## Compute row-wise 
C = zeros_like(B,dtype='complex_')

for j in range(B.shape[0]):
    Cshift[j,:] = fft.fftshift(fft.fft(B[j,:]))
    C[j,:] = fft.fft(B[j,:])
    
img = axs[1].imshow(log(abs(Cshift)))
img.set_cmap('gray')
axs[1].axis('off')

D = zeros_like(C)
for j in range(C.shape[1]):
    D[:,j] = fft.fft(C[:,j]) ## Compute column-wise FFT

img = axs[2].imshow(fft.fftshift(log(abs(D))))
img.set_cmap('gray')
axs[2].axis('off')

set1.show()
D = fft.fft2(B) ## Much more efficient to use fft2


# In[ ]:




