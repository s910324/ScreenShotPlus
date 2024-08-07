import pya

class DisplayConfigWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(DisplayConfigWidget, self).__init__()
        self.saveFullPath = None
        self.initUI()
        #self.initSignal()
        
    def initUI(self):
        self.showLypnCB  = pya.QCheckBox("Show layer panel")                                   
        self.showLnumCB  = pya.QCheckBox("Show layer number")
        self.showLnameCB = pya.QCheckBox("Show layer name")
        self.showLsourCB = pya.QCheckBox("Show layer source")
        self.showLvisCB  = pya.QCheckBox("Show only visible")
        self.dirCB       = pya.QComboBox()  
        self.gridCB      = pya.QComboBox()                                   
        self.scaleCB     = pya.QComboBox()
        self.axisCB      = pya.QComboBox()
        self.layout      = pya.QGridLayout()
        
        self.layout.addWidget(pya.QLabel("Layer setting:"),  0, 0, 1, 1)            
        self.layout.addWidget(pya.QLabel("Orentation:"),     5, 0, 1, 1)      
        self.layout.addWidget(pya.QLabel("Grid:"),           6, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Scale bar:"),      7, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Axis :"),          8, 0, 1, 1)
        
        self.layout.addWidget(self.showLypnCB,  0, 1, 1, 1)
        self.layout.addWidget(self.showLnumCB,  1, 1, 1, 1)
        self.layout.addWidget(self.showLnameCB, 2, 1, 1, 1)
        self.layout.addWidget(self.showLsourCB, 3, 1, 1, 1)
        self.layout.addWidget(self.showLvisCB,  4, 1, 1, 1)
        self.layout.addWidget(self.dirCB,       5, 1, 1, 1)
        self.layout.addWidget(self.gridCB,      6, 1, 1, 1)
        self.layout.addWidget(self.scaleCB,     7, 1, 1, 1)
        self.layout.addWidget(self.axisCB,      8, 1, 1, 1)
        
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setColumnMinimumWidth(0, 70)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)
        
        lineTheme = {
            "Invisible"                          : "invisible", 
            "Dots"                               : "dots", 
            "Dotted lines"                       : "dotted-lines",
            "Light dotted lines"                 : "light-dotted-lines", 
            "Dotted lines, 10 dots per dividion" : "tenths-dotted-lines", 
            "Crosses"                            : "crosses", 
            "Lines"                              : "lines", 
            "Lines with ticks"                   : "tenth-marked-lines"
        }
        scaleTheme = {
            "Show" : "true",
            "Hide" : "false"
        }
        
        dirTheme = {
            "Left side"   : "L",
            "Bottom side" : "B",
        }
        for t in lineTheme:
            self.gridCB.addItem(t, lineTheme[t])
            self.axisCB.addItem(t, lineTheme[t])
            
        for t in scaleTheme:
            self.scaleCB.addItem(t, scaleTheme[t])
        
        for t in dirTheme:
            self.dirCB.addItem(t, dirTheme[t])
        
if __name__ == "__main__" :
    w = DisplayConfigWidget()
    w.show()