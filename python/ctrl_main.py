import pya
import pickle

from lysc_layer_img_list      import LayerImgList
from lysc_layout_display      import LayoutDisplay
from lysc_layer_screen_shot   import LayerScreenShot
from ctrl_save_file           import SaveFileWidget
from ctrl_tab_bookmk          import BMKTabWidget
from ctrl_tab_disp            import DisplayTabWidget
from ctrl_get_screen          import GetScreenWidget

class ControlWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(ControlWidget, self).__init__()
        self.mw         = pya.Application.instance().main_window()
        self.cv         = self.mw.current_view()
        self.waitUpdate = False
        self.installEventFilter(self)
        self.initUI()
        self.initTheme()
        self.initSignal()
        self.initVal()
        self.getScreen()

    def check_cv(self):
        self.cv = self.mw.current_view()
        return self.cv
        

    def initUI(self):
        self.disp     = LayerScreenShot(control = self)
        self.saveW    = SaveFileWidget()
        self.getW     = GetScreenWidget()
        self.dispW    = DisplayTabWidget()
        self.viewW    = BMKTabWidget()
        self.ctrlTab  = pya.QTabWidget()
        self.layout   = pya.QGridLayout()
        
        self.ctrlTab.addTab(self.dispW, "Display Setting")
        self.ctrlTab.addTab(self.viewW, "View Setting")
        
        self.layout.addWidget(self.ctrlTab, 0, 0, 1, 1)
        self.layout.addWidget(self.getW,    1, 0, 1, 1)
        self.layout.addWidget(self.saveW,   2, 0, 1, 1)
        self.setLayout(self.layout)
        self.disp.waitClose = False
        self.setWindowTitle("Screenshot Control")

    def initTheme(self):
        if self.check_cv():
            bgc        = self.cv.get_config("background-color") if self.cv else "#FFFFFF"
            bgc        = "#FFFFFF" if bgc == "auto" else bgc
            dark_bg    = (int(bgc[1:3], 16) + int(bgc[3:5], 16) + int(bgc[5:7], 16)) <= (255)
            txtc       = "#FFFFFF" if dark_bg else "#000000"
            styleSheet = f"""
                QWidget{{    background-color : {bgc};}}
                QListWidget{{background-color : {bgc}; border-style : solid; border : None;}}
                QLabel{{color: {txtc};}}
            """
            self.disp.setStyleSheet(styleSheet)
        
    def initVal(self):
        loaded = self.loadSettings()    
        
        if not(loaded):
            imgCfg  = self.dispW.imgCfg
            dispCfg = self.dispW.dispCfg
            imgCfg.imgWSpn.setValue(400)
            imgCfg.imgHSpn.setValue(400)
            imgCfg.lyWSpn.setValue(180)
            self.disp.layerList.setFixedWidth(180)
            for cb in [dispCfg.showLypnCB, dispCfg.showLnumCB, dispCfg.showLnameCB, dispCfg.showLsourCB, dispCfg.showLvisCB]:
                cb.setCheckState(pya.Qt.Checked)
        
    def initSignal(self):
        dispCfg = self.dispW.dispCfg
        imgCfg  = self.dispW.imgCfg
        viewCfg = self.viewW.viewCfg
        viewBMK = self.viewW.viewBMK

        viewCfg.getViewPB.clicked.connect(       lambda   : self.getViewBox())
        viewCfg.setFitPB.clicked.connect(        lambda   : self.zoomFit())
        viewCfg.setViewPB.clicked.connect(       lambda   : self.setView())
        viewCfg.bkViewPB.clicked.connect(        lambda   : self.bkView())
        dispCfg.showLypnCB.stateChanged.connect( lambda n : self.enableLyChecks(n))
        imgCfg.lyWSpn.valueChanged.connect(      lambda w : self.disp.setLableListDimension(w))
        #viewBMK.itemDoubleClicked.connect(       lambda i : self.gotoBMK(i))
        self.getW.getPB.clicked.connect(         lambda   : self.getScreen())
        self.getW.copyPB.clicked.connect(        lambda   : self.disp.copyScreen())
        self.saveW.savePB.clicked.connect(       lambda   : self.saveW.save(self.disp.renderImage(), "png")) 
        
        for cb in [dispCfg.showLnumCB, dispCfg.showLnameCB, dispCfg.showLsourCB, dispCfg.showLvisCB]:
            cb.stateChanged.connect( lambda  : self.getLayerLabels())
            
        dispCfg.dirCB.currentIndexChanged.connect(  lambda i : self.disp.setDirection(dispCfg.dirCB.itemData(i)))
        dispCfg.gridCB.currentIndexChanged.connect( lambda i : self.getScreen())
        dispCfg.scaleCB.currentIndexChanged.connect(lambda i : self.getScreen())
        dispCfg.axisCB.currentIndexChanged.connect( lambda i : self.getScreen())
        
    def getScreen(self):
        if not(self.check_cv()) : return
        
        dispCfg  = self.dispW.dispCfg
        imgCfg   = self.dispW.imgCfg
        
        settings = {
            "grid-visible"    : "true",
            "grid-show-ruler" : dispCfg.scaleCB.itemData (dispCfg.scaleCB.currentIndex), # ruler
            "grid-style0"     : dispCfg.axisCB.itemData  (dispCfg.axisCB.currentIndex ), # axis
            "grid-style1"     : dispCfg.gridCB.itemData  (dispCfg.gridCB.currentIndex ), # near style
            "grid-style2"     : dispCfg.gridCB.itemData  (dispCfg.gridCB.currentIndex ), # far  style
        }
        
        for s in settings:
            self.cv.set_config(s, settings[s])

        self.disp.getScreen(
            w = imgCfg.imgWSpn.value, 
            h = imgCfg.imgHSpn.value, 
        )
        
        self.getLayerLabels()
        self.cv.clear_config()
        
    def getLayerLabels(self):
        dispCfg  = self.dispW.dispCfg
        self.disp.getLayerLabels(            
            showLayerNo     = dispCfg.showLnumCB.checkState  == pya.Qt.Checked, 
            showName        = dispCfg.showLnameCB.checkState == pya.Qt.Checked, 
            showSourceView  = dispCfg.showLsourCB.checkState == pya.Qt.Checked, 
            showOnlyVisible = dispCfg.showLvisCB.checkState  == pya.Qt.Checked
        )
        
    def getViewBox(self):
        if not(self.check_cv()) : return
        b       = self.cv.box()
        viewCfg = self.viewW.viewCfg
        viewCfg.vp1xDblSpn.value = b.p1.x
        viewCfg.vp1yDblSpn.value = b.p1.y
        viewCfg.vp2xDblSpn.value = b.p2.x
        viewCfg.vp2yDblSpn.value = b.p2.y

    
    def setView(self):
        if not(self.check_cv()) : return
        
        viewCfg = self.viewW.viewCfg
        b       = pya.DBox(
            viewCfg.vp1xDblSpn.value,
            viewCfg.vp1yDblSpn.value,
            viewCfg.vp2xDblSpn.value,
            viewCfg.vp2yDblSpn.value,
        )
        self.cv.zoom_box(b)
        self.getScreen()
        
    def zoomFit(self):
        if not(self.check_cv()) : return
        self.cv.zoom_fit()
        self.getScreen()
    
    def bkView(self):
        viewBMK = self.viewW.viewBMK
        viewCfg = self.viewW.viewCfg

        viewBMK.addBookmark(
            "Undefined",
            viewCfg.vp1xDblSpn.value,
            viewCfg.vp1yDblSpn.value,
            viewCfg.vp2xDblSpn.value,
            viewCfg.vp2yDblSpn.value,
        )

        
    def gotoBMK(self, item):
        viewBMK = self.viewW.viewBMK
        bmk     = viewBMK.itemWidget(item).value()
        
        if not(self.check_cv()) : return

        viewCfg = self.viewW.viewCfg
        viewCfg.vp1xDblSpn.value = bmk["x1"]
        viewCfg.vp1yDblSpn.value = bmk["y1"]
        viewCfg.vp2xDblSpn.value = bmk["x2"]
        viewCfg.vp2yDblSpn.value = bmk["y2"]
        b = pya.DBox(
            bmk["x1"],
            bmk["y1"],
            bmk["x2"],
            bmk["y2"],
        )
        self.cv.zoom_box(b)
        self.getScreen()
        
    def enableLyChecks(self, n):
        dispCfg = self.dispW.dispCfg
        enable  = (n in [ pya.Qt.Checked, True])
        for cb in [dispCfg.showLnumCB, dispCfg.showLnameCB, dispCfg.showLsourCB, dispCfg.showLvisCB]:
            cb.setEnabled(enable)
        self.disp.layerList.setVisible(enable)
    
    def saveSettings(self):
        dispCfg  = self.dispW.dispCfg
        imgCfg   = self.dispW.imgCfg
        viewBMK  = self.viewW.viewBMK
        settings = {
            "imgWSpn"     : imgCfg.imgWSpn.value,
            "imgHSpn"     : imgCfg.imgHSpn.value,
            "lyWSpn"      : imgCfg.lyWSpn.value,
            "ovspSpn"     : imgCfg.ovspSpn.value,
            
            "showLypnCB"  : dispCfg.showLypnCB.checkState  == pya.Qt.Checked, 
            "showLnumCB"  : dispCfg.showLnumCB.checkState  == pya.Qt.Checked, 
            "showLnameCB" : dispCfg.showLnameCB.checkState == pya.Qt.Checked, 
            "showLsourCB" : dispCfg.showLsourCB.checkState == pya.Qt.Checked, 
            "showLvisCB"  : dispCfg.showLvisCB.checkState  == pya.Qt.Checked, 
            "dirCB"       : dispCfg.dirCB.currentIndex,
            "gridCB"      : dispCfg.gridCB.currentIndex,
            "scaleCB"     : dispCfg.scaleCB.currentIndex,
            "axisCB"      : dispCfg.axisCB.currentIndex,
            "bookmarks"   : [viewBMK.itemWidget(viewBMK.item (row)).value() for row in range(viewBMK.count)],
        }
        dirPath  = os.path.dirname(__file__) 
        filepath = os.path.realpath(os.path.join(dirPath, "setting.pkl"))
       
        with open(filepath, 'wb') as f:
            pickle.dump(settings, f)

    def loadSettings(self):
        dirPath  = os.path.dirname(__file__) 
        filepath = os.path.realpath(os.path.join(dirPath, "setting.pkl"))
        dispCfg  = self.dispW.dispCfg
        imgCfg   = self.dispW.imgCfg
        viewBMK  = self.viewW.viewBMK
        if not(os.path.isfile(filepath)) : return False
        
        with open(filepath, 'rb') as f:  
            try:
                s = pickle.load(f)
                imgCfg.imgWSpn.setValue( s["imgWSpn"])
                imgCfg.imgHSpn.setValue( s["imgHSpn"])
                imgCfg.lyWSpn.setValue ( s["lyWSpn" ])
                imgCfg.ovspSpn.setValue( s["ovspSpn"])
                
                dispCfg.showLypnCB.setCheckState ( pya.Qt.Checked if s["showLypnCB" ] else pya.Qt.Unchecked)
                dispCfg.showLnumCB.setCheckState ( pya.Qt.Checked if s["showLnumCB" ] else pya.Qt.Unchecked)
                dispCfg.showLnameCB.setCheckState( pya.Qt.Checked if s["showLnameCB"] else pya.Qt.Unchecked)
                dispCfg.showLsourCB.setCheckState( pya.Qt.Checked if s["showLsourCB"] else pya.Qt.Unchecked)
                dispCfg.showLvisCB.setCheckState ( pya.Qt.Checked if s["showLvisCB" ] else pya.Qt.Unchecked)
                dispCfg.dirCB.setCurrentIndex  (s["dirCB" ])
                dispCfg.gridCB.setCurrentIndex (s["gridCB" ])
                dispCfg.scaleCB.setCurrentIndex(s["scaleCB"])
                dispCfg.axisCB.setCurrentIndex (s["axisCB" ])
                self.enableLyChecks(s["showLypnCB" ])
                for bmk in s["bookmarks"]:
                    viewBMK.addBookmark(bmk["name"], bmk["x1"], bmk["y1"], bmk["x2"], bmk["y2"])
            except Exception:
                pass
        return True
        
    def closeEvent(self, event):
        self.disp.waitClose = True
        self.disp.close()
        self.saveSettings()
        event.accept()
    '''
    def changeEvent(self, event):
        print(event.type())
        if event.type() == pya.QEvent.ActivationChange:
            self.getScreen()
            print("OK")
    
    def eventFilter(self, source, event):
       
        
        if event.type() in[pya.QEvent.ActivationChange, pya.QEvent.WindowStateChange]:
            
            chk = [self.isActiveWindow, self.disp.isActiveWindow, self.isHidden(), self.disp.isHidden()]
            print(event.type())
            print(chk)
            if chk == [False, False]:
                #self.disp.lower()
                pass
            if chk == [True, False]:
                pass
                #self.disp.showNormal()
                #self.disp.raise_()
            
        
        if event.type() in [pya.QEvent.WindowActivate, pya.QEvent.MouseButtonPress]:
            if self.waitUpdate:
                self.getScreen()
                self.waitUpdate = False

        elif event.type() in [pya.QEvent.Leave, pya.QEvent.WindowDeactivate]:
            self.waitUpdate = True
        
        event.accept()
    '''
if __name__ == "__main__" :
    wmain, hmain = 500, 500
    wctrl, hctrl = 300, 500
    xmain, ymain = 300, 300
    xctrl        = xmain + wmain + wctrl /2
    yctrl        = ymain


    ctrl = ControlWidget()
    disp = ctrl.disp
    disp.setGeometry(xmain, ymain, wmain, hmain)
    ctrl.setGeometry(xctrl, yctrl, wctrl, hctrl)
    disp.show()
    ctrl.show()
    
