import cv2

class MarkMyTerritory:

    def __init__(self,size=None,square=None):
        self.src = cv2.imread("input_image.png",cv2.IMREAD_UNCHANGED)
        self.rows = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        if size:
            self.size = int(size)
        else:
            self.size = None
        
        if square:
            self.square = square
            self.alpha = self.square[0]
            self.num = int(self.square[1])
        else:
            self.square = None
            self.alpha = None
            self.num = None

    
    def resizing(self,size=None):
        if size:
            self.size = size
        dsize = (self.size, self.size)
        output = cv2.resize(self.src, dsize)
        return output

    def drawing(self,square=None):
        # coordinates
        if square:
            self.alpha = square[0]
            self.num = int(square[1])
        resized = self.resizing()
        height, width, channel = resized.shape
        single_square = (height/8,width/8)
        if (self.alpha not in self.rows.keys()) or (self.num not in self.rows.values()):
            return "Not a valid square or value"

        # drawing the circle
        bef_radius = width/8/2
        center_coordinates = (round(self.rows[self.alpha]*single_square[0]-bef_radius),round((8-(self.num-1))*single_square[1]-bef_radius))
        if self.rows[self.alpha] % 2 == 0:
            if self.num % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
        else:
            if self.num % 2 == 0:
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)
        radius = round(width/8/2)
        thickness = -1
        image = cv2.circle(resized, center_coordinates, radius, color, thickness)
        cv2.imwrite('cv2-resize-image-width.png',image)
        return "Created"

    def displaying(self):
        draw = self.drawing()
        if draw == "Created":
            img = cv2.imread("cv2-resize-image-width.png",cv2.IMREAD_UNCHANGED)
            cv2.imshow('image',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Not Create any file")
        