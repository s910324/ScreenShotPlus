import pya

class HLine(pya.QFrame):
    def __init__(self, parent = None):
        #super(HLine, self).__init__(parent)
        self.setFrameShape(pya.QFrame.HLine)
        self.setFrameShadow(pya.QFrame.Sunken)