#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#------------Globals-------------
#bad practice
isOn = False # Whether or not the system is monitoring the line
urlList = [] # Urls to capture as they come across the line
listContainer = QtGui.QFormLayout()
#--------------------------------

#-----------Test Data------------
urlList.append('test 1')
urlList.append('test 2')
urlList.append('test 3')
#--------------------------------


class List(QtGui.QWidget):
    def __init__(self, items):
        QtGui.QWidget.__init__(self)
        mygroupbox = QtGui.QGroupBox()
        for i in range(len(items)):
            listContainer.addRow(QtGui.QLabel(items[i]))
        mygroupbox.setLayout(listContainer)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(scroll)

    def updateBox():
        for i in range(val):
            listContainer.addRow(u)

    @staticmethod
    def addLine(text, flag):
        # TODO: Add lines of colored urls to the scroll view
        print 'addLine'
        urlList.append(text)
        label = QtGui.QLabel(urlList[-1])
        if flag:
            color = 'color: red' if flag else 'color: green'
            label.setStyleSheet(color)
        listContainer.addRow(label)


class MainWindow(QtGui.QWidget):
    global urlList
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        listView = List(urlList)

        #-----------On/Off button-------------
        def handleButton(self):
            global isOn #python 'gotcha'
            # TODO: Call python backend here
            isOn = not isOn
            if isOn:
                print 'isOn'
            else:
                print 'isOff'

            listView.addLine("TESTTTt",isOn)

        self.button = QtGui.QPushButton('On/Off', self)
        self.button.clicked.connect(handleButton)
        #-------------------------------------




        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()


        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.button, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(listView, 3, 1, 5, 1)

        self.setLayout(grid)

        self.resize(800, 500)
        self.move(100, 100)
        self.setWindowTitle('Sniffer Deluxe')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    bringWindowToFront(w)

    sys.exit(app.exec_())

def bringWindowToFront(window):
    # only somewhat works
    window.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    # this will activate the window
    window.activateWindow()


if __name__ == '__main__':
    main()

