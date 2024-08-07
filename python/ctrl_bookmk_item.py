import pya

class BMKItem(pya.QWidget):
    def __init__(self, index, name, x1, y1, x2, y2, parent = None):
        super(BMKItem, self).__init__(parent)  
        self.initUI()
        self.setValue(index, name, x1, y1, x2, y2)
        
    def initUI(self):
        self.idLB    = pya.QLabel()
        self.nameLE  = pya.QLineEdit()
        self.rectLB  = pya.QLabel()
        self.y1LB    = pya.QLineEdit()
        self.x2LB    = pya.QLineEdit()
        self.y2LB    = pya.QLineEdit()
        self.layout  = pya.QGridLayout()

        self.layout.addWidget(self.idLB,   0, 0, 1, 1)
        self.layout.addWidget(self.nameLE, 0, 1, 1, 1)
        self.layout.addWidget(self.rectLB, 0, 2, 1, 1)

        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 1)
        self.layout.setColumnStretch(5, 1)
        self.layout.setColumnStretch(6, 1)
        self.layout.setColumnMinimumWidth(0, 25)
        self.layout.setColumnMinimumWidth(1, 45)
        self.layout.setContentsMargins(5,10,5,10)
        self.setLayout(self.layout)
        
    
    def setValue(self, index, name, x1, y1, x2, y2, value = 0):
        self.index = index
        self.name  = name
        self.x1    = x1
        self.y1    = y1
        self.x2    = x2
        self.y2    = y2
        self.idLB.setText(f"#{index}")
        self.nameLE.setText(name)
        self.rectLB.setText(f"({x1:.3f}, {y1:.3f})\n({x2:.3f},{y2:.3f})")
    
    def setIndex(self, index):
        self.idLB.setText("#{value}")

    def value(self):
        return {
            #"index": self.index,
            "name" : self.name,
            "x1"   : self.x1,
            "y1"   : self.y1,
            "x2"   : self.x2,
            "y2"   : self.y2,
        }
        
if __name__ == "__main__" :
    w = BMKItem(0, "name", 123, 223, 323, 423)
    w.show()      