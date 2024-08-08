import pya

class SetViewWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(SetViewWidget, self).__init__()
        self.initUI()
        #self.initSignal()
        
    def initUI(self):
        self.vp1xDblSpn = pya.QDoubleSpinBox()
        self.vp1yDblSpn = pya.QDoubleSpinBox()
        self.vp2xDblSpn = pya.QDoubleSpinBox()
        self.vp2yDblSpn = pya.QDoubleSpinBox()
        self.getViewPB  = pya.QPushButton("Get view box")
        self.setViewPB  = pya.QPushButton("Set view")
        self.setFitPB   = pya.QPushButton("Zoom fit")
        self.bkViewPB   = pya.QPushButton("Bookmark view")
        self.layout     = pya.QGridLayout()
        self.bpLayout   = pya.QGridLayout()
        
        self.layout.addWidget(pya.QLabel("View\n(x1, y1)"), 0, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("(x2, y2)"),       1, 0, 1, 1)
        
        self.layout.addWidget(self.vp1xDblSpn,  0, 1, 1, 1)
        self.layout.addWidget(self.vp1yDblSpn,  0, 2, 1, 1)
        self.layout.addWidget(self.vp2xDblSpn,  1, 1, 1, 1)
        self.layout.addWidget(self.vp2yDblSpn,  1, 2, 1, 1)
        self.layout.addLayout(self.bpLayout,    2, 0, 1, 3)
        self.bpLayout.addWidget(self.getViewPB, 0, 0, 1, 1) 
        self.bpLayout.addWidget(self.setViewPB, 0, 1, 1, 1) 
        self.bpLayout.addWidget(self.setFitPB,  0, 2, 1, 1) 
            
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setColumnMinimumWidth(0, 70)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)
        self.bpLayout.setContentsMargins(0, 0, 0, 0)
        self.bpLayout.setColumnMinimumWidth(0, 70)
        self.bpLayout.setColumnMinimumWidth(1, 70)
        self.bpLayout.setColumnMinimumWidth(2, 70)
        self.setLayout(self.layout)
        
        for spn in [self.vp1xDblSpn, self.vp1yDblSpn, self.vp2xDblSpn, self.vp2yDblSpn]:
            spn.setRange(-1e5, 1e5)
            spn.setAlignment(pya.Qt.AlignmentFlag.AlignCenter)
 
                
if __name__ == "__main__" :
    w = SetViewWidget()
    w.show()