#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#------------Globals-------------
#bad practice
isOn = False # Whether or not the system is monitoring the line
urlList = [] # Urls to capture as they come across the line
#--------------------------------


class List(QtGui.QWidget):
    def __init__(self, val):
        global urlList
        QtGui.QWidget.__init__(self)
        mygroupbox = QtGui.QGroupBox('this is my groupbox')
        myform = QtGui.QFormLayout()
        combolist = []
        for i in range(val):
            urlList.append(QtGui.QLabel('mylabel'))
            combolist.append(QtGui.QComboBox())
            myform.addRow(urlList[i],combolist[i])
        mygroupbox.setLayout(myform)
        scroll = QtGui.QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(scroll)

    def updateBox():
        # TODO:
        print 'todo'

    def addLine(text):
        # TODO: Add lines of colored urls to the scroll view
        print 'addLine'
        urlList.append('NEW LINEE')
        combolist.append(QtGui.QComboBox())

        myform.addRow(urlList[-1],combolist[-1])


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #-----------On/Off button-------------
        def handleButton(self):
            global isOn #python 'gotcha'
            # TODO: Call python backend here
            isOn = not isOn
            if isOn:
                print 'isOn'
            else:
                print 'isOff'

        self.button = QtGui.QPushButton('On/Off', self)
        self.button.clicked.connect(handleButton)
        #-------------------------------------




        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = List(20)


        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.button, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

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

