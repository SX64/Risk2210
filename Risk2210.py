#!/usr/bin/env python

#need to figure out QT

#need to copy over what I have with java

#ideas that need to be implemented: //in no particular order
#space station
#commanders (is a guy)
#borders
#territories
#guys
#commander types
#player
#turn
#turn order
#the moon
#regions, for lack of the correct term
#bonuses (technically boni)
#cards
#card types
#energy
#dice
#an attack
#contiguity
#eight sided dice
#water vs land vs moon territories
#territory ownership
#contiguity
#
"""
#OS X 10.9.3
#using PySide 1.2.1
#using Qt 4.8.6
#chmod +x this file, then cd [wherever this is], ./Risk2210.py
"""




import sys
import random
from PySide import *


#MacBook panel is 1440x900
width = 1400
height = 860
gfxOff = 40


"""
app = QtGui.QApplication(sys.argv)

board = QtGui.QWidget()
board.resize(width, height)
board.setWindowTitle('earth')
board.show()

#moon = QtGui.QWidget()
#moon.resize(250, 150)
#moon.setWindowTitle('moon')
# moon.show()

sys.exit(app.exec_())

"""
class test:
	def amount():
		print 'called'
		

class boardGUI(QtGui.QWidget):
    
    def __init__(self):
        super(boardGUI, self).__init__()
        
        self.initUI()
        
        
        
        
        
    def initUI(self):
    	#QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        #self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Button\'s spleen', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')
        foo = test()
        btn.clicked.connect(foo.amount)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
    
    	qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 150)
    
    
        self.setGeometry(gfxOff, gfxOff, width, height)
        self.setWindowTitle('Risk 2210')
        #self.setWindowIcon(QtGui.QIcon('web.png'))        this for title bar
    
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = boardGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

























