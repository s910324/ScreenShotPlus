import pya

class GetScreenWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(GetScreenWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.getPB  = pya.QPushButton("Get screen")
        self.copyPB = pya.QPushButton("Copy screen to clipboard")
        self.layout = pya.QGridLayout()
        self.layout.addWidget(self.getPB,  1, 0, 1, 1)
        self.layout.addWidget(self.copyPB, 2, 0, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setRowMinimumHeight(0, 25)
        self.layout.setRowMinimumHeight(3, 25)
        self.setLayout(self.layout)