import os
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

from PIL import Image
from PIL.ImageQt import *
from PIL import ImageFilter
from PIL.ImageFilter import*

app = QApplication([])
app.setStyleSheet('''QWidget
                    {background:#E6D0B8;
                    font-size: 12pt;
                    color:#804737;}
                    ''')
window = QWidget()
window.resize(1000, 700)
window.setWindowTitle('project_PIL1.1')
window.setWindowIcon(QtGui.QIcon('ico1.ico'))


theme = QLabel("Всесвіт Cередзем'я Толкієна")
label_t = QLabel('')
label_t.setFixedSize(800, 600)
label_p = QLabel('')
#list_p = QLabel('1-6') #int(i) abo float(i)
list_label = QLineEdit('')
list_label.setPlaceholderText('1-6')

search = QPushButton('Пошук')
page = QLabel('1')

left = QPushButton('<<↢')
#left.setStyleSheet('''
#                    border-radius:15px;
#                    ''')
right = QPushButton('↣>>')
#right.setStyleSheet('''
#                    border-radius:15px;
#                    ''')

v1 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()

h1.addWidget(left)
h1.addWidget(theme, alignment = Qt.AlignCenter)
h1.addWidget(right)
h3.addWidget(list_label)
h3.addWidget(search)
h2.addWidget(label_t)
h2.addWidget(label_p)
h4.addWidget(page, alignment= Qt.AlignCenter)
v1.addLayout(h1)
#v1.addWidget(list_p, alignment=Qt.AlignCenter)
v1.addLayout(h3)
v1.addLayout(h2)
v1.addLayout(h4)

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
    i = int(i) + 1
    if i == 7:
        i = 1
    t=open(str(i)+'_txt.txt',encoding='utf-8')
    label_t.setText(t.read())
    page.setText(str(i))

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

right.clicked.connect(button_right)

def button_left():
    global i
    i = int(i) - 1
    if i == 0:
        i = 6
    t=open(str(i)+'_txt.txt',encoding='utf-8')
    label_t.setText(t.read())
    page.setText(str(i))

    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

left.clicked.connect(button_left)

def searching():
    global i
    i = list_label.text()
    t=open(str(i)+'_txt.txt',encoding='utf-8')
    label_t.setText(t.read())
    page.setText(str(i))
    
    label_p.hide()
    pixmapimage = QPixmap(str(i)+'.jpg')
    w,h = label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(200, 500, Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

search.clicked.connect(searching)

window.setLayout(v1)
window.show()
app.exec_()
