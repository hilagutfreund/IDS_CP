#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui

print 'Working'

def main():

    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(800, 500)
    w.move(100, 100)
    w.setWindowTitle('Sniffer Deluxe')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()