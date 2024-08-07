import pya

class LayerImgLabel(pya.QWidget):
    def __init__(self, label_png, label_string, parent = None):
        super(LayerImgLabel, self).__init__(parent)  
        self.initUI()
        self.setDisplay(label_png, label_string)
        
    def initUI(self):
        self.layerPixmap = pya.QPixmap()
        self.layerImage  = pya.QLabel()
        self.layerLabel  = pya.QLabel()
        self.layout      = pya.QGridLayout()

        imgCol   = 1
        labelCol = 2
        self.layout.addWidget(self.layerImage, 0, imgCol,   1, 1)
        self.layout.addWidget(self.layerLabel, 0, labelCol, 1, 1)
        self.layout.setColumnStretch(labelCol, 1)
        self.layout.setColumnMinimumWidth(0, 5)
        self.layout.setColumnMinimumWidth(3, 5)
        self.layout.setContentsMargins(1,2,1,2)
        self.setLayout(self.layout)
    
    def setLabelDisplayLen(self, l):
        self.layerLabel.setFixedWidth(l)
     
    def setDisplay(self, label_png, label_string):
        self.layerLabel.setText(label_string + " ")
        self.layerPixmap.loadFromData(label_png)
        self.layerImage.setPixmap(self.layerPixmap)
       