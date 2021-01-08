#!/usr/bin/env python
# coding: utf-8

# # OpenCV

# In[1]:


import cv2


# In[2]:


#Reading an image
img = cv2.imread("Skyline-1.jpg", 1)
cv2.imshow("Skyline", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[2]:


#saving an image
img = cv2.imread("Skyline-1.jpg", 0)
cv2.imwrite("newSkyline.jpg", img)


# In[2]:


#resizing an image by reducing width to 200 pixels
img = cv2.imread("Skyline-1.jpg", 1)
print("original size:" +str(img.shape))

r = 200.0/img.shape[1]
dim = (200, int(img.shape[0]*r))

new_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("New image", new_img)
cv2.waitKey(10000)

print("New size:" +str(new_img.shape))


# In[ ]:




