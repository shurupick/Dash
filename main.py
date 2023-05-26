import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout

from ui_mainwindow import Ui_MainWindow
import pyqtgraph as pg
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random


from matplotlib.backends.qt_compat import QtWidgets


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.buttons()
        self.plotsPressure()

    def buttons(self):
        self.ui.labelLineTemp.hide()
        self.ui.labelLineAcceleration.hide()
        self.ui.labeLinePressure.hide()
        self.ui.labelLineIlluminattion.hide()


        self.ui.pushButtonTemp.clicked.connect(self.pushButtonTempClicked)
        self.ui.pushButtonPressure.clicked.connect(self.pushButtonPressureClicked)
        self.ui.pushButtonIllumination.clicked.connect(self.pushButtonIlluminationClicked)
        self.ui.pushButtonAcceleration.clicked.connect(self.pushButtonAccelerationClicked)

    def plotsPressure(self):
        layout = QtWidgets.QVBoxLayout(self.ui.graphicsViewPressure)
        self.figure = plt.figure(facecolor="#191B21")
        self.figure.subplots_adjust(left=0.035, bottom=0.045, right=1.0, top=1.0)

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("background-color: rgb(103, 103, 103);\n"
                                   "border: 0px;\n"
                                   "border-radius: 17px")
        data = [random.random() for i in range(10)]

        # create an axis
        self.ax = self.figure.add_subplot(111)

        self.ax.set_facecolor("#191B21")

        # plot data
        self.ax.plot(data, '*-')
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

    def activeTemperatureButton(self):
        self.ui.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_white.svg);\n"
                                             "}\n")

        self.ui.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
                                                 "	\n"
                                                 "	background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-ser.svg);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-white.svg);\n"
                                                 "\n"
                                                 "}")

        self.ui.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
                                                     "	\n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	\n"
                                                     "	border-image: url(:/icons/light-ser.svg);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    \n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/light-white.svg);\n"
                                                     "\n"
                                                     "}")

        self.ui.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "\n"
                                                     "	border-image: url(:/icons/movement-sensor-ser.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/movement-sensor-white.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "")

    def activePressureButton(self):
        self.ui.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
                                                 "	\n"
                                                 "	background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-white.svg);\n"
                                                 "}\n")
        self.ui.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
                                                     "	\n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	\n"
                                                     "	border-image: url(:/icons/light-ser.svg);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    \n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/light-white.svg);\n"
                                                     "\n"
                                                     "}")

        self.ui.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "\n"
                                                     "	border-image: url(:/icons/movement-sensor-ser.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/movement-sensor-white.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "")

        self.ui.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_ser.svg);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_white.svg);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")

    def activeIlluminationButton(self):
        self.ui.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
                                                     "	\n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	\n"
                                                     "	border-image: url(:/icons/light-white.svg);\n"
                                                     "}\n")

        self.ui.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
                                                 "	\n"
                                                 "	background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-ser.svg);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-white.svg);\n"
                                                 "\n"
                                                 "}")

        self.ui.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "\n"
                                                     "	border-image: url(:/icons/movement-sensor-ser.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/movement-sensor-white.svg);\n"
                                                     "\n"
                                                     "}\n"
                                                     "")

        self.ui.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_ser.svg);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_white.svg);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")

    def activeAccelerationButton(self):
        self.ui.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
                                                     "background-color: rgb(25, 27, 33);\n"
                                                     "\n"
                                                     "	border-image: url(:/icons/movement-sensor-white.svg);\n"
                                                     "\n"
                                                     "}\n")

        self.ui.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_ser.svg);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "	background-color: rgb(25, 27, 33);\n"
                                             "	border: 0px;\n"
                                             "	border-image: url(:/icons/temp_white.svg);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")
        self.ui.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
                                                 "	\n"
                                                 "	background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-ser.svg);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(25, 27, 33);\n"
                                                 "	border-image: url(:/icons/pressure-white.svg);\n"
                                                 "\n"
                                                 "}")

        self.ui.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
                                                     "	\n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	\n"
                                                     "	border-image: url(:/icons/light-ser.svg);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    \n"
                                                     "	background-color: rgb(25, 27, 33);\n"
                                                     "	border-image: url(:/icons/light-white.svg);\n"
                                                     "\n"
                                                     "}")

    def pushButtonTempClicked(self):
        self.ui.labelLineAcceleration.hide()
        self.ui.labeLinePressure.hide()
        self.ui.labelLineIlluminattion.hide()
        self.ui.labelLineTemp.show()
        self.activeTemperatureButton()
        self.ui.stackedWidget.setCurrentIndex(1)

    def pushButtonPressureClicked(self):
        self.ui.labelLineAcceleration.hide()
        self.ui.labelLineIlluminattion.hide()
        self.ui.labelLineTemp.hide()
        self.ui.labeLinePressure.show()
        self.activePressureButton()
        self.ui.stackedWidget.setCurrentIndex(2)

    def pushButtonIlluminationClicked(self):
        self.ui.labelLineAcceleration.hide()
        self.ui.labeLinePressure.hide()
        self.ui.labelLineTemp.hide()
        self.ui.labelLineIlluminattion.show()
        self.activeIlluminationButton()
        self.ui.stackedWidget.setCurrentIndex(3)

    def pushButtonAccelerationClicked(self):
        self.ui.labeLinePressure.hide()
        self.ui.labelLineIlluminattion.hide()
        self.ui.labelLineTemp.hide()
        self.ui.labelLineAcceleration.show()
        self.activeAccelerationButton()
        self.ui.stackedWidget.setCurrentIndex(4)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
