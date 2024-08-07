import pya

class ImageConfigWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(ImageConfigWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.imgWSpn = pya.QSpinBox()
        self.imgHSpn = pya.QSpinBox()
        self.lyWSpn  = pya.QSpinBox()
        self.ovspSpn = pya.QSpinBox()
        self.layout  = pya.QGridLayout()
        
        self.layout.addWidget(pya.QLabel("Image Width:"),  0, 0, 1, 1)              
        self.layout.addWidget(pya.QLabel("Image Height:"), 1, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Layer Width:"),  2, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Oversampling:"), 3, 0, 1, 1)
        
        self.layout.addWidget(self.imgWSpn,  0, 1, 1, 1)
        self.layout.addWidget(self.imgHSpn,  1, 1, 1, 1)
        self.layout.addWidget(self.lyWSpn,   2, 1, 1, 1)
        self.layout.addWidget(self.ovspSpn,  3, 1, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setColumnMinimumWidth(0, 70)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)
        
        for spn in [self.imgWSpn, self.imgHSpn, self.lyWSpn, self.ovspSpn]:
            spn.setAlignment(pya.Qt.AlignmentFlag.AlignCenter)
            
        self.imgWSpn.setRange(1, 8E3)
        self.imgHSpn.setRange(1, 8E3)
        self.lyWSpn.setRange(0, 500)
        self.ovspSpn.setRange(0, 3)
        
            
if __name__ == "__main__" :
    w = ImageConfigWidget()
    w.show()