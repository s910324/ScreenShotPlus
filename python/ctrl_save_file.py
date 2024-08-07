import pya
import os

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
        self.cancelPB       = pya.QPushButton("Cancel")
        self.layout         = pya.QGridLayout()
                
        self.layout.addWidget(pya.QLabel("Folder path:"), 0, 0, 1, 1)
        self.layout.addWidget(pya.QLabel("File name:"),   1, 0, 1, 1)
        
        self.layout.addWidget(self.folderPathEdit, 0, 1, 1, 1)
        self.layout.addWidget(self.getFolderPB,    0, 2, 1, 1)
        self.layout.addWidget(self.fileNameEdit,   1, 1, 1, 2)
        self.layout.addWidget(self.savePB,         2, 1, 1, 2)
        self.layout.addWidget(self.cancelPB,       3, 1, 1, 2)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setColumnMinimumWidth(0, 70)
        self.layout.setColumnStretch(1, 1)
        self.setLayout(self.layout)
        self.getFolderPB.setFixedWidth(25)
        self.folderPathEdit.setEnabled(False)
        
    
    def initSignal(self):
        self.savePB.clicked.connect(self.save)
        self.getFolderPB.clicked.connect(self.selectFolder)
    
    def selectFolder(self):
        path = pya.QFileDialog.getExistingDirectory()
        if path:
            self.folderPathEdit.setText(path)

    def save(self):
        invalid    = ['<', '\\', '|', '/', '>', ':', '*', '?', '"']
        folderPath = self.folderPathEdit.text
        fileName   = self.fileNameEdit.text
        self.saveFullPath = None

        if (fileName == "") or any([(i in fileName) for i in invalid]):
            return
            
        if not(os.path.isdir(folderPath)): 
            return
            
        self.saveFullPath = os.path.join(folderPath, f"{fileName}.png")

                
                
if __name__ == "__main__" :
    w = SaveFileWidget()
    w.show()