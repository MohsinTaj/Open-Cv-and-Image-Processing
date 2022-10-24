# Python program to explain cv2.cvtColor() method
# importing cv2
import cv2
# path
path = "C:/Users/92334/Downloads/OIP.JFIF"
# Reading an image in default mode
src = cv2.imread(path)
# Window name in which image is displayed
window_name = 'Image'
# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2GRAY color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
image = cv2.resize(image,(480,640))
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
