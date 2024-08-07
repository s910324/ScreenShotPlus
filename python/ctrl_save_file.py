import pya
import os
from glob import glob

class SaveFileWidget(pya.QWidget):
    def __init__(self, parent = None):
        super(SaveFileWidget, self).__init__()
        self.saveFullPath = None
        self.initUI()
        self.initSignal()
        
    def initUI(self):
        self.folderPathEdit = pya.QLineEdit()
        self.fileNameEdit   = pya.QLineEdit()
        self.getFolderPB    = pya.QPushButton("...")
        self.savePB         = pya.QPushButton("Save")
        self.layout         = pya.QGridLayout()
                
        self.layout.addWidget(pya.QLabel("Folder path:"), 0, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("File name:"),   1, 0, 1, 1)
        
        self.layout.addWidget(self.folderPathEdit, 0, 1, 1, 1)
        self.layout.addWidget(self.getFolderPB,    0, 2, 1, 1)
        self.layout.addWidget(self.fileNameEdit,   1, 1, 1, 1)
        self.layout.addWidget(self.savePB,         1, 2, 1, 1)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setColumnMinimumWidth(0, 70)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)
        self.savePB.setFixedWidth(35)
        self.getFolderPB.setFixedWidth(35)
        self.folderPathEdit.setEnabled(False)
        
    
    def initSignal(self):
        self.savePB.clicked.connect(lambda : self.save())
        self.getFolderPB.clicked.connect(self.selectFolder)
    
    def selectFolder(self):
        path = pya.QFileDialog.getExistingDirectory()
        if path:
            self.folderPathEdit.setText(path)

    def save(self, data = "TEST", suffix = "txt", override = False):
        invalid    = ['<', '\\', '|', '/', '>', ':', '*', '?', '"']
        folderPath = self.folderPathEdit.text
        fileName   = self.fileNameEdit.text
        self.saveFullPath = None
        
        
        if (fileName == "") or any([(i in fileName) for i in invalid]):
            pya.QToolTip.showText(pya.QCursor.pos, "File name Invalid")
            return
            
        if len(folderPath) == 0: 
            pya.QToolTip.showText(pya.QCursor.pos, "Select save path")
            return
                        
        if not(os.path.isdir(folderPath)): 
            pya.QToolTip.showText(pya.QCursor.pos, "File Path not existed")
            return
            
        modifier = "" 
        if not (override):
            existing_files    = glob(os.path.join(folderPath, f"{fileName}*.{suffix}"))
            modifier          = f"({len(existing_files) + 1})" if existing_files else ""
            if modifier:
                pass #todo: override notice
            
        self.saveFullPath = os.path.join(folderPath, f"{fileName}{modifier}.{suffix}")

        if isinstance(data, pya.QPixmap): 
            data.save(self.saveFullPath)
        else:
            with open(self.saveFullPath, 'w') as f:
                f.write(str(data)) 
 
        pya.QToolTip.showText(pya.QCursor.pos, f"File saved: {self.saveFullPath}")
           


      
                
if __name__ == "__main__" :
    w = SaveFileWidget()
    w.show()