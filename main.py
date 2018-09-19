
import numpy as np
import cv2
import os,math,copy,random
import Walker

'''['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
'''
#image we're walking on
filename = 'reee.jpg'
img = cv2.imread(filename,1)
name, extension = os.path.splitext(filename)

global walkers 
walkers = []

# mouse callback function
def create_walker(event,x,y,flags,param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        walkers.append(Walker.Walker(x,y,[255,0,0],img.shape[0],img.shape[1]))
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            walkers.append(Walker.Walker(x,y,[255,0,0],img.shape[0],img.shape[1]))
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False



#here we create the window 
cv2.namedWindow('new image')
cv2.setMouseCallback('new image',create_walker)

newImg = copy.copy(img)
while(1):
    for walker in walkers:
        walker.draw(newImg,0)
        #walker.completelyRandomWalk()
        walker.walk(img)
        walker.draw(newImg,1)
    
    #cv2.imshow('original image',img)
    cv2.imshow('new image',newImg)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
