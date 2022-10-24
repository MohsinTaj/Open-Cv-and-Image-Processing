import cv2
image = cv2.imread('C:/Users/92334/Downloads/OIP.JFIF')
output = image.copy()
cv2.rectangle(output, (32, 60), (420, 1600), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)