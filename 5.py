import cv2
image = cv2.imread('C:/Users/92334/Downloads/Screenshot 2022-10-23 001711.png')
output = image.copy()
cv2.putText(output, "OpenCV with 3 Idiots!!!", (10, 25),
 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
