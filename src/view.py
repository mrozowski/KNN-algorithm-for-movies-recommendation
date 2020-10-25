

from PyQt5 import QtCore, QtGui, QtWidgets
import presenter

class View(object):
    def __init__(self):
        self.recom = []
        self.listWidget = None
        self.presenter = None

    def set_presenter(self, _presenter: presenter.Presenter):
        self.presenter = _presenter

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget{background-color: #141B32;}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidged{background-color: #141B32;}")
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color: white;}")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(160, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showButton.setFont(font)
        self.showButton.setStyleSheet("QPushButton{background-color: #8296DE;}")
        self.showButton.setObjectName("showButton")
        self.showButton.clicked.connect(lambda: self.presenter.on_button_clicked())


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color: white;}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(70, 170, 311, 261))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("QListWidget{color: white;}")


        self.movie1 = QtWidgets.QLabel(self.centralwidget)
        self.movie1.setGeometry(QtCore.QRect(460, 130, 291, 61))
        self.movie1.setObjectName("movie1")
        self.recom.append(self.movie1)

        self.movie2 = QtWidgets.QLabel(self.centralwidget)
        self.movie2.setGeometry(QtCore.QRect(460, 210, 291, 61))
        self.movie2.setObjectName("movie2")
        self.recom.append(self.movie2)

        self.movie3 = QtWidgets.QLabel(self.centralwidget)
        self.movie3.setGeometry(QtCore.QRect(460, 290, 291, 61))
        self.movie3.setObjectName("movie3")
        self.recom.append(self.movie3)

        self.movie4 = QtWidgets.QLabel(self.centralwidget)
        self.movie4.setGeometry(QtCore.QRect(460, 370, 291, 61))
        self.movie4.setObjectName("movie4")
        self.recom.append(self.movie4)

        self.movie5 = QtWidgets.QLabel(self.centralwidget)
        self.movie5.setGeometry(QtCore.QRect(460, 450, 291, 61))
        self.movie5.setObjectName("movie5")
        self.recom.append(self.movie5)

        for a in self.recom:
            font = QtGui.QFont()
            font.setPointSize(10)
            a.setFont(font)
            a.setStyleSheet("QLabel{border: 2px solid #8296DE; border-radius: 10px; color: white; padding-left: 5px;}")
            a.hide()
        self.presenter.set_list()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose one of your favourite videos and KNN algorithm will recommend you 5 similar movies you might like"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.label_3.setText(_translate("MainWindow", "Algorithm recommendation"))


