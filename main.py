import sys
 #import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtWidgets
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.plotsPressure()
        self.plotsTemp()
        self.plotsIlluminattion()
        self.plotsAcceleration()

    def plotsTemp(self):
        layoutTemp = QtWidgets.QVBoxLayout(self.ui.graphicsViewTemp)

        # создание layout и задание ему цевета
        # на нем будет распологаться сам рисунок
        figurePlotTemp = plt.figure(facecolor="#191B21")

        # задаем размеры рисунка графика на layout
        figurePlotTemp.subplots_adjust(left=0.075, bottom=0.120, right=1.0, top=0.975)

        canvasTemp = FigureCanvas(figurePlotTemp)

        toolbarTemp = NavigationToolbar(canvasTemp, self)
        toolbarTemp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "border: 0px;\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "border-radius: 17px")

        # create a data
        x = np.array([i for i in range(100)])
        y = np.array([np.random.uniform(22, 25) for i in range(100)])

        xnew = np.linspace(x.min(), x.max(), 400)

        spl = make_interp_spline(x, y, 7)
        dataTemp = spl(xnew)

        dispers, mean = statistics(dataTemp)


        # create an axis
        axTemp = figurePlotTemp.add_subplot(111)

        axTemp.spines[['top', 'right']].set_visible(False)
        axTemp.spines['bottom'].set_color("#676767")
        axTemp.spines['left'].set_color("#676767")
        axTemp.tick_params(colors='#ffffff', which='both')
        axTemp.xaxis.label.set_color("#ffffff")
        axTemp.yaxis.label.set_color("#ffffff")
        axTemp.set_facecolor("#191B21")  # цвет окна с графиком



        # Подписи для осей:
        plt.xlabel('Time (s)', fontsize=14)
        plt.ylabel('Temperature (°C)', fontsize=14)

        plt.ylim(min(dataTemp) - 2, max(dataTemp) + 2)
        plt.text(0, max(dataTemp) + 1, f"mean = {round(mean,3)}     dispersion = {round(dispers,3)}" , color = "#ffffff")

        # plot data
        axTemp.plot(xnew, dataTemp)
        layoutTemp.addWidget(toolbarTemp)
        layoutTemp.addWidget(canvasTemp)

    def plotsPressure(self):
        layoutPressure = QtWidgets.QVBoxLayout(self.ui.graphicsViewPressure)

        figurePlotPressure = plt.figure(facecolor="#191B21")
        figurePlotPressure.subplots_adjust(left=0.075, bottom=0.120, right=1.0, top=0.975)

        canvasPressure = FigureCanvas(figurePlotPressure)

        toolbarPressure = NavigationToolbar(canvasPressure, self)
        toolbarPressure.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: 0px;\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-radius: 17px")

        # create a data
        x = np.array([i for i in range(100)])
        y = np.array([np.random.uniform(22, 25) for i in range(100)])

        xnew = np.linspace(x.min(), x.max(), 400)

        spl = make_interp_spline(x, y, 7)
        dataPressure = spl(xnew)

        dispers, mean = statistics(dataPressure)


        # create an axis
        axPressure = figurePlotPressure.add_subplot(111)

        axPressure.spines[['top', 'right']].set_visible(False)
        axPressure.spines['bottom'].set_color("#676767")
        axPressure.spines['left'].set_color("#676767")
        axPressure.tick_params(colors='#ffffff', which='both')
        axPressure.xaxis.label.set_color("#ffffff")
        axPressure.yaxis.label.set_color("#ffffff")
        axPressure.set_facecolor("#191B21")  # цвет окна с графиком
        axPressure.set_facecolor("#191B21")

        # Подписи для осей:
        plt.xlabel('Time (s)', fontsize=14)
        plt.ylabel('Pressure (hPa)', fontsize=14)

        plt.ylim(min(dataPressure) - 2, max(dataPressure) + 2)
        plt.text(0, max(dataPressure) + 1, f"mean = {round(mean,3)}     dispersion = {round(dispers,3)}" , color = "#ffffff")

        # plot data
        axPressure.plot(xnew, dataPressure)
        layoutPressure.addWidget(toolbarPressure)
        layoutPressure.addWidget(canvasPressure)

    def plotsIlluminattion(self):
        layoutIlluminattion = QtWidgets.QVBoxLayout(self.ui.graphicsViewIllunination)

        figurePlotIlluminattion = plt.figure(facecolor="#191B21")
        figurePlotIlluminattion.subplots_adjust(left=0.075, bottom=0.120, right=1.0, top=0.975)

        canvasIlluminattion = FigureCanvas(figurePlotIlluminattion)

        toolbarIlluminattion = NavigationToolbar(canvasIlluminattion, self)
        toolbarIlluminattion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border: 0px;\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-radius: 17px")

        # create a data
        x = np.array([i for i in range(100)])
        y = np.array([np.random.uniform(22, 25) for i in range(100)])

        xnew = np.linspace(x.min(), x.max(), 400)

        spl = make_interp_spline(x, y, 7)
        dataIlluminattion = spl(xnew)

        dispers, mean = statistics(dataIlluminattion)

        # create an axis
        axIlluminattion = figurePlotIlluminattion.add_subplot(111)

        axIlluminattion.spines[['top', 'right']].set_visible(False)
        axIlluminattion.spines['bottom'].set_color("#676767")
        axIlluminattion.spines['left'].set_color("#676767")
        axIlluminattion.tick_params(colors='#ffffff', which='both')
        axIlluminattion.xaxis.label.set_color("#ffffff")
        axIlluminattion.yaxis.label.set_color("#ffffff")
        axIlluminattion.set_facecolor("#191B21")  # цвет окна с графиком

        # Подписи для осей:
        plt.xlabel('Time (s)', fontsize=14)
        plt.ylabel('Illuminattion (lx)', fontsize=14)

        plt.ylim(min(dataIlluminattion) - 2, max(dataIlluminattion) + 2)
        plt.text(0, max(dataIlluminattion) + 1, f"mean = {round(mean,3)}     dispersion = {round(dispers,3)}" , color = "#ffffff")

        # plot data
        axIlluminattion.plot(xnew, dataIlluminattion)
        layoutIlluminattion.addWidget(toolbarIlluminattion)
        layoutIlluminattion.addWidget(canvasIlluminattion)

    def plotsAcceleration(self):
        layoutAcceleration = QtWidgets.QVBoxLayout(self.ui.graphicsViewAcceleration)
        figurePlotAcceleration = plt.figure(facecolor="#191B21")
        figurePlotAcceleration.subplots_adjust(left=0.075, bottom=0.120, right=1.0, top=0.975)

        canvasAcceleration = FigureCanvas(figurePlotAcceleration)

        toolbarAcceleration = NavigationToolbar(canvasAcceleration, self)
        toolbarAcceleration.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border: 0px;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "border-radius: 17px")

        # create a data
        x = np.array([i for i in range(100)])
        y = np.array([np.random.uniform(10, 20) for i in range(100)])

        xnew = np.linspace(x.min(), x.max(), 200)

        spl = make_interp_spline(x, y, 7)
        dataAcceleration = spl(xnew)

        dispers, mean = statistics(dataAcceleration)

        # create an axis
        axAcceleration = figurePlotAcceleration.add_subplot(111)

        axAcceleration.spines[['top', 'right']].set_visible(False)
        axAcceleration.spines['bottom'].set_color("#676767")
        axAcceleration.spines['left'].set_color("#676767")
        axAcceleration.tick_params(colors='#ffffff', which='both')
        axAcceleration.xaxis.label.set_color("#ffffff")
        axAcceleration.yaxis.label.set_color("#ffffff")
        axAcceleration.set_facecolor("#191B21")  # цвет окна с графиком

        # Подписи для осей:
        plt.xlabel('Time (s)', fontsize=14)
        plt.ylabel('Acceleration (m/s^2)', fontsize=14)

        plt.ylim(min(dataAcceleration) - 2, max(dataAcceleration) + 2)
        plt.text(0, max(dataAcceleration) + 1, f"mean = {round(mean,3)}     dispersion = {round(dispers,3)}" , color = "#ffffff")

        axAcceleration.set_facecolor("#191B21")

        # plot data
        axAcceleration.plot(xnew, dataAcceleration)
        layoutAcceleration.addWidget(toolbarAcceleration)
        layoutAcceleration.addWidget(canvasAcceleration)


class pushButtonsLogic(MainWindow):


    def __init__(self):
        super().__init__()
        self.u = self.ui
        self.buttons()
        self.u.stackedWidget.setCurrentIndex(0)

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

def statistics(data):
    mean = sum(data)/len(data)
    sqrmean = sum([i**2 for i in data])/len(data)
    meansqr = mean**2
    dispersion = sqrmean - meansqr
    return dispersion, mean




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pushButtonsLogic()

    window.show()

    sys.exit(app.exec())
