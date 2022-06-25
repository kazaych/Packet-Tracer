import UDP_socket
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.portbutton = QtWidgets.QPushButton(self.centralwidget)
        self.portbutton.setGeometry(QtCore.QRect(740, 760, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.portbutton.setFont(font)
        self.portbutton.setObjectName("portbutton")
        self.portbutton.clicked.connect(self.openport)
        self.dle = QtWidgets.QCheckBox(self.centralwidget)
        self.dle.setGeometry(QtCore.QRect(50, 810, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dle.setFont(font)
        self.dle.setObjectName("dle")
        self.tcp = QtWidgets.QCheckBox(self.centralwidget)
        self.tcp.setGeometry(QtCore.QRect(130, 810, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tcp.setFont(font)
        self.tcp.setObjectName("tcp")
        self.udp = QtWidgets.QCheckBox(self.centralwidget)
        self.udp.setGeometry(QtCore.QRect(220, 810, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.udp.setFont(font)
        self.udp.setObjectName("udp")
        self.portnum = QtWidgets.QLineEdit(self.centralwidget)
        self.portnum.setGeometry(QtCore.QRect(170, 770, 91, 21))
        self.portnum.setObjectName("portnum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 730, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setIndent(-8)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 770, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget_out = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_out.setGeometry(QtCore.QRect(25, 21, 1041, 731))
        self.listWidget_out.setObjectName("listWidget_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.portbutton.setText(_translate("MainWindow", "Open port"))
        self.dle.setText(_translate("MainWindow", "DLE"))
        self.tcp.setText(_translate("MainWindow", "TCP"))
        self.udp.setText(_translate("MainWindow", "UDP"))
        self.label.setText(_translate("MainWindow", "Parameters"))
        self.label_2.setText(_translate("MainWindow", "Port number"))

    def addtooutput(self, data):
        self.listWidget_out.addItem(data)

    def takeportnum(self):
        port = self.portnum.text()
        return port

    def openport(self):
        port = int(self.takeportnum())
        sock = UDP_socket.UdpSocket(port)
        raw = sock.sockopen()
        if raw == '':
            self.listWidget_out.addItem(QtWidgets.QListWidgetItem('Port is empty'))
        else:
            raw_out = QtWidgets.QListWidgetItem(str.upper(raw.hex()))
            self.listWidget_out.addItem(raw_out)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
