import cv2

#Make sure you import cv2
#conda install cv2 if you have anaconda installed
#pip install cv2 if you have pip installed

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# test.jpg is the image you want to test
img_path = input('Enter the path to the image you want to test: ')

img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite('face_detected.jpg', img)


