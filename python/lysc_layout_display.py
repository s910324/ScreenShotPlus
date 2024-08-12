import pya

class LayoutDisplay(pya.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.viewer = pya.QLabel()
        self.layout = pya.QVBoxLayout()
        self.layout.addWidget(self.viewer)
        self.viewer.setAlignment(pya.Qt.AlignCenter)
        self.layout.setAlignment(pya.Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        #self.layout.addStretch()
        self.setLayout(self.layout)


if __name__ == "__main__" :
    w = LayoutDisplay()
    w.show()