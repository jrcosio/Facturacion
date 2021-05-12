# -*- coding: utf-8 -*-

from VentanaMensaje import VentanaMensaje
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Principal(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi()


    def setupUi(self):
        self.resize(780, 505)
        self.setMinimumSize(QtCore.QSize(780, 505))
        self.setMaximumSize(QtCore.QSize(780, 505))
        self.setWindowTitle("Facturación Joyería Blanco")
        self.setStyleSheet("""
                QWidget {
                        background-color: rgb(38, 39, 65);
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
                QLineEdit{
                        color: rgb(0, 0, 0);
                        background-color: rgba(255, 255, 255, 0);
                        border:none;
                        border-bottom: 1px solid rgb(79, 82, 140);
                }
                """)

        self.centralwidget = QtWidgets.QWidget(self)
        
        self.frame_Inicio = QtWidgets.QFrame(self.centralwidget)
        self.frame_Inicio.setGeometry(QtCore.QRect(227, 12, 541, 481))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.frame_Inicio.setFont(font)
        self.frame_Inicio.setStyleSheet("""
                QFrame {
                        background-color: rgb(206, 206, 209);
                        border: 2px solid rgb(204, 0, 0);
                        border-radius: 30px;
                }
                """)
 
        self.frame_Menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_Menu.setGeometry(QtCore.QRect(12, 114, 201, 381))
        self.frame_Menu.setStyleSheet("""
                QFrame{
                        border-radius: 20px;
                        border: 2px solid rgb(80, 82, 140);
                }
                """)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_Menu)
        self.verticalLayout_2.setContentsMargins(12, 12, -1, 12)

        self.lbMenu = QtWidgets.QLabel(self.frame_Menu)
        self.lbMenu.setStyleSheet("""
                QLabel{
                        color: rgb(206, 206, 209);
                        border:none;
                        border-bottom: 1px solid rgb(206, 206, 209);
                }
                """)
        self.lbMenu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbMenu.setText("Menú")

        self.verticalLayout_2.addWidget(self.lbMenu)

        self.LayoutMenu = QtWidgets.QVBoxLayout()

        self.btnInicio = QtWidgets.QPushButton(self.frame_Menu)
        self.btnInicio.setText("Inicio")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInicio.setIcon(icon)
        self.btnInicio.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnInicio)
    
        self.btnClientes = QtWidgets.QPushButton(self.frame_Menu)
        self.btnClientes.setText("Clientes")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/gente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClientes.setIcon(icon)
        self.btnClientes.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnClientes)

        self.btnFacturas = QtWidgets.QPushButton(self.frame_Menu)
        self.btnFacturas.setText("Facturas")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/factura2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFacturas.setIcon(icon1)
        self.btnFacturas.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnFacturas)

        self.btnPresupuestos = QtWidgets.QPushButton(self.frame_Menu)
        self.btnPresupuestos.setText("Presupuestos")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Iconos/presupuesto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPresupuestos.setIcon(icon2)
        self.btnPresupuestos.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnPresupuestos)

        self.btnConsultas = QtWidgets.QPushButton(self.frame_Menu)
        self.btnConsultas.setText("Consultas")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Iconos/consulta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultas.setIcon(icon3)
        self.btnConsultas.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnConsultas)

        self.btnConfig = QtWidgets.QPushButton(self.frame_Menu)
        self.btnConfig.setText("Configuración")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Iconos/config2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfig.setIcon(icon4)
        self.btnConfig.setIconSize(QtCore.QSize(45, 45))
        self.LayoutMenu.addWidget(self.btnConfig)

        self.verticalLayout_2.addLayout(self.LayoutMenu)

        self.frame_Usuario = QtWidgets.QFrame(self.centralwidget)
        self.frame_Usuario.setGeometry(QtCore.QRect(12, 12, 199, 106))
        self.frame_Usuario.setStyleSheet("""
                QFrame{
                        background-color: rgba(255, 255, 255, 0);
                }
                QLabel {
                        color: rgb(206, 206, 209);
                }
                """)
        
        self.lbTitulo = QtWidgets.QLabel(self.frame_Usuario)
        self.lbTitulo.setGeometry(QtCore.QRect(10, 0, 161, 19))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lbTitulo.setFont(font)
        self.lbTitulo.setStyleSheet("color: rgb(251, 215, 110);")
        self.lbTitulo.setText(":: Facturación ::")
        self.lbTitulo.setAlignment(QtCore.Qt.AlignCenter)
      
        self.lbIconoUser = QtWidgets.QLabel(self.frame_Usuario)
        self.lbIconoUser.setGeometry(QtCore.QRect(30, 30, 64, 64))
        self.lbIconoUser.setPixmap(QtGui.QPixmap("Iconos/user.png"))
        self.lbIconoUser.setScaledContents(True)
        self.lbIconoUser.setAlignment(QtCore.Qt.AlignCenter)
        
        self.lbUsuario = QtWidgets.QLabel(self.frame_Usuario)
        self.lbUsuario.setGeometry(QtCore.QRect(100, 40, 101, 20))
        self.lbUsuario.setStyleSheet("color: rgb(198, 196, 220);")
        self.lbUsuario.setText("Usuario")
        self.lbUsuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.btnSalir = QtWidgets.QPushButton(self.frame_Usuario)
        self.btnSalir.setGeometry(QtCore.QRect(100, 60, 81, 31))
        self.btnSalir.setStyleSheet("""
                QPushButton{
	                border-radius: 10px;
	                background-color: rgba(102, 102, 102,0);
	                color:rgb(206, 206, 209);
                }
                QPushButton:hover {
	                border-radius: 10px;
	                background-color: rgb(102, 255, 204);
	                color: rgb(252, 1, 7);
                }
                QPushButton:pressed {
                        border-radius: 10px;
                        background-color: rgb(253, 102, 102);
                        color: rgb(255, 255, 255);
                }
                """)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Iconos/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon5)
        self.btnSalir.setIconSize(QtCore.QSize(24, 24))
        self.btnSalir.setText("Salir")

        self.lbEtiquetaUsuario = QtWidgets.QLabel(self.frame_Usuario)
        self.lbEtiquetaUsuario.setGeometry(QtCore.QRect(100, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbEtiquetaUsuario.setFont(font)
        self.lbEtiquetaUsuario.setText("Usuario/a:")
        self.lbEtiquetaUsuario.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.setCentralWidget(self.centralwidget)

        self.eventos()
    
    def eventos(self):
            self.btnSalir.clicked.connect(lambda:self.close())

            
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        window = VentanaMensaje("SALIR","¿Desea cerrar el programa de Facturación?")
        window.exec()

        if window.OK :
             event.accept()
        else:
             event.ignore()

    
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Principal()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
