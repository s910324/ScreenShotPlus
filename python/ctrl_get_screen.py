import pya

class GetScreenWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(GetScreenWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.getPB  = pya.QPushButton("Get screen")
        self.copyPB = pya.QPushButton("Copy screen")
        self.layout = pya.QGridLayout()
        self.layout.addWidget(self.getPB,  1, 0, 1, 1)
        self.layout.addWidget(self.copyPB, 1, 2, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setRowMinimumHeight(0, 25)
        self.layout.setRowMinimumHeight(3, 25)
        self.setLayout(self.layout)
        
        
if __name__ == "__main__" :
    w = GetScreenWidget()
    w.show()