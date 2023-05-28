    def plotsAcceleration(self):
        layoutAcceleration = QtWidgets.QVBoxLayout(self.ui.graphicsViewAcceleration)
        self.figurePlotAcceleration = plt.figure(facecolor="#191B21")
        self.figurePlotAcceleration.subplots_adjust(left=0.035, bottom=0.045, right=1.0, top=1.0)

        self.canvasIlluminattion = FigureCanvas(self.figurePlotAcceleration)

        self.toolbarAcceleration = NavigationToolbar(self.canvasAcceleration, self)
        self.toolbarAcceleration.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border: 0px;\n"
                                   "border-radius: 17px")
        dataAcceleration = [random.random() for i in range(10)]

        # create an axis
        self.axAcceleration = self.figurePlotAcceleration.add_subplot(111)

        self.axAcceleration.set_facecolor("#191B21")

        # plot data
        self.Acceleration.plot(dataAcceleration, '*-')
        layoutAcceleration.addWidget(self.toolbarAcceleration)
        layoutAcceleration.addWidget(self.canvasAcceleration)