import pya

from ctrl_display_config import DisplayConfigWidget
from ctrl_img_config     import ImageConfigWidget
from ctrl_misc           import HLine

class DisplayTabWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(DisplayTabWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.imgCfg  = ImageConfigWidget()
        self.dispCfg = DisplayConfigWidget()
        self.layout  = pya.QGridLayout()
        self.layout.addWidget(self.imgCfg,  0, 0, 1, 1)
        self.layout.addWidget(HLine(self),  1, 0, 1, 1)
        self.layout.addWidget(self.dispCfg, 2, 0, 1, 1)
        self.layout.setRowStretch(3, 1)
        self.layout.setRowMinimumHeight(1, 15)
        self.setLayout(self.layout)