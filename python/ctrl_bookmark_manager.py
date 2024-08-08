import pya
from ctrl_bookmk_item import BMKItem
from ctrl_bookmk_list import BMKListWidget

class BMKManager(pya.QWidget):
    def __init__(self, parent = None):
        super(BMKManager, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.listW    = BMKListWidget()
        self.addPB    = pya.QPushButton("add")
        self.delPB    = pya.QPushButton("delete")
        self.mvTopPb  = pya.QPushButton("")
        self.mvUpPb   = pya.QPushButton("")
        self.mvDnPb   = pya.QPushButton("")
        self.mvEndPb  = pya.QPushButton("")
        self.exportPB = pya.QPushButton("")
        self.importPB = pya.QPushButton("")
        self.layout   = pya.QGridLayout()
        
        self.layout.addWidget(self.listW,    0, 0, 10, 1)
        self.layout.addWidget(self.addPB,    0, 1,  1, 1)
        self.layout.addWidget(self.mvTopPb,  1, 1,  1, 1)
        self.layout.addWidget(self.mvUpPb,   2, 1,  1, 1)
        self.layout.addWidget(self.mvDnPb,   3, 1,  1, 1)
        self.layout.addWidget(self.mvEndPb,  4, 1,  1, 1)
        self.layout.addWidget(self.importPB, 6, 1,  1, 1)
        self.layout.addWidget(self.exportPB, 7, 1,  1, 1)
        self.layout.addWidget(self.delPB,    9, 1,  1, 1)
        self.layout.setContentsMargins(      0, 0,  0, 0)
        self.setLayout(self.layout)
        
        self.layout.setRowStretch( 5, 1)
        self.layout.setRowStretch( 8, 1)
        self.layout.setRowStretch(10, 1)
        
if __name__ == "__main__" :
    w = BMKManager()

    w.show()