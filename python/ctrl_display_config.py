import pya

class DisplayConfigWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(DisplayConfigWidget, self).__init__()
        self.saveFullPath = None
        self.initUI()
        #self.initSignal()
        
    def initUI(self):
        self.lyAdjCB      = pya.QComboBox()  
        self.gridCB       = pya.QComboBox()                                   
        self.scaleCB      = pya.QComboBox()
        self.axisCB       = pya.QComboBox()
        
        self.showLnumCB   = pya.QCheckBox("Show layer number")
        self.showLnameCB  = pya.QCheckBox("Show layer name")
        self.showLsourCB  = pya.QCheckBox("Show layer source")
        
        self.hideHiddenCB = pya.QCheckBox("Hide hidden layers")
        self.hideEmptyCB  = pya.QCheckBox("Hide empty layers")
        self.hideNIVCB    = pya.QCheckBox("Hide layers not in view")
        self.hideTxtCB    = pya.QCheckBox("Hide text")
        self.layout       = pya.QGridLayout()
        
        self.layout.addWidget(pya.QLabel("Layer window:"),   0, 0, 1, 1)      
        self.layout.addWidget(pya.QLabel("Grid style:"),     1, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Scale bar:"),      2, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Axis style:"),     3, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("Layer setting:"),  5, 0, 1, 1) 
        
        self.layout.addWidget(self.lyAdjCB,       0, 1, 1, 1)
        self.layout.addWidget(self.gridCB,        1, 1, 1, 1)
        self.layout.addWidget(self.scaleCB,       2, 1, 1, 1)
        self.layout.addWidget(self.axisCB,        3, 1, 1, 1)
        self.layout.setRowMinimumHeight(          4, 15     )
        self.layout.addWidget(self.showLnumCB,    5, 1, 1, 1)
        self.layout.addWidget(self.showLnameCB,   6, 1, 1, 1)
        self.layout.addWidget(self.showLsourCB,   7, 1, 1, 1)
        self.layout.setRowMinimumHeight(          8, 15     )
        self.layout.addWidget(self.hideHiddenCB,  9, 1, 1, 1)
        self.layout.addWidget(self.hideEmptyCB,  10, 1, 1, 1)
        self.layout.addWidget(self.hideNIVCB,    11, 1, 1, 1)
        self.layout.addWidget(self.hideTxtCB,    12, 1, 1, 1)        
        self.layout.setContentsMargins(           0, 0, 0, 0)
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
        scaleConfg = {
            "Show" : "true",
            "Hide" : "false"
        }
        
        dirConfg = {
            "Left side"   : "L",
            "Bottom side" : "B",
            "Right side"  : "R",
            "Top side"    : "T",
            "Hide"        : "H",
        }
        

        for t in lineTheme:
            self.gridCB.addItem(t, lineTheme[t])
            self.axisCB.addItem(t, lineTheme[t])
            
        for t in scaleConfg:
            self.scaleCB.addItem(t, scaleConfg[t])
        
        for t in dirConfg:
            self.lyAdjCB.addItem(t, dirConfg[t])
            

            
if __name__ == "__main__" :
    w = DisplayConfigWidget()
    w.show()