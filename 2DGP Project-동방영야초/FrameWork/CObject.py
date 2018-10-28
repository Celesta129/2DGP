name = "class_Object"



class cObject:
    def __init__(self, w = None, h = None):
        self.x,self.y = 0,0
        self.velocity = [0,0]

        self.frame = 0
        self.frame_offset = 0
        self.image_width = 0
        self.image_height = 0
        self.width = None
        self.height = None
        self.image = None
        self.image_left = 0
        self.image_bottom = 0
        if(w == None):
            self.Width = self.image_width
        if(h == None):
            self.Height = self.image_height

    def draw(self):
        if self.image != None:
            self.image.clip_draw(self.image_left + self.frame_offset* self.frame, self.image_bottom,
                                 self.image_width ,self.image_height,
                                 self.x, self.y,
                                 self.width,self.height)
        pass

    def update(self):
        pass
