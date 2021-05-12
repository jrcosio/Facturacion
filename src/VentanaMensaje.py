# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaMensaje(QtWidgets.QDialog):

    OK = False

    def __init__(self,Titulo,Mensaje,parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(Titulo,Mensaje)

    def setupUi(self,Titulo,Mensaje):
        self.resize(540, 192)
        self.setWindowTitle(Titulo)
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(38, 39, 65)
            }

            QPushButton{
                border-radius: 20px;
                background-color: rgb(248, 201, 35);
                color: rgb(0, 0, 0);
            }

            QPushButton:hover {
                border-radius: 20px;
                background-color: rgb(157, 122, 8);
                color: rgb(0, 0, 0);
            }

            QPushButton:pressed {
                border-radius: 20px;
                background-color: rgb(253, 102, 102);
                color: rgb(255, 255, 255);
            }
            QLabel{
                color: rgb(206, 206, 209);
            }
            """)
        self.lbIcono = QtWidgets.QLabel(self)
        self.lbIcono.setGeometry(QtCore.QRect(20, 20, 64, 64))
        self.lbIcono.setPixmap(QtGui.QPixmap("Iconos/exclamation.png"))
        self.lbIcono.setScaledContents(True)
        self.lbIcono.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 130, 271, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnCancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCancelar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/cerrar2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setIconSize(QtCore.QSize(42, 42))
        self.btnCancelar.setText("Cancelar")

        self.horizontalLayout.addWidget(self.btnCancelar)
        self.btnOK = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnOK.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/ok3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon1)
        self.btnOK.setIconSize(QtCore.QSize(42, 42))
        self.btnOK.setText("OK")

        self.horizontalLayout.addWidget(self.btnOK)

        self.lbTexto = QtWidgets.QLabel(self)
        self.lbTexto.setGeometry(QtCore.QRect(100, 10, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbTexto.setFont(font)
        self.lbTexto.setText(Mensaje)

        self.btnOK.clicked.connect(self.onOK)
        self.btnCancelar.clicked.connect(lambda:self.close())
    
    def onOK(self):
        self.OK = True
        self.close()
