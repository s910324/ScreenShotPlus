
import os
import sys
import pya

class RoundPushButton(pya.QPushButton):
	def __init__(self, *args, **argv):
		super(RoundPushButton, self).__init__(*args, **argv)

		self.theme = """
			QPushButton {
				padding: 0.2em 0.2em 0.2em 0.2em;
				color: #dddddd;
				background-color: rgba(35, 80, 35, 110);
				border-style: solid;
				border-width: 0px;
				border-radius: 3px;
			}

			QPushButton:hover {
				background-color: rgba(35, 80, 35, 90);
			}
			 
			QPushButton:pressed {
				background-color: rgba(35, 80, 35, 60);
			}

			QPushButton:disabled {
				color: #999999;
				background-color: rgba(200, 200, 200, 50);
			}

			QPushButton[warning='true'] {
				background-color: rgba(240, 140, 0, 120);
			}
			QPushButton[warning='true']:hover {
				background-color: rgba(240, 140, 0, 90);
			}
			QPushButton[warning='true']:pressed {
				background-color: rgba(240, 140, 0, 60);
			}
		"""

		self.setStyleSheet(self.theme)
		
def svgIcon(name, size = (64, 64), color = pya.QColor(0,0,0,150)):
    dirPath   = os.path.dirname(__file__) 
    genPath   = lambda rPath : os.path.realpath(os.path.join(dirPath, *rPath.split("/")))
    iconPath  = genPath("../icon")
    renderer  = pya.QSvgRenderer(f"{iconPath}/{name}.svg")
    pixmap    = pya.QPixmap(size[0], size[1])
    pixmap.fill(pya.QColor(0,0,0,0))
    painter   = pya.QPainter(pixmap)
    renderer.render(painter)
    painter.setCompositionMode(painter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), color)
    painter.end()
    return pya.QIcon(pixmap)

if __name__ == '__main__':
    a = pya.QWidget()
    l = pya.QVBoxLayout(a)

    
    pb = PushButton(
        text = "  minimize", 
        icon = svgIcon("trash-can-solid"),    
        parent = a,
    )
    l.addWidget(pb)
    a.setLayout(l)
    a.show()
