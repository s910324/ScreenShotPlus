import pya
from lysc_layer_img_list import LayerImgList
from lysc_layout_display import LayoutDisplay


class LayerScreenShot(pya.QWidget):
    def __init__(self, control, parent = None):
        super(LayerScreenShot, self).__init__(parent)  
        self.initValue(control = control)
        self.initUI()
        self.initTheme()
        self.setLableListDimension(self.lListD)
        self.setDirection(self.direction)
        self.getLayerLabels()
        self.getScreen(self.imgW, self.imgH)
    
    def initValue(self, w = 400, h = 400, ld = 180, direction = "L", control = None):
        self.imgW      = w
        self.imgH      = h
        self.lListD    = ld
        self.waitClose = True
        self.control   = control
        self.direction = direction
        
    def initUI(self):
        self.layerList = LayerImgList()
        self.ssWidget  = LayoutDisplay()
        self.layout    = pya.QGridLayout()
        self.layout.addWidget(self.ssWidget, 1, 1, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.setWindowTitle("Screenshot View")

    def initTheme(self):
        self.check_cv()
        bgc        = self.cv.get_config("background-color") if self.cv else "#FFFFFF"
        bgc        = "#FFFFFF" if bgc == "auto" else bgc
        dark_bg    = (int(bgc[1:3], 16) + int(bgc[3:5], 16) + int(bgc[5:7], 16)) <= (255)
        txtc       = "#FFFFFF" if dark_bg else "#000000"
        ltxtc      = "#333333" if dark_bg else "#eeeeee"
        sswStyle   = f"""
            QWidget{{
                background-color : {bgc};
                
            }}
            QLabel{{
                color: {ltxtc};
                font: bold 36px;
            }}

        """
        
        llStyle = f"""
            QListWidget{{
                background-color : {bgc}; 
                border-style     : solid; 
                border           : None;
            }}
            QLabel{{
                color: {txtc};
            }}
        """
        
        self.ssWidget.setStyleSheet(sswStyle)
        self.layerList.setStyleSheet(llStyle)
        
    def check_cv(self):
        self.cv = pya.Application.instance().main_window().current_view()
        return self.cv
        
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
        self.layerList.setVisible(not(self.direction == "H"))
        self.ssWidget.setFixedSize(self.imgW, self.imgH)
        if self.direction in ["L", "R"]:
            self.layerList.setFixedSize(self.lListD, self.imgH)
            self.setFixedSize(self.imgW + self.lListD, self.imgH)
            
        if self.direction in ["T", "B"]:
            self.layerList.setFixedSize(self.imgW, self.lListD)
            self.setFixedSize(self.imgW, self.imgH + self.lListD)
            
        if self.direction in ["H"]:
            self.setFixedSize(self.imgW, self.imgH)
        
        self.update()
                   
    def getScreen(self, w, h, oversampling= 0, showRuler = "true", gridStyle = "dots", axisStyle = "lines", showText = "true"):
        if not(self.check_cv()) : 
            self.ssWidget.viewer.setText("No Layout avaliable")
            return
        
        settings = {
            "grid-visible"    : "true",
            "grid-show-ruler" : showRuler, # ruler
            "grid-style0"     : axisStyle, # axis
            "grid-style1"     : gridStyle, # near style
            "grid-style2"     : gridStyle, # far  style
            "text-visible"    : showText,  
        }
        
        for s in settings:
            self.cv.set_config(s, settings[s])

        img = self.cv.get_image_with_options(w, h)
        self.ssWidget.viewer.setPixmap(pya.QPixmap().fromImage(img))
        self.setImgDimension(w, h)
        self.getLayerLabels()
        self.cv.clear_config()
        
    def getLayerLabels(self, *args, **argv):
        self.layerList.getLayerIcon(*args, **argv)
        
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
    w.getLayerLabels()
    w.show()