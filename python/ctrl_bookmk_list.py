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

    def dragMoveEvent(self, event):
        if event.keyboardModifiers():
            event.ignore()
        else:
            super().dragMoveEvent(event)
            self.updateBMKOrder()

    def dropEvent(self, event):
        if event.keyboardModifiers():
            event.ignore()
        else:
            super().dropEvent(event)
            self.updateBMKOrder()

    def deleteupdateBMKOrder(self, cardWidget):
        for row in range(self.count()):
            if self.itemWidget( self.item (row)) == cardWidget:
                self.takeItem (row)
        self.updateCardOrder()


    def bmkWidgets(self):
        return [self.itemWidget( self.item (row))for row in range(self.count())]

    def updateBMKOrder(self):
        for index, widget in enumerate(self.cardWidgets()):
            widget.setSequnce(index+1)

    def save(self, path=""):
        with open(r'.\export.rcp', 'wb') as f:
            for index, widget in enumerate(self.cardWidgets()):
                pickle.dump(widget, f)

    def load(self, path=""):
        self.clear()
        with open(r'.\export.rcp', 'rb') as f:
            widget = pickle.load(f)
            self.addCard(widget)

if __name__ == "__main__" :
    w = BMKListWidget()
    w.addBookmark("bookmark 1",    0,    0, 500, 500)
    w.addBookmark("bookmark 2", -500, -500,   0,   0)
    w.addBookmark("bookmark 3", -500, -500, 500, 500)
    w.show()