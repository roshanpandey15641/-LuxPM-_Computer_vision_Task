#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
# read images
img = cv2.imread("images.jpg")
cv2.imshow("original_image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


#Transform the image in the +x direction by 25%, and create an image
img = cv2.imread("images.jpg")
cv2.imshow("original_image",img)
cv2.waitKey(0)
img_scaled = cv2.resize(img,None,fx=0.75,fy=0.75)# x-axis and y-axis
cv2.imshow('scaling-linear interplotation',img_scaled)
cv2.waitKey()
cv2.destroyAllWindows()


# In[3]:


#Rotate the image in Z by 90 degree
img=cv2.imread("images.jpg")
height , width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,.5)
rotated_image = cv2.warpAffine(img,rotation_matrix,(width,height))

cv2.imshow('Rotated image',rotated_image)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


#Rotate the image in Z by -90 degree
img=cv2.imread("images.jpg")
height , width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),-90,.5)
rotated_image = cv2.warpAffine(img,rotation_matrix,(width,height))

cv2.imshow('Rotated image',rotated_image)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


#From the center of the image, in all directions, increase the RGB values of the pixels in a manner that, each pixel from the center, the percentage drops by 1%. i.e. the center pixel's RGB will increase by 50%, and the next pixels in x and y directions will be 49%. This goes on and on until the increase becomes 0 %.

img = cv2.imread("images.jpg")
cv2.imshow("original_image",img)
cv2.waitKey(0)

B,G,R = cv2.split(img)
zeros = np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros,zeros,R]))
cv2.imshow("Green", cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:




