import cv2
image = cv2.imread("C:/Users/92334/Downloads/OIP.JFIF") 
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("Image", image)
cv2.waitKey(0)
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))
