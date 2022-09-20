#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib.image import imread
from numpy import *
import matplotlib.pyplot as set1 


# In[13]:


set1.rcParams['figure.figsize'] = [10, 10]
set1.rcParams.update({'font.size': 15})

naruto = r'C:\Users\xxlab\Task1Folder\DATA\naruto.jpg' ##convert to grayscale image
A = imread(naruto,3)
B = mean(A, -1); 


# In[14]:



## Denoise
Bnoise = B + 200*random.randn(*B.shape).astype('uint8') # Add some noise
Bt = fft.fft2(Bnoise)
Btshift = fft.fftshift(Bt)
F = log(abs(Btshift)+1) # Put FFT on log scale

fig,axs = set1.subplots(2,2)

axs[0,0].imshow(Bnoise,cmap='gray')
axs[0,0].axis('off')

axs[0,1].imshow(F,cmap='gray')
axs[0,1].axis('off')

nx,ny = B.shape
X,Y = meshgrid(arange(-ny/2+1,ny/2+1),arange(-nx/2+1,nx/2+1))
R2 = power(X,2) + power(Y,2)
ind = R2 < 150**2
Btshiftfilt = Btshift * ind
Ffilt = log(abs(Btshiftfilt)+1) # Put FFT on log scale

axs[1,1].imshow(Ffilt,cmap='gray')
axs[1,1].axis('off')

Btfilt = fft.ifftshift(Btshiftfilt)
Bfilt = fft.ifft2(Btfilt).real
axs[1,0].imshow(Bfilt,cmap='gray')
axs[1,0].axis('off')

set1.show()


# In[ ]:




