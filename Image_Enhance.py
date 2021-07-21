import cv2


#READ THE IMAGE
img=cv2.imread('1.jpg')
#APPLY CLAHE----> CONTRAST LIMITED ADAPTIVE HISTOGRAM EQUALIZATION
clahe=cv2.createCLAHE()
#CONVERT TO GRAYSCALE IMAGE
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#APPLY ENHANCEMENT
enh_img=clahe.apply(gray_img)
#SAVE IMG
cv2.imwrite('2.jpg',enh_img)

print("Done")