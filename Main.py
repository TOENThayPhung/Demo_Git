#%%
x=int(input("Nhập số cần tính giai thừa:"))
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (fact(x))

# %%
import cv2
import numpy as np

#1a
I = cv2.imread("K04.jpg")
cv2.imshow('kênh G',I[0;2;1]) #OpenCV: BGR:0->B,1->G,2->R
#1b
#đổi BGR sang gray
Ig = cv2.cvt(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('anh gray',Ig)
#Tính độ cao ảnh
print('độ cao của ảnh',Ig.shape[0])
#độ rộng ảnh
print(Ig.shape[1])

cv2.waitKet()

# %%
