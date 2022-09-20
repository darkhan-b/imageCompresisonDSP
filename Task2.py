#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib.image import imread
from numpy import *
import matplotlib.pyplot as set1 


# In[19]:


set1.rcParams['figure.figsize'] = [3, 3]
set1.rcParams.update({'font.size': 12})

naruto = r'C:\Users\xxlab\Task1Folder\DATA\naruto.jpg' ##convert to grayscale image
A = imread(naruto,3)
B = mean(A, -1); 


# In[21]:


Bt = fft.fft2(B)
Btsort = sort(abs(Bt.reshape(-1))) ## sort by magnitude


for keep in (.1, .05, .01, .002): ## Zero out all small coefficients and inverse transform
    thresh = Btsort[int(floor((1-keep)*len(Btsort)))]
    ind = abs(Bt)>thresh          ## Find small indices
    Atlow = Bt * ind                 ## Threshold small indices
    Alow = fft.ifft2(Atlow).real  ## Compressed image
    set1.figure()
    set1.imshow(Alow,cmap='gray')
    set1.axis('off')
    set1.title('Image FFT with % = ' + str(keep))


# In[ ]:




