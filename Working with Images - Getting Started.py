#!/usr/bin/env python
# coding: utf-8

# ## Reading an image in OpenCV using Python

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


## Read image from disk
img = cv2.imread("Faza_jkt.jpg", cv2.IMREAD_COLOR)

# creating GUI to display image on screen
cv2.imshow("image", img)

# to hold the window on screen, we use cv2. wait key method
# should be positive int

cv2.waitKey(0)
# for removing / deleting created GUI window from screen
cv2.destroyAllWindows()


# In[3]:


img.shape

# width 1280, 960 and its RGB (3 channels)


# ## Reading Files using Matplotlib

# In[4]:


img = cv2.imread("Faza_jkt.jpg")
# display using matplotlib
plt.imshow(img)

# matplotlib using BGR


# ## Convert BGR to RGB using OpenCV

# In[5]:


img = cv2.imread('Faza_jkt.jpg')

# convert BGR to RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# sdisplay using plt
plt.imshow(RGB_img)


# ## opening in grayscale mode

# In[7]:


path = r'Faza_jkt.jpg'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)


# In[8]:


img.shape


# In[ ]:




