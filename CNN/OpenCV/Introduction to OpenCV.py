#!/usr/bin/env python
# coding: utf-8

# # Import opencv

# In[1]:


import cv2
import matplotlib.pyplot as plt


# ## Reading an Image

# In[2]:


image = cv2.imread('faza.jpg')
image


# ## Extracting the height and width of an image

# In[3]:


h, w = image.shape[:2]
print(f"Height = {h} and Width = {w}")


# # Extracting RGB Values from Image

# In[4]:


(B,G,R) = image[100,100]


# ## Displaying the pixel values

# In[5]:


print(f"R = {R}, G = {G}, B = {B}")


# ## pass channel to extract the value for specific channel

# In[6]:


B = image[100,100,0]
print("B = {}".format(B))


# # Extracting the Region of Interest (ROI)

# In[7]:


roi = image[100:500, 200:700]
roi


# # Resizing Image

# In[8]:


# resize func take 2 dimension, image and dimension
resize = cv2.resize(image, (800, 800))


# In[9]:


cv2.imshow("Resized Image", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


plt.imshow(resize)
plt.show()


# ## Resize but maintaning the ratio

# In[12]:


ratio = 800 / w

# create a tuple containing w and h
dim = (800, int(h * ratio))

# resize the image
resize_aspect = cv2.resize(image, dim)
plt.imshow(resize_aspect)
plt.show()


# # Rotating the Image

# In[14]:


# calculating the center of image
center = (w // 2, h // 2)

# generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)

# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w,h))
plt.imshow(rotated)
plt.show()

"""2 main function
getRotationMatrix2D, warpAffine
getRotationMatrix2D takes 3 arguments:
1. center (center coordinates of image)
2. Angle (the angle in degrees by which the image should be rotated)
3. scale (the scalling factor)

warpAffine calculated new x, y of the image and transform it"""


# ## Displaying text

# In[15]:


# copying the original image
output = image.copy()

# adding the text using putText func()
text = cv2.putText(output, 'OpenCV Demo', (500,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,0), 2)


# In[16]:


plt.imshow(output)
plt.show()


# In[ ]:




