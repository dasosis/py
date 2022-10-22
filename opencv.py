import cv2 as cv
print("Package Imported")

#imread -image read to read images

img= cv.imread("op.png")
print(img)
cv.imshow("Output",img)
cv.waitKey(0)