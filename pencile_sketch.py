import cv2

image=cv2.imread("myphoto.jpg")

# converting to grey
grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# help in masking the image
invert=cv2.bitwise_not(grey_img)

# blurring image
blur=cv2.GaussianBlur(invert,(21,21),0)

invertedblur=cv2.bitwise_not(blur)

sketch=cv2.divide(grey_img,invertedblur,scale=256.0)

# converting image to sketch
cv2.imwrite('sketch.png',sketch)
