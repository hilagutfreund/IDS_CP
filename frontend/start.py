#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
sys.path.append('../backend/')
from Sniffer import StartSniffer, StopSniffer
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
            listContainer.insertRow(0,QtGui.QLabel(items[i].url))
        mygroupbox.setLayout(listContainer)

        scroll = QtGui.QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(scroll)


  #  @staticmethod
def AddLine(listItem):
    # TODO: Add lines of colored urls to the scroll view
    print 'addLine'
    urlList.append(listItem)
    label = QtGui.QLabel(listItem.url)
    color = 'color: red' if listItem.flag else 'color: green'
    label.setStyleSheet(color)
    listContainer.insertRow(0,label)
    updatePercentBool()


def snifferCallback(dest_ip_addr):
    print 'this is the mofoin dest ip: ' + dest_ip_addr
    next = dest_ip_addr.split(".")
    bo = True
    if int(next[0]) > 110:
        bo = False
    AddLine(ListItem(dest_ip_addr,bo))


class MyThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)
    def run( self ):
        # returns dest_ip_addr
        global isOn #python 'gotcha'
        isOn = not isOn
        if isOn:
            StartSniffer(self.updated.emit)
        else:
            StopSniffer()

class MainWindow(QtGui.QWidget):
    global urlList
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        listView = List(urlList)

        self._thread = MyThread(self)
        self._thread.updated.connect(snifferCallback)

        self.button = QtGui.QPushButton('On/Off', self)
        self.button.clicked.connect(self._thread.start)
        #-------------------------------------

        titleEdit = QtGui.QLineEdit()
        titleEdit.setPlaceholderText("Filter Search")
        self.setFocus()

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

