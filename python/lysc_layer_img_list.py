import pya
from lysc_layer_img_label import LayerImgLabel

class LayerImgList(pya.QListWidget):
    def __init__(self, parent = None):
        super(LayerImgList, self).__init__()
        self.initUI()
        self.setVertical()
    
    def initUI(self):
        self.setHorizontalScrollBarPolicy(pya.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(pya.Qt.ScrollBarAlwaysOff)
        self.setUniformItemSizes(True)
        
        self.setFrameShape(pya.QFrame.Panel)
        self.setFrameShadow(pya.QFrame.Plain)
        self.setLineWidth(0)
        
    def setHorizontal(self):
        self.setResizeMode(pya.QListView.Adjust)
        self.setViewMode(pya.QListView.IconMode)
        self.setFlow(pya.QListView.LeftToRight)
        
    def setVertical(self):
        self.setResizeMode(pya.QListView.Fixed)
        self.setViewMode(pya.QListView.ListMode)
        self.setFlow(pya.QListView.TopToBottom)
        
    def addLayerItem(self, label_png, label_text):
        lwidget = LayerImgLabel(label_png, label_text, self)
        lItem   = pya.QListWidgetItem(self)
        lItem.setSizeHint(lwidget.sizeHint())
        lItem.setFlags(pya.Qt.NoItemFlags)
        self.addItem(lItem)
        self.setItemWidget(lItem, lwidget)
        return lwidget, lItem
    
    def getLabelData(self, cv, layer_iter, showLayerNo, showName, showSourceView):
        layerProp = layer_iter.current()
        if layerProp.source_cellview < 0:
            showLayerNo    = False
            showSourceView = False
            
        lp_lydt     = f"{layerProp.source_layer}/{layerProp.source_datatype}" if showLayerNo                      else None
        lp_name     = f"{layerProp.name}"                                     if (layerProp.name  and showName )  else None
        lp_source   = f"@{layerProp.source_cellview + 1}"                     if  showSourceView                  else None
        label_text  = " - ".join([txt for txt in [lp_name, lp_lydt, lp_source] if txt])
        
        label_png   = cv.icon_for_layer(layer_iter, 25, 10, 1).to_png_data()
        return {"img" : label_png, "txt" : label_text}

    def setTheme(self, bgc, txtc):
        self.txtc = txtc
        self.bgc  = bgc
            
    def getLayerIcon(self, 
            showLayerNo = True, showName   = True, showSourceView = True, 
            hideHiddenL = True, hideEmptyL = True, hideNIVL       = True, ):
        cv = pya.Application.instance().main_window().current_view()
        if not(cv): return

        self.clear()
        layer_iter = cv.begin_layers()
        labelData  = []
        while not(layer_iter.at_end()):  

            layerProp = layer_iter.current()  
            if [hideHiddenL, layerProp.visible] in [[True, True], [False, True], [False, False]] : 
                labelData.append(self.getLabelData(cv, layer_iter, showLayerNo, showName, showSourceView))
            layer_iter.next()
        
        labelDispLen = max([len(ld["txt"]) for ld in labelData])

        for ld in labelData:
            lwidget, lItem = self.addLayerItem(ld["img"], ld["txt"])
            lwidget.setLabelDisplayLen(15 + labelDispLen * 6 )
            lItem.setSizeHint(lwidget.sizeHint())
            lwidget.update()
            
if __name__ == "__main__" :
    w = LayerImgList()
    w.getLayerIcon(showName   = False)
    w.resize(300, 150)
    w.show()