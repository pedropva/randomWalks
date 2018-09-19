import random
class Walker: 
    
    def __init__(self,x,y,paintColor,pixelColor,limitX,limitY):#x,y and color
        self.x = x 
        self.y = y 
        self.paintColor = paintColor
        self.pixelColor = pixelColor
        self.limitX = limitX
        self.limitY = limitY

    # Draws self shape to a given context
    def draw(self,img,old):
        if(old == 1):
            img[self.y,self.x][0] = self.paintColor[0]
            img[self.y,self.x][1] = self.paintColor[1]
            img[self.y,self.x][2] = self.paintColor[2]
            
        else:
            img[self.y,self.x][0] = 255 - self.paintColor[0] 
            img[self.y,self.x][1] = 255 - self.paintColor[1]
            img[self.y,self.x][2] = 255 - self.paintColor[2]

    def walk(self,img):
        similaritys =[0] * 8
        #run on all neightboors of the pixel and get their similarity
        for x in range(0,8): 
            similaritys[x] = self.similarity(self.getNeighboor(img,x))
        
        print(similaritys)
        probabilitys = ['0'] * (1+similaritys[0]) + ['1'] * (1+similaritys[1]) + ['2'] * (1+similaritys[2]) + ['3'] * (1+similaritys[3]) + ['4'] * (1+similaritys[4]) + ['5'] * (1+similaritys[5]) + ['6'] * (1+similaritys[6]) + ['7'] * (1+similaritys[7])
        
        choice = random.choice(probabilitys)
        x,y = self.getNeighboorPos(int(choice))
        self.setRelativePosition(x,y)

    def completelyRandomWalk(self):
        self.randomize()

    def randomize (self):

        self.x += random.randint(-1,1)
        self.y += random.randint(-1,1)
        return self

    def similarity(self,pixel):
        #value = 255//(1+abs(self.pixelColor-pixel))
        value = 1000//(1+(abs((pixel[0] - self.pixelColor[0])) + abs((pixel[1] - self.pixelColor[1])) + abs((pixel[2] - self.pixelColor[2]))))
        return value

    def setRelativePosition(self,x,y):
        if(self.x + x > 0 and self.x + x < self.limitX):            
            self.x += x
        if(self.y + y > 0 and self.y + y < self.limitY):            
            self.y += y
        return self

    def setPosition(self,x,y):
        if(x > 0 and x < self.limitX):            
            self.x = x
        if(y > 0 and y < self.limitY):            
            self.y = y
        return self

    def getNeighboor(self,img,number):
        neightboors = []
        
        if self.x + 1 < self.limitX:    
            neightboors.append(img[self.y,self.x+1])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])
        if self.x - 1 > 0:
            neightboors.append(img[self.y,self.x-1])
        else:
            neightboors.append([255-self.pixelColor,255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y + 1 < self.limitY:    
            neightboors.append(img[self.y+1,self.x])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y - 1 > 0:    
            neightboors.append(img[self.y-1,self.x])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y + 1 < self.limitY and self.x + 1 < self.limitX:
            neightboors.append(img[self.y+1,self.x+1])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y - 1 > 0 and self.x - 1 > 0:
            neightboors.append(img[self.y-1,self.x-1])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y + 1 < self.limitY and self.x - 1 > 0:
            neightboors.append(img[self.y+1,self.x-1])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        if self.y - 1 > 0 and self.x + 1 < self.limitX:
            neightboors.append(img[self.y-1,self.x+1])
        else:
            neightboors.append([255-self.pixelColor[0],255-self.pixelColor[1],255-self.pixelColor[2]])

        return neightboors[number]

    def getNeighboorPos(self,number):
        if number == 0:
            return 0,1
        if number == 1:
            return 0,-1
        if number == 2:
            return 1,0
        if number == 3:
            return -1,0
        if number == 4:
            return 1,1
        if number == 5:
            return -1,-1
        if number == 6:
            return 1,-1
        if number == 7:
            return -1,1
        
        