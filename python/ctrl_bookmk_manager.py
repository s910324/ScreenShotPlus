import pya
from ctrl_misc        import *
from ctrl_bookmk_item import BMKItem
from ctrl_bookmk_list import BMKListWidget

class BMKManager(pya.QWidget):
    def __init__(self, parent = None):
        super(BMKManager, self).__init__()
        self.initUI()
        self.initSignal()
        
    def initUI(self):
        self.listW    = BMKListWidget()
        self.addPB    = RPushButton()
        self.delPB    = RPushButton()
        self.mvTopPb  = RPushButton()
        self.mvUpPb   = RPushButton()
        self.mvDnPb   = RPushButton()
        self.mvEndPb  = RPushButton()
        self.exportPB = RPushButton()
        self.importPB = RPushButton()
        self.layout   = pya.QGridLayout()
        
        self.layout.addWidget(self.listW,    0, 0, 11, 1)
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

        icon_config = {
            self.addPB    : "bookmark-regular", 
            self.delPB    : "trash-solid", 
            self.mvTopPb  : "angles-up-solid", 
            self.mvUpPb   : "angle-up-solid", 
            self.mvDnPb   : "angle-down-solid", 
            self.mvEndPb  : "angles-down-solid", 
            self.exportPB : "file-export-solid", 
            self.importPB : "file-import-solid", 
        }
        
        for w in icon_config:
            w.setIcon(svgIcon(icon_config[w]))
            w.setIconSize(pya.QSize(12, 12))
            w.setFixedSize(pya.QSize(28, 28))


    def initSignal(self):
        # self.addPB.clicked.connect(   lambda : self.addBookmark("Testing", 0, 0, 5, 5))
        self.mvUpPb.clicked.connect(  lambda : self.listW.moveBMK(-1))
        self.mvDnPb.clicked.connect(  lambda : self.listW.moveBMK( 1))
        self.mvTopPb.clicked.connect( lambda : self.listW.moveBMK(-self.listW.count))
        self.mvEndPb.clicked.connect( lambda : self.listW.moveBMK( self.listW.count))
        self.delPB.clicked.connect(   lambda : self.listW.delBMK())
        self.exportPB.clicked.connect(lambda : self.listW.load())
        self.importPB.clicked.connect(lambda : self.listW.save())
        
    def addBookmark(self, name, x1, y1, x2, y2):
        self.listW.addBookmark(name, x1, y1, x2, y2)  
    
    def bookmarks(self) :
        return [self.listW.itemWidget(self.listW.item (row)).value() for row in range(self.listW.count)]
               
if __name__ == "__main__" :
    w = BMKManager()
    w.addBookmark("bookmark 1",    0,    0, 500, 500)
    w.addBookmark("bookmark 2", -500, -500,   0,   0)
    w.addBookmark("bookmark 3", -500, -500, 500, 500)
    w.addBookmark("bookmark 4",    0,    0, 500, 500)
    w.addBookmark("bookmark 5", -500, -500,   0,   0)
    w.addBookmark("bookmark 6", -500, -500, 500, 500)
    w.addBookmark("bookmark 7", -500, -500, 500, 500)
    w.addBookmark("bookmark 8", -500, -500, 500, 500)
    w.show()