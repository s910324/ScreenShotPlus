import pya
import pickle
from ctrl_bookmk_item import BMKItem

class BMKListWidget(pya.QListWidget):
    def __init__(self, parent = None):
        super(BMKListWidget, self).__init__()
        self.initUI()
        
    def initUI(self):
        pass

        
    def addBookmark(self, name, x1, y1, x2, y2):
        lwidget = BMKItem(self.count + 1, name, x1, y1, x2, y2, self)
        lItem   = pya.QListWidgetItem(self)
        lItem.setSizeHint(lwidget.sizeHint())
        self.addItem(lItem)
        self.setItemWidget(lItem, lwidget)
        
    def addBookmarks(self, bmks):
        for bmk in bmks:
            self.addBookmark( bmk["name"], bmk["x1"], bmk["y1"], bmk["x2"], bmk["y2"])
            
    def moveBMK(self, mv):
        datas        = self.bmkDatas()
        row          = self.currentRow
        dest         = (row + mv)
        dest         = 0              if dest < 0              else dest
        dest         = (self.count-1) if dest > (self.count-1) else dest       
        at_top_mvup  = (row == 0            and mv < 1)
        at_end_mvdn  = (row == self.count-1 and mv > 0)
        unchanged    = (dest == row)
        if any([at_top_mvup, at_end_mvdn, unchanged]) : return

        rowData = datas.pop(row)
        datas.insert(dest, rowData)
        self.clear()
        self.addBookmarks(datas)
        self.currentRow = dest
            
    def delBMK(self):
        datas        = self.bmkDatas()
        row          = self.currentRow
        rowData = datas.pop(row)
        self.clear()
        self.addBookmarks(datas)
        self.currentRow = row
    
    def bmkDatas(self):
        return [self.itemWidget( self.item (row)).value() for row in range(self.count)]
        
    def bmkWidgets(self):
        return [self.itemWidget( self.item (row))for row in range(self.count)]

    def selectFolder(self):

            self.folderPathEdit.setText(path)
            
    def save(self):
        path = pya.QFileDialog.getSaveFileName(filter = "*bmk")
        if path:
            with open(f'{path}.bmk', 'wb') as f:
                print("A")
                pickle.dump(self.bmkDatas(), f)
                print("B")
                pya.QToolTip.showText(pya.QCursor.pos, f"File saved : {path}")
                
    def load(self):
        path = pya.QFileDialog.getOpenFileName(filter = "*bmk")
        if path:
            with open(f'{path}.bmk', 'rb') as f:
                datas = pickle.load(f)
                self.clear()
                self.addBookmarks(datas)
                pya.QToolTip.showText(pya.QCursor.pos, f"File loaded : {path}")

if __name__ == "__main__" :
    w = BMKListWidget()
    w.addBookmark("bookmark 1",    0,    0, 500, 500)
    w.addBookmark("bookmark 2", -500, -500,   0,   0)
    w.addBookmark("bookmark 3", -500, -500, 500, 500)
    w.addBookmark("bookmark 4", -500, -500, 500, 500)
    w.addBookmark("bookmark 5", -500, -500, 500, 500)
    w.show()