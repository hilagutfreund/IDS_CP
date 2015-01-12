#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

#------------Globals-------------
#bad practice
isOn = False # Whether or not the system is monitoring the line
urlList = [] # Urls to capture as they come across the line
listContainer = QtGui.QFormLayout()
percent = ""
#--------------------------------
def updatePercentBool():
    count = 0
    for i in range(len(urlList)):
        if urlList[i].flag:
            count += 1
    updatePerBool = float(count)/ float(len(urlList)) * 100.0
    percent.setText(str("%.2f" % updatePerBool) + "% flagged")

class ListItem():
    url = ''
    flag = False
    def __init__(self,url2,flag2):
        self.url = url2
        self.flag = flag2

#-----------Test Data------------
urlList.append(ListItem('test 1',True))
urlList.append(ListItem('test 2',False))
urlList.append(ListItem('test 3',False))
#--------------------------------


class List(QtGui.QWidget):
    def __init__(self, items):
        QtGui.QWidget.__init__(self)
        mygroupbox = QtGui.QGroupBox()
        for i in range(len(items)):
            listContainer.addRow(QtGui.QLabel(items[i].url))
        mygroupbox.setLayout(listContainer)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(scroll)


    @staticmethod
    def addLine(listItem):
        # TODO: Add lines of colored urls to the scroll view
        print 'addLine'
        urlList.append(listItem)
        label = QtGui.QLabel(listItem.url)
        color = 'color: red' if listItem.flag else 'color: green'
        label.setStyleSheet(color)
        listContainer.addRow(label)
        updatePercentBool()


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

            listView.addLine(ListItem("TESTTTt",isOn))

        self.button = QtGui.QPushButton('On/Off', self)
        self.button.clicked.connect(handleButton)
        #-------------------------------------

        
        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.button, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        
        global percent
        percent = QtGui.QLabel("0 % flagged")
        grid.addWidget(percent, 2, 0)
       
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

