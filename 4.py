import cv2
image = cv2.imread('C:/Users/92334/Downloads/OIP.JFIF')
output = image.copy()
cv2.circle(output, (390, 120), 40, (0, 255, 0), 3)
cv2.imshow("Circle", output)
cv2.waitKey(0)
