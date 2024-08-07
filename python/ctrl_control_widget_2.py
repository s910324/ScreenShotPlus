class HLine(pya.QFrame):
    def __init__(self, parent = None):
        super(HLine, self).__init__(None)
        self.setFrameShape(pya.QFrame.HLine)
        self.setFrameShadow(pya.QFrame.Sunken)

class ControlWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(ControlWidget, self).__init__()
        self.waitClose = False
        self.parent    = parent
        self.initUI()
        self.setPanelValue()
        self.initSignal()
          
    def initUI(self):
        self.layout                = pya.QGridLayout()
        self.onTopCB               = pya.QCheckBox("Always on top")
        self.pathLabel             = pya.QLabel("Path:")
        self.imgWidthLabel         = pya.QLabel("Image width:")
        self.imgHeightLabel        = pya.QLabel("Image height:")
        self.lyWidthLabel          = pya.QLabel("Layer panel width:")
        self.lyAdjLabel            = pya.QLabel("Layer view:")
        self.viewLabelx1y1         = pya.QLabel("X1,Y1:")
        self.viewLabelx2y2         = pya.QLabel("X2,Y2:")
        self.viewLabelVR           = pya.QLabel("Set View Rect:")
         
        self.gridLabel             = pya.QLabel("Grid:")
        self.scaleLabel            = pya.QLabel("Scale bar:")
        self.axisLabel             = pya.QLabel("Axis:")   
          
        self.gridHide              = pya.QCheckBox("Hide grids")                                   
        self.scaleHide             = pya.QCheckBox("Hide Ruler")
        
        self.showLypnCB            = pya.QCheckBox("Show layer panel")                                   
        self.showLndtCB            = pya.QCheckBox("Show layer no")
        self.showLnameCB           = pya.QCheckBox("Show layer name")
        self.showLsourceCB         = pya.QCheckBox("Show layer source")
        self.showLvisibleCB        = pya.QCheckBox("Show only visible")
        
        
            
        self.xDblSpin1             = pya.QDoubleSpinBox()
        self.xDblSpin2             = pya.QDoubleSpinBox()
        self.yDblSpin1             = pya.QDoubleSpinBox()
        self.yDblSpin2             = pya.QDoubleSpinBox()

        self.imgWidthSpin          = pya.QSpinBox()
        self.imgHeightSpin         = pya.QSpinBox()
        self.lyWidthSpin           = pya.QSpinBox()
        
        self.pathEdit              = pya.QLineEdit()
        self.getViewPB             = pya.QPushButton("Get current view box")
        self.setViewPB             = pya.QPushButton("Set view")
        self.setFitPB              = pya.QPushButton("Zoom fit")
        self.getScreenPB           = pya.QPushButton("Get image")
        self.saveScreenPB          = pya.QPushButton("Save image")
        self.cancelPB              = pya.QPushButton("Cancel")
        
        
        self.imgWidthSpin.setMaximum(1e4)
        self.imgHeightSpin.setMaximum(1e4)
        self.lyWidthSpin.setMaximum(500)

        self.xDblSpin1.setRange(-1e5, 1e5)
        self.xDblSpin2.setRange(-1e5, 1e5)
        self.yDblSpin1.setRange(-1e5, 1e5)
        self.yDblSpin2.setRange(-1e5, 1e5)
        

        col = 2
        g   = 0
        
        self.layout.addWidget(self.imgWidthLabel,  g + 0, 0, 1, 1  )
        self.layout.addWidget(self.imgWidthSpin,   g + 0, 1, 1, col)
        self.layout.addWidget(self.imgHeightLabel, g + 1, 0, 1, 1  )
        self.layout.addWidget(self.imgHeightSpin,  g + 1, 1, 1, col)
        self.layout.addWidget(self.lyWidthLabel,   g + 2, 0, 1, 1)
        self.layout.addWidget(self.lyWidthSpin,    g + 2, 1, 1, col)
        self.layout.addWidget(self.onTopCB,        g + 3, 1, 1, col)
        
        g = g + 3
        
        self.layout.setRowStretch(g, 1)
        g = g + 1
        
        self.layout.addWidget(HLine(self),         g + 0, 0, 1, col + 1)
        g = g + 1
        self.layout.addWidget(self.lyAdjLabel,     g + 0, 0, 1, 1  )
        self.layout.addWidget(self.showLypnCB,     g + 0, 1, 1, col)
        self.layout.addWidget(self.showLndtCB,     g + 1, 1, 1, col)
        self.layout.addWidget(self.showLnameCB,    g + 2, 1, 1, col)
        self.layout.addWidget(self.showLsourceCB,  g + 3, 1, 1, col)
        self.layout.addWidget(self.showLvisibleCB, g + 4, 1, 1, col)
        g = g + 4
        
        self.layout.setRowStretch(g, 1)
        g = g + 1
        
        self.layout.addWidget(HLine(self),         g + 0, 0, 1, col + 1)
        g = g + 1
        
        self.layout.addWidget(self.gridLabel,      g + 0, 0, 1, col)
        self.layout.addWidget(self.gridHide,       g + 0, 1, 1, col)
        self.layout.addWidget(self.scaleLabel,     g + 1, 0, 1, col)
        self.layout.addWidget(self.scaleHide,      g + 1, 1, 1, col)
        g = g + 3
        
        self.layout.setRowStretch(g, 1)
        g = g + 1
        
        self.layout.addWidget(HLine(self),         g + 0, 0, 1, col + 1)
        g = g + 1
        
        self.layout.addWidget(self.viewLabelx1y1,  g + 0, 0, 1, 1  ) 
        self.layout.addWidget(self.xDblSpin1,      g + 0, 1, 1, 1  )
        self.layout.addWidget(self.yDblSpin1,      g + 0, 2, 1, 1  )
        
        self.layout.addWidget(self.viewLabelx2y2,  g + 1, 0, 1, 1  ) 
        self.layout.addWidget(self.xDblSpin2,      g + 1, 1, 1, 1  )
        self.layout.addWidget(self.yDblSpin2,      g + 1, 2, 1, 1  )
        self.layout.addWidget(self.viewLabelVR,    g + 2, 0, 1, 1  ) 
        self.layout.addWidget(self.getViewPB,      g + 2, 1, 1, col)
        self.layout.addWidget(self.setViewPB,      g + 3, 1, 1, col)
        self.layout.addWidget(self.setFitPB,       g + 4, 1, 1, col)
        g = g + 5

        
        self.layout.setRowStretch(g, 1)
        g = g + 1
        
        self.layout.addWidget(HLine(self),         g + 0, 0, 1, col + 1)
        g = g + 1
        
        self.layout.addWidget(self.pathLabel,      g + 0, 0, 1, 1  )
        self.layout.addWidget(self.pathEdit,       g + 0, 1, 1, col)
        g = g + 2
        
        self.layout.addWidget(self.getScreenPB,    g + 0, 1, 1, col)
        self.layout.addWidget(self.saveScreenPB,   g + 1, 1, 1, col)
        self.layout.addWidget(self.cancelPB,       g + 2, 1, 1, col)
        self.layout.setRowStretch(7, 1)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)
        self.setLayout(self.layout)
        self.setWindowTitle("Screenshot Control")
    
    def setPanelValue(self ):
        self.imgWidthSpin.setValue(400)
        self.imgHeightSpin.setValue(400)
        self.lyWidthSpin.setValue(180)
        self.showLypnCB.setCheckState(pya.Qt.Checked)
        self.showLndtCB.setCheckState(pya.Qt.Checked)
        self.showLnameCB.setCheckState(pya.Qt.Checked)
        self.showLsourceCB.setCheckState(pya.Qt.Checked)
        self.showLvisibleCB.setCheckState(pya.Qt.Checked)
        
    def initSignal(self):
        self.showLypnCB.stateChanged.connect(lambda n : self.enableLyChecks(n))
        

    def enableLyChecks(self, n):
        for option in [self.showLndtCB, self.showLnameCB, self.showLsourceCB, self.showLvisibleCB]:
            option.setEnabled(n == pya.Qt.Checked)
        
    def closeEvent(self, event):
        if self.waitClose:
            event.accept()
        else:
            self.parent.close()
            
if __name__ == "__main__" :
    w = ControlWidget()
    w.show()