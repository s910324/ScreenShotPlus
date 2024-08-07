import pya

class LayoutDisplay(pya.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.viewer = pya.QLabel()
        self.layout = pya.QVBoxLayout()
        self.layout.addWidget(self.viewer)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def getScreen(self, *args, **kwards):
        cv = pya.Application.instance().main_window().current_view()
        if cv :
            img = cv.get_image_with_options(*args, **kwards)
            self.viewer.setPixmap(pya.QPixmap().fromImage(img))
        else:
            self.viewer.setText("No Layout avaliable")
            
if __name__ == "__main__" :
    w = LayoutDisplay()
    w.getScreen(width = 400, height = 400)
    w.show()