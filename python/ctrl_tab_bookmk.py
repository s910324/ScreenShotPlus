import pya

from ctrl_bookmk_list    import BMKListWidget
from ctrl_set_view       import SetViewWidget
from ctrl_misc           import HLine

class BMKTabWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(BMKTabWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.viewCfg = SetViewWidget()
        self.viewBMK = BMKListWidget()
        self.layout  = pya.QGridLayout()
        self.layout.addWidget(self.viewCfg, 0, 0, 1, 1)
        self.layout.addWidget(HLine(self),  1, 0, 1, 1)
        self.layout.addWidget(self.viewBMK, 2, 0, 1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowMinimumHeight(1, 15)
        self.setLayout(self.layout)