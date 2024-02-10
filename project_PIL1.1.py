import os
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL.ImageQt import *
from PIL import ImageFilter
from PIL.ImageFilter import*

app = QApplication([])
app.setStyleSheet('''QWidget
                    {background:#E8D7CF;
                    font-size: 12pt;
                    color:#E66A74;}
                    ''')
window = QWidget()
window.resize(1000, 700)
window.setWindowTitle('project_PIL1.1')
#window.setWindowIcon("ico1.ico")


theme = QLabel("Всесвіт Cередзем'я Толкієна")
label_t = QLabel('')
label_t.setFixedSize(800, 600)
label_p = QLabel('')

left = QPushButton('<<↢')
right = QPushButton('↣>>')

v1 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

h1.addWidget(left)
h1.addWidget(theme, alignment = Qt.AlignCenter)
h1.addWidget(right)
h2.addWidget(label_t)
h2.addWidget(label_p)
v1.addLayout(h1)
v1.addLayout(h2)

m=os.path.abspath('1_txt.txt')
t=open(m, encoding='utf-8')
label_t.setText(t.read())
label_p.hide()
pixmapimage = QPixmap('1.jpg')
w,h = label_p.width(), label_p.height()
pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

i = 1
def button_right():
    global i
    i = i + 1
    if i == 7:
        i = 1
    t=open(str(i)+'_txt.txt',encoding='utf-8')
    label_t.setText(t.read())

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

right.clicked.connect(button_right)

def button_left():
    global i
    i = i - 1
    if i == 0:
        i = 6
    t=open(str(i)+'_txt.txt',encoding='utf-8')
    label_t.setText(t.read())

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

left.clicked.connect(button_left)


window.setLayout(v1)
window.show()
app.exec_()