import pya
from ctrl_bookmk_item import BMKItem

class BMKListWidget(pya.QListWidget):
    def __init__(self, parent = None):
        super(BMKListWidget, self).__init__()

    def addBookmark(self, name, x1, y1, x2, y2):
        lwidget = BMKItem(self.count + 1, name, x1, y1, x2, y2, self)
        lItem   = pya.QListWidgetItem(self)
        lItem.setSizeHint(lwidget.sizeHint())
        self.addItem(lItem)
        self.setItemWidget(lItem, lwidget)
        
    def keyPressEvent(self, e):
        print (e.key())
        if e.key() == pya.Qt.Key_Delete:
            print("OK")
        
if __name__ == "__main__" :
    w = BMKListWidget()
    w.addBookmark("bookmark 1",    0,    0, 500, 500)
    w.addBookmark("bookmark 2", -500, -500,   0,   0)
    w.addBookmark("bookmark 3", -500, -500, 500, 500)
    w.show()