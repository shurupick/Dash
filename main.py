import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtWidgets

import numpy as np

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.plotsPressure()


    def plotsPressure(self):
        layout = QtWidgets.QVBoxLayout(self.ui.graphicsViewPressure)
        self.figure = plt.figure(facecolor="#191B21")
        self.figure.subplots_adjust(left=0.035, bottom=0.045, right=1.0, top=1.0)

        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
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


class pushButtonsLogic(MainWindow):
    def __init__(self):
        super().__init__()
        self.u = self.ui
        self.buttons()

    def buttons(self):
        self.u.labelLineTemp.hide()
        self.u.labelLineAcceleration.hide()
        self.u.labeLinePressure.hide()
        self.u.labelLineIlluminattion.hide()

        self.u.pushButtonTemp.clicked.connect(self.pushButtonTempClicked)
        self.u.pushButtonPressure.clicked.connect(self.pushButtonPressureClicked)
        self.u.pushButtonIllumination.clicked.connect(self.pushButtonIlluminationClicked)
        self.u.pushButtonAcceleration.clicked.connect(self.pushButtonAccelerationClicked)

    def activeTemperatureButton(self):
        self.u.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
                                            "	background-color: rgb(25, 27, 33);\n"
                                            "	border: 0px;\n"
                                            "	border-image: url(:/icons/temp_white.svg);\n"
                                            "}\n")

        self.u.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
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
        self.u.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
                                                "	\n"
                                                "	background-color: rgb(25, 27, 33);\n"
                                                "	border-image: url(:/icons/pressure-white.svg);\n"
                                                "}\n")
        self.u.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
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
        self.u.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
                                                    "	\n"
                                                    "	background-color: rgb(25, 27, 33);\n"
                                                    "	\n"
                                                    "	border-image: url(:/icons/light-white.svg);\n"
                                                    "}\n")

        self.u.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
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
        self.u.pushButtonAcceleration.setStyleSheet(u"QPushButton {\n"
                                                    "background-color: rgb(25, 27, 33);\n"
                                                    "\n"
                                                    "	border-image: url(:/icons/movement-sensor-white.svg);\n"
                                                    "\n"
                                                    "}\n")

        self.u.pushButtonTemp.setStyleSheet(u"QPushButton {\n"
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
        self.u.pushButtonPressure.setStyleSheet(u"QPushButton {\n"
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

        self.u.pushButtonIllumination.setStyleSheet(u"QPushButton {\n"
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
        self.u.labelLineAcceleration.hide()
        self.u.labeLinePressure.hide()
        self.u.labelLineIlluminattion.hide()
        self.u.labelLineTemp.show()
        self.activeTemperatureButton()
        self.u.stackedWidget.setCurrentIndex(1)

    def pushButtonPressureClicked(self):
        self.u.labelLineAcceleration.hide()
        self.u.labelLineIlluminattion.hide()
        self.u.labelLineTemp.hide()
        self.u.labeLinePressure.show()
        self.activePressureButton()
        self.u.stackedWidget.setCurrentIndex(2)

    def pushButtonIlluminationClicked(self):
        self.u.labelLineAcceleration.hide()
        self.u.labeLinePressure.hide()
        self.u.labelLineTemp.hide()
        self.u.labelLineIlluminattion.show()
        self.activeIlluminationButton()
        self.u.stackedWidget.setCurrentIndex(3)

    def pushButtonAccelerationClicked(self):
        self.u.labeLinePressure.hide()
        self.u.labelLineIlluminattion.hide()
        self.u.labelLineTemp.hide()
        self.u.labelLineAcceleration.show()
        self.activeAccelerationButton()
        self.u.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pushButtonsLogic()
    window.show()
    sys.exit(app.exec())
