import pya
from lysc_layer_img_list import LayerImgList
from lysc_layout_display import LayoutDisplay


class LayerScreenShot(pya.QWidget):
    def __init__(self, control, parent = None):
        super(LayerScreenShot, self).__init__(parent)  
        self.imgW      = 400
        self.imgH      = 400
        self.lListD    = 180
        self.waitClose = True
        self.control   = control
        self.initUI()
        self.setDirection("L")

        
    def initUI(self):
        self.layerList = LayerImgList()
        self.ssWidget  = LayoutDisplay()
        self.layout    = pya.QGridLayout()
        self.layout.addWidget(self.ssWidget, 1, 1, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.setWindowTitle("Screenshot View")
    
    def setDirection(self, d):
        self.direction = d
        index = self.layout.indexOf(self.layerList)
        if index > 0 :
            self.layout.removeWidget (self.layerList)
        
        if d == "T" : 
            self.layout.addWidget(self.layerList, 0, 1, 1, 1)
            self.layerList.setHorizontal()
            
        if d == "L" : 
            self.layout.addWidget(self.layerList, 1, 0, 1, 1)
            self.layerList.setVertical()
            
        if d == "R" : 
            self.layout.addWidget(self.layerList, 1, 2, 1, 1)
            self.layerList.setVertical()
            
        if d == "B" : 
            self.layout.addWidget(self.layerList, 2, 1, 1, 1)
            self.layerList.setHorizontal()
        self.autoSizeWidget()
    
    def setImgDimension(self, w, h):
        self.imgW = w
        self.imgH = h
        self.autoSizeWidget()
        
    def setLableListDimension(self, dim):
        self.lListD = dim
        self.autoSizeWidget()

    def autoSizeWidget(self):
        self.ssWidget.setFixedSize(self.imgW, self.imgH)
        if self.direction in ["L", "R"]:
            self.layerList.setFixedSize(self.lListD, self.imgH)
            self.setFixedSize(self.imgW + self.lListD, self.imgH)
            
        if self.direction in ["T", "B"]:
            self.layerList.setFixedSize(self.imgW, self.lListD)
            self.setFixedSize(self.imgW, self.imgH + self.lListD)
        self.update()
                   
    def getScreen(self, w, h):
        self.ssWidget.getScreen(w, h)
        self.setImgDimension(w, h)

    def getLayerLabels(self, showLayerNo = True, showName = True, showSourceView = True, showOnlyVisible = True):
        self.layerList.getLayerIcon(showLayerNo, showName, showSourceView, showOnlyVisible)
        
    def renderImage(self):
        widgetImage = pya.QPixmap(self.size)
        self.render(widgetImage)
        return widgetImage
        
    def saveScreen(self, path):
        statusStr = "Invalid file path"
        if os.path.exists(os.path.dirname(path)):
            statusStr   = "File saved"
            self.renderImage().save(path)
        pya.QMessageBox.information(None, 'Status', f'{statusStr}\n{path}')
    
    def copyScreen(self):
        px = self.renderImage()
        pya.QApplication.clipboard().setPixmap(px)
        pya.QToolTip.showText(pya.QCursor.pos, "Image Copied to Clipboard")
        
    def keyPressEvent(self, e):
        if e.modifiers & pya.Qt.ControlModifier:
            if e.key() == pya.Qt.Key_C:
                self.copyScreen()
            
    def closeEvent(self, event):
        if self.waitClose:
            event.accept()
        else:
            if self.control : self.control.close()

    '''
    def eventFilter(self, source, event):
        if event.type() == pya.QEvent.WindowActivate:
            if not(self.control.isActiveWindow):
                self.control.activateWindow()
        event.accept()
    '''
        
if __name__ == "__main__" :
    w = LayerScreenShot(None)
    w.getScreen(400, 400)
    w.show()