import os
class Image():
    def __init__(self)->None:
        FilePath=None
        if os.path.exists(os.getcwd()+"\\image.jpg"):
            FilePath=os.getcwd()+"\\image.jpg"
        elif os.path.exists(os.getcwd()+"\\image.png"):
            FilePath=os.getcwd()+"\\image.png"
        
        self.imgPath=FilePath

    def exist(self)->bool:
        if self.imgPath==None:
            return False
        else:
            return True

